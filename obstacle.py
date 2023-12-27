from talk import talk
def obstacle(R1, R2):
      decision="Pas d'obstacle"
      if (R1[0]>=R2[2]) or (R1[2]<=R2[0]) or (R1[3]<=R2[1]) or (R1[1]>=R2[3]):
          decision=""
          if (R1[0]>=R2[2]):
              decision+="A gauche "
          if (R1[2]<=R2[0]):
              decision+="A droite"
          if (R1[3]<=R2[1]):
              decision+="Stop"
          if (R1[1]>=R2[3]):
              decision+="Stop"
          
      return decision
        # import the opencv library
import cv2
from roboflow import Roboflow

pathu="/home/pi/final_glass/config.txt"
def obst(param):
    list_key=["OXvzw6as00ve7iIpRs5n", "rf_0edelnfoYyUCh9G3uiwerSFiArt2", "rf_z5xKWAIKfRb4aTEEUGmf41OzkUq1"]
    rf = Roboflow(api_key=list_key[0])
    project = rf.workspace().project("obstacle-avoidance-robot")
    model = project.version(1).model
    # define a video capture object
    vid = cv2.VideoCapture(2)
      
    while(True):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        r=""
        with open(pathu, "r") as f:
            r=f.read()
        print("read: ", r)
                
        if r=="1":
            break
        p="iom.jpg"
        # Display the resulting frame
        e=frame.shape
        w=e[1]
        h=e[0]
        xa=int(w/5)
        ya= 200
        xb=int(4*w/5)
        yb=int(h-30)
        print(h, w, xa, xb)
        cv2.rectangle(frame,(xa, ya) , (xb, yb), (255, 0, 0), 2)
        #cv2.rectangle
        cv2.imwrite(p, frame)
        try:
            #print(model.predict(p, confidence=40, overlap=30).json())
            detections=model.predict(p, confidence=40, overlap=30)#["predictions"][0]#.json())
            print(detections.json())
            
            for bounding_box in detections:
                x1 = bounding_box['x'] - bounding_box['width'] / 2
                x2 = bounding_box['x'] + bounding_box['width'] / 2
                y1 = bounding_box['y'] - bounding_box['height'] / 2
                y2 = bounding_box['y'] + bounding_box['height'] / 2
                print("Classe: ", bounding_box['class'])
                box = (x1, x2, y1, y2)
                print("Boss: ", box)
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
                decision=obstacle((int(x1), int(y1), int(x2), int(y2)), (xa, ya, xb, yb))
                cv2.putText(frame, decision, (int(h/2), int(w/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                talk(decision)
        except:
            rf = Roboflow(api_key=list_key[list_key.index(list_key[0])+1])
            project = rf.workspace().project("obstacle-avoidance-robot")
            model = project.version(1).model
        cv2.imshow('frame', frame)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
      
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    
while(True):
    r=""
    with open(pathu, "r") as f:
            r=f.read()
    print("read: ", r)
    if r=="0":
        obst(2)
    else:
        print("Stop")