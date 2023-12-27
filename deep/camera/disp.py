import cv2
import numpy as np

def compute_left_disparity_map(img_left, img_right):
    
    ### START CODE HERE ###
    
    # Parameters
    num_disparities = 6*16
    block_size = 11
    
    min_disparity = 0
    window_size = 6
    
    img_left = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
    img_right = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)

    
    # Stereo BM matcher
    left_matcher_BM = cv2.StereoBM_create(
        numDisparities=num_disparities,
        blockSize=block_size
    )

    # Stereo SGBM matcher
    left_matcher_SGBM = cv2.StereoSGBM_create(
        minDisparity=min_disparity,
        numDisparities=num_disparities,
        blockSize=block_size,
        P1=8 * 3 * window_size ** 2,
        P2=32 * 3 * window_size ** 2,
        mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
    )

    # Compute the left disparity map
    disp_left = left_matcher_SGBM.compute(img_left, img_right).astype(np.float32)/16
    
    ### END CODE HERE ###
    
    return disp_left



def calc_depth_map(disp_left, k_left, t_left, t_right, bu):

    ### START CODE HERE ###
    
    # Get the focal length from the K matrix
    f = k_left[0, 0]
    print(f)
    bo=0
    # Get the distance between the cameras from the t matrices (baseline)
    b = bu #= t_left[bo] - t_right[bo]

    # Replace all instances of 0 and -1 disparity with a small minimum value (to avoid div by 0 or negatives)
    disp_left[disp_left == 0] = 0.1
    disp_left[disp_left == -1] = 0.1

    # Initialize the depth map to match the size of the disparity map
    depth_map = np.ones(disp_left.shape, np.single)

    # Calculate the depths 
    depth_map[:] = b / disp_left[:]
    
    ### END CODE HERE ###
    
    return depth_map
# Compute the disparity map using the fuction above

k_left=np.array([[526.77741422 ,0,327.23449594],
 [  0, 523.81288438, 242.27606072], [  0,0.,1. ]], dtype=float)

t_left=np.array([1.22440887,-4.03340983,14.77109359])
t_right=np.array([ 7.14905223,-5.01298205,14.93269914])


def dist(depth_map, frame1):
    depth_thresh = 100.0 # Threshold for SAFE distance (in cm)
     
    # Mask to segment regions with depth less than threshold
    mask = cv2.inRange(depth_map,10,depth_thresh)
     
    # Check if a significantly large obstacle is present and filter out smaller noisy regions
    if np.sum(mask)/255.0 > 0.01*mask.shape[0]*mask.shape[1]:
     
      # Contour detection 
      contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      cnts = sorted(contours, key=cv2.contourArea, reverse=True)
       
      # Check if detected contour is significantly large (to avoid multiple tiny regions)
      if cv2.contourArea(cnts[0]) > 0.01*mask.shape[0]*mask.shape[1]:
     
        x,y,w,h = cv2.boundingRect(cnts[0])
     
        # finding average depth of region represented by the largest contour 
        mask2 = np.zeros_like(mask)
        cv2.drawContours(mask2, cnts, 0, (255), -1)
        cv2.drawContours(frame1, cnts, 0, (255), -1)
        #cv2.imshow('mask2',mask2)
        # Calculating the average depth of the object closer than the safe distance
        depth_mean, _ = cv2.meanStdDev(depth_map, mask=mask2)
         
        # Display warning text
        cv2.putText(frame1, "WARNING !", (x+5,y-40), 1, 2, (0,0,255), 2, 2)
        cv2.putText(frame1, "Object at", (x+5,y), 1, 2, (100,10,25), 2, 2)
        cv2.putText(frame1, "%.2f cm"%depth_mean, (x+5,y+40), 1, 2, (100,10,25), 2, 2)
     
    else:
      cv2.putText(frame1, "SAFE!", (100,100),1,3,(0,255,0),2,3)
     
    cv2.imshow('output_canvas',frame1)



def nothing(x):
    pass

import time
import cv2
import numpy as np
import matplotlib.pyplot as plt
vid1 = cv2.VideoCapture(0)
vid2 = cv2.VideoCapture(2)
#cv2.namedWindow('image')
#cv2.createTrackbar('R', 'image', 7, 50, nothing)

while True:
    ret1, frame1=vid1.read()
    ret2, frame2 = vid2.read()
    frame1 = cv2.rotate(frame1, cv2.ROTATE_180)
    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        # if 'q' key-pressed break out
        break

    bu = 7.5 #cv2.getTrackbarPos('R', 'image')
    disp_left = compute_left_disparity_map(frame1, frame2)
    depth_map_left = calc_depth_map(disp_left, k_left, t_left, t_right, bu)
    print(depth_map_left[320,240]*100)
    cv2.putText(frame1, f"{depth_map_left[320,240]*100} cm", (255,250), 1, 2, (0,0,255), 2, 2)
    # Get the depth map by calling the above function
    #disp_left=9/disp_left
    dist(depth_map_left, frame1)
    # Display the depth map
    #plt.figure(figsize=(8, 8) dpi=100)
    #plt.imshow(depth_map_left, cmap='flag')
    #plt.show()
    cv2.imshow("depth", disp_left)
    #cv2.waitKey(0)
# Display the depth map

vid1.release()
vid2.release()
cv2.destroyAllWindows()


