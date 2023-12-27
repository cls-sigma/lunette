
'''import cv2
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")'''
import time

'''
from pydub import AudioSegment
from pydub.playback import play'''
from google.cloud import vision

def correct(test):
    test=test.lower()

def talk(test):
    print(test)
    pass
def ocr(content):
    pass
def audio(path3):
    pass#play(AudioSegment.from_file(path3))

import cv2

import os, io
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'key.json'
from google.cloud import vision
import argparse
from enum import Enum
import io
client = vision.ImageAnnotatorClient()
import argparse
from enum import Enum
import io

from google.cloud import vision
from PIL import Image, ImageDraw
import json
# Document API
class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5

def draw_boxes(image, bounds, color):
    """Draw a border around the image using the hints in the vector list."""
    draw = ImageDraw.Draw(image)

    for bound in bounds:
        draw.polygon(
            [
                bound.vertices[0].x,
                bound.vertices[0].y,
                bound.vertices[1].x,
                bound.vertices[1].y,
                bound.vertices[2].x,
                bound.vertices[2].y,
                bound.vertices[3].x,
                bound.vertices[3].y,
            ],
            None,
            color,
        )
    return image

def get_document_bounds(image_file, feature):
    """Returns document bounds given an image."""
    client = vision.ImageAnnotatorClient()

    bounds = []

    with io.open(image_file, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    #print(response)
    document = response.full_text_annotation
    test=document.text
    t=" "
    t=test.lower()

    print("text ", t)
    #text=document.
    '''with open("yui.txt", "w") as f:
        f.write(f"{response}")'''
    #print("Document: ", document)
    # Collect specified feature bounds by enumerating all document features
    i=0
    for  page in document.pages:
        i+=1
        #print("Page: ", i)
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols:
                        if feature == FeatureType.SYMBOL:
                            bounds.append(symbol.bounding_box)

                    if feature == FeatureType.WORD:
                        bounds.append(word.bounding_box)

                if feature == FeatureType.PARA:
                    bounds.append(paragraph.bounding_box)

            if feature == FeatureType.BLOCK:
                bounds.append(block.bounding_box)

    # The list `bounds` contains the coordinates of the bounding boxes.
    return bounds, t

def render_doc_text(filein=None, img=None):
    if filein:
        pass
    else:
        filein = "jklvv.jpg"
        im1 = img.copy()
        cv2.imwrite(filein, im1)

    #image = Image.open(filein)
    u="no"
    bounds, text = get_document_bounds(filein, FeatureType.BLOCK)

    x=[]
    y=[]
    if bounds:
        for bound in bounds:
                x+=[
                        bound.vertices[0].x,
                        bound.vertices[1].x,
                        bound.vertices[2].x,
                        bound.vertices[3].x,
                 ]
                y+=[

                        bound.vertices[0].y,
                        bound.vertices[1].y,
                        bound.vertices[2].y,
                        bound.vertices[3].y,
                ]
        print(x,y )
        print(int(max(x)-int(min(x))))
        print(int(max(y) - int(min(y))))
        start_point = (int(min(x)), int(min(y)))
        end_point = (int(max(x)),int(max(y)))
        u=[int(min(x)), int(min(y)),int(max(x)),int(max(y))]

        print(start_point, end_point)

    return u, text
    """print("Bound1: ", bounds)
    draw_boxes(image, bounds, "red")
    for vertex in bounds.bounding_poly.normalized_vertices:
        x = vertex.x * w
        y = vertex.y * h
        l.append((x, y))
    print(l)
    # t += f" a {object_.name} , \n"
    '''print(f'\n{object_.name} (confidence: {object_.score})')
    for vertex in object_.bounding_poly.normalized_vertices:
        print(f' - ({vertex.x}, {vertex.y})')'''
    # print(w, h)  # print('')

    start_point = (int(l[0][0]), int(l[0][1]))
    end_point = (int(l[1][0]), int(l[2][1]))
    u = [int(l[0][0]), int(l[0][1]), int(l[1][0]), int(l[2][1])]
    start_point=
    end_point=
    image = cv2.imread(filein)
    image = cv2.rectangle(image, start_point, end_point, (255, 0, 0), 2)
    # Displaying the image
    # cv2.imwrite("window_name.jpeg", image)"""
    '''bounds = get_document_bounds(filein, FeatureType.BLOCK)
    print("Bound2: ", bounds)
    draw_boxes(image, bounds, "blue")
    bounds = get_document_bounds(filein, FeatureType.PARA)
    print("Bound3: ", bounds)
    draw_boxes(image, bounds, "red")
    bounds = get_document_bounds(filein, FeatureType.WORD)
    print("Bound4: ", bounds)
    draw_boxes(image, bounds, "yellow")
'''
    '''if fileout != 0:
        image.save(fileout)
    else:
        image.show()'''

"""if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("detect_file", help="The image for text detection.")
    parser.add_argument("-out_file", help="Optional output file", default=0)
    args = parser.parse_args()

    render_doc_text(args.detect_file, args.out_file)"""
def localize(img=None, path=None):
        content = ""
        u = "no"
        w, h, t = 0, 0, 0
        if path:
            h, w, t = cv2.imread(path).shape
            with open(path, "rb") as f:

                content = f.read()
        else:
            p = "jklvv.jpg"
            im1 = img.copy()
            cv2.imwrite(p, im1)
            h, w, t = cv2.imread(path).shape
            with open(p, "rb") as f:
                content = f.read()

        image = vision.Image(content=content)

        objects = client.object_localization(image=image).localized_object_annotations
        t = ''

        if len(objects):
            t += f"Number of objects i found:  {len(objects)} \n"
            print('Normalized bounding polygon vertices: ')
            for object_ in objects:
                print("nom: ",object_.name)
                if object_.name.lower() in ['book', "notebook","bookseries"]:
                    i = 0
                    l = []
                    for vertex in object_.bounding_poly.normalized_vertices:
                        x = vertex.x * w
                        y = vertex.y * h
                        l.append((x, y))
                    print(l)
                    # t += f" a {object_.name} , \n"
                    '''print(f'\n{object_.name} (confidence: {object_.score})')
                    for vertex in object_.bounding_poly.normalized_vertices:
                        print(f' - ({vertex.x}, {vertex.y})')'''
                    #print(w, h)  # print('')

                    start_point = (int(l[0][0]), int(l[0][1]))
                    end_point = (int(l[1][0]), int(l[2][1]))
                    u=[int(l[0][0]), int(l[0][1]),int(l[1][0]), int(l[2][1]) ]
                    #image = cv2.imread(path)
                    #image = cv2.rectangle(image, start_point, end_point, (255, 0, 0), 2)
                    # Displaying the image
                    #cv2.imwrite("window_name.jpeg", image)
                    #cv2.waitKey(1)
                    #time.sleep(3)
        else:
            pass



        return u
        # print(f'Number of objects found: {len(objects)}')

#localize(path="images.jpg")

#
#render_doc_text(filein="images.jpeg")#, fileout="ime.jpeg")
    # print(f'Number of objects found: {len(objects)}')
def ocr2():

    vid = cv2.VideoCapture(0)
    text = ''
    compt=0
    while (True):

        ret, frame = vid.read()
        w_, h_, r = frame.shape
        a, b = (int(h_ / 10), 0), (int(9*h_/10), w_)
        print(a, b, w_, h_)
        cv2.rectangle(frame, a, b, (0, 255, 255), 2)
        # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        '''if bre == 1:
            return 0'''
        result=render_doc_text(img=frame)
        try:
            result, text = result
        except:
            pass
        percent=0.40
        if result!="no":
            cv2.rectangle(frame, (result[0],result[1]), (result[2],result[3]), (255, 0, 0), 2)
            decision1=""
            decision2=""
            x, y, z, t=result
            n=(w_-(z-x))/2
            seuil1 = percent *n
            if (x-n)>seuil1:
                talk('Deplacez un peu vers la Gauche')
            elif (x-n)<-seuil1:
                talk('Deplacez un peu vers la Droite')
            elif -seuil1<(x-n)<seuil1:
                talk("Position Horizontale acceptable")
                decision1="acceptable"
                m = (h_ - abs(y - t)) / 2
                seuil2 = percent * m
                if (t - m) > seuil2:
                    talk('Deplacez un peu vers la Haut')
                elif (t- m) < -seuil2:
                    talk('Deplacez un peu vers la bas')
                elif -seuil2 < (t - m) < seuil2:
                    talk("Position verticale acceptable, prise de photo")
                    decision2= 'acceptable'
                    audio("/home/pi/final_glass/camera.mp3")
                    if text:
                        talk("Le texte dans votre image est: ")
                        talk(correct(text.lower()))
                    else:
                        res = ocr(content=frame)
                        if res:
                            talk("Le texte dans votre image est: ")
                            talk(correct(res))
                        else:
                            talk("Je nai pas pu lire votre texte. Vous pouvez réesayer")

                    """
                    """
                    break


        else:
            pass
        compt += 1
        cv2.imshow('yur', frame)
        if compt == 30:

                talk("temps expiré pour le guide, j'essayerai de vous"
                     " lire votre document mais la précision ne sera peut-etre pas bonne")
                audio("/home/pi/final_glass/cam.wav")
                res = ocr(content=frame)
                if res:
                    talk("Le texte dans votre image est: ")
                    talk(correct(res))
                    vid.release()
                    # Destroy all the windows
                    cv2.destroyAllWindows()
                    return 0

                else:
                    talk("Je n'ai pas pu lire votre document. Désolé")
                    vid.release()
                    # Destroy all the windows
                    cv2.destroyAllWindows()
                    return 0
                #break

    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()






ocr2()


