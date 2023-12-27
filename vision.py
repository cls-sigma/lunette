import requests
import cv2
import os
from age_gender import age_gender, train
import json
import io
from PIL import Image
from io import BytesIO

import numpy as np
# Localize objects in image
from googletrans import Translator
trans = Translator()

from google.cloud import vision
subscription_key ="145af05003a24b0386b05fc7c5485387" # "b9230eaa6f4845d39fee128a91ed992d" #f7890188eca646409d8ec1f8d341ea64"
face_api_url = "https://visionplusface.cognitiveservices.azure.com/"
# Add your Computer Vision key and endpoint to your environment variables.
endpoint ="https://visionplusglass.cognitiveservices.azure.com/" #https://visionplusface.cognitiveservices.azure.com/" #os.environ['COMPUTER_VISION_ENDPOINT']

analyze_url = endpoint + "vision/v3.1/analyze"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='/home/pi/final_glass/key.json'

from google.cloud import vision
client = vision.ImageAnnotatorClient()
# Set image_url to the URL of an image that you want to analyze.
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/" + \
    "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"

def analyse(img=None, path=None):
    #params=
    param='Categories,Description,Color'
    param=param.replace(" ", "")
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream' }
    params = {'visualFeatures': param}#'Categories,Description,Color'}
    #data = {'url': image_url}
    
    data=''
    #content = ""
    if path:
        with open(path, "rb") as f:
            data = f.read()
    else:
        p = "jklvv.jpg"
        im1 = img.copy()
        cv2.imwrite(p, im1)
        with open(p, "rb") as f:
            data = f.read()
    response = requests.post(analyze_url, headers=headers,
                             params=params, data=data)
    #response.raise_for_status()

    # The 'analysis' object contains various fields that describe the image. The most
    # relevant caption for the image is obtained from the 'description' property.
    t=""
    analysis = response.json()
    resp=json.dumps(response.json())
    print(resp)
    if "Description" in param:
        t+=analysis["description"]["captions"][0]["text"]+" \n"
    if "Categories" in param:
        t+=" categories: "+ analysis["categories"][0]["name"]+" \n"
    if "Color" in param:
        print("couleur")
        t+=" Colors: dominant Color Foreground: "+ analysis["color"]["dominantColorForeground"]+ " "
        t+="dominant Color Background: "+analysis["color"]["dominantColorBackground"]+" \n"
        t+="dominant Colors: "+ analysis["color"]["dominantColors"][0]+ "\n"
    
        
    #image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    #print()
    t=trans.translate(t, dest="fr").text
    print(t)
    return t

def objects(content=None, param=None, path=None):
    #param=param.replace(" ", "")
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream' }
    params = {'visualFeatures': "Description"}#'Categories,Description,Color'}
    #data = {'url': image_url}
    
    data=''
    if path:
        with open(path, "rb") as f:
            data=f.read()
    else:
        path='/home/pi/final_glass/zz.png'
        #if path:
        with open(path, "wb") as f:
                f.write(content)
        with open(path, "rb") as f:
            data=f.read()
    response = requests.post(analyze_url, headers=headers,
                             params=params, data=data)
    response.raise_for_status()

    # The 'analysis' object contains various fields that describe the image. The most
    # relevant caption for the image is obtained from the 'description' property.
    t=""
    analysis = response.json()
    resp=json.dumps(response.json())
    print(resp)
    try:
        t+="Je vois: "+ trans.translate(analysis["description"]["captions"][0]["text"],dest="fr").text+" \n"
    except:
        t+="Je vois: "+ ", ".join(analysis["description"]["tags"])+" \n"
        
    print(t)
   
    return t

def read(path):
    
    analyze_url=endpoint + "/vision/v3.1/read/analyze"
    #param=param.replace(" ", "")
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
               'Content-Type': 'application/octet-stream' }
    params = {'visualFeatures': "Read"}#'Categories,Description,Color'}
    #data = {'url': image_url}
    
    data=''
    with open(path, "rb") as f:
        data=f.read()
    
    response = requests.post(analyze_url, headers=headers, data=data)
                            # params=params, data=data)
    response.raise_for_status()
    operation_url = response.headers["Operation-Location"]
    print(operation_url)
    # The recognized text isn't immediately available, so poll to wait for completion.
    analysis = {}
    t=""
    while (True):
        response_final = requests.get(
            response.headers["Operation-Location"], headers=headers)
        analysis = response_final.json()
        t+=""
    return t
        #print(json.dumps(analysis, indent=4))


#analyse(path="/home/pi/final_glass/sitsope.jpg")#, "Color,Description, Objects")



def ocr1(path=None, content=None):

    """Detects text in the file."""
    pat='jkj.jpg'
    
    if path:
        with open(path, "rb") as f:
            content=f.read()
    else:
        #data=BytesIO(content)
        cv2.imwrite(pat, content)
        with io.open(pat, 'rb') as image_file:
           content = image_file.read()

    

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    t=""
    #print(texts.keys())
    for text in texts:
        t=f'\n"{text.description}"'

        vertices = ([f'({vertex.x},{vertex.y})'
                    for vertex in text.bounding_poly.vertices])
        break
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    '''for text in texts:
        print(f'\n"{text.description}"')

        vertices = ([f'({vertex.x},{vertex.y})'
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))'''
    if t:
        t = "Le texte: \n :"+trans.translate(t.lower(), dest='fr').text
        
        print(t)
        return t
    else:
        return "pas de texte "
    

     
#ocr("/home/pi/Downloads/ocrfr.png")

#vision()
    
 #https://github.com/charlielito/vision-sentiment-analysis-googleapiimport cv2
# age and gender: https://www.geeksforgeeks.org/age-detection-using-deep-learning-in-opencv/
"""https://www.geeksforgeeks.org/age-detection-using-deep-learning-in-opencv/
https://www.thepythoncode.com/article/gender-detection-using-opencv-in-python
age: https://www.thepythoncode.com/article/predict-age-using-opencv
"""
#hand: https://www.geeksforgeeks.org/face-and-hand-landmarks-detection-using-python-mediapipe-opencv/



    

'''
'''
############## Spanish version #################
#emo = ['Bravo', 'Sorprendido','Triste', 'Feliz']
#string = 'Sin emocion'

#from google.oauth2 import service_account
#credentials = service_account.Credentials.from_service_account_file('VisionApp-9cb3e521631b.json')

# Instantiates a client





def localize_objects(img=None, path=None):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    content=""
    if path:
        with open(path, "rb") as f:
            content = f.read()
    else:
        p = "jklvv.jpg"
        im1 = img.copy()
        cv2.imwrite(p, im1)
        with open(p, "rb") as f:
            content = f.read()
    image = vision.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations
    t = ''
    if len(objects):
        t += f"{len(objects)} differents elements find \n"
        print('Normalized bounding polygon vertices: ')
        for object_ in objects:
            t += f" a {object_.name} , \n"
            print(t)
            #print(f'\n{object_.name} (confidence: {object_.score})')
            # for vertex in object_.bounding_poly.normalized_vertices:
            # print(f' - ({vertex.x}, {vertex.y})')
            # print('')
    else:
        t += "I don't find objects in front of you, if is anormal, please try again"

    t = trans.translate(t, dest='fr').text

    return t
    # print(f'Number of objects found: {len(objects)}')



#path = '/content/yu.jfif'
#localize_objects(path="/home/pi/final_glass/zz.png")
#print(localize_objects(path="/home/pi/final_glass/sitsope.jpg")) 

#Emotions
emo = ['Angry', 'Surprised','Sad', 'Happy', "Under Exposed", "Blurred", "Headwear"]
likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                    'LIKELY', 'VERY_LIKELY')

def sentiment(img=None, path=None):
    content = ""
    if path:
        with open(path, "rb") as f:
            content = f.read()
    else:
        
        im1 = img#.copy()
        p = "jklvv.jpg"
        cv2.imwrite(p, im1)
        with open(p, "rb") as f:
            content = f.read()
    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations
    print('Number of faces: ', len(faces))
    for face in faces:
        x = face.bounding_poly.vertices[0].x
        y = face.bounding_poly.vertices[0].y
        x2 = face.bounding_poly.vertices[2].x
        y2 = face.bounding_poly.vertices[2].y
        #cv2.rectangle(img, (x, y), (x2, y2), (0, 255, 0), 2)

        sentiment = [likelihood_name[face.anger_likelihood],
                     likelihood_name[face.surprise_likelihood],
                     likelihood_name[face.sorrow_likelihood],
                     likelihood_name[face.joy_likelihood],
                     likelihood_name[face.under_exposed_likelihood],
                     likelihood_name[face.blurred_likelihood],
                     likelihood_name[face.headwear_likelihood]]

        for item, item2 in zip(emo, sentiment):
            #print(item, ": ", item2)
            print("")

        string = 'No sentiment'

        if not (all(item == 'VERY_UNLIKELY' for item in sentiment)):
            if any(item == 'VERY_LIKELY' for item in sentiment):
                state = sentiment.index('VERY_LIKELY')
                # the order of enum type Likelihood is:
                # 'LIKELY', 'POSSIBLE', 'UNKNOWN', 'UNLIKELY', 'VERY_LIKELY', 'VERY_UNLIKELY'
                # it makes sense to do argmin if VERY_LIKELY is not present, one would espect that VERY_LIKELY
                # would be the first in the order, but that's not the case, so this special case must be added
            else:
                state = np.argmin(sentiment)
            

            string = emo[state]
            print(string)
            string = trans.translate(string, dest='fr').text
            print("Voila string: ", string)
        return string
    
 
'''import cv2
compressRate=1
video_capture = cv2.VideoCapture(0)
c=0

while(True):
    ret, img = video_capture.read()
    #img = cv2.resize(img, (0,0), fx=compressRate, fy=compressRate )
    #cv2.imshow('frame', img)
    #sentiment(img)
    #cv2.putText(img,string, (int(640/2),int(480/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
    
    c+=1
    if cv2.waitKey(1) & ord("q")==0xFF:
        string=ocr1(content=img)
        print("Voila string: ", string)
        break
    if c==10:
        sentiment=localize_objects(img=img)
        print("Voila string: ", sentiment)
        break
    cv2.imshow("Video", img)
        
    #cv2.waitKey(1)

video_capture.release()# When everything is done, release the capture
cv2.destroyAllWindows()'''
   
