'''
import yaml

from ultralytics import YOLO
from ultralytics import YOLO

from pydub import AudioSegment
from pydub.playback import play


def audio(path3):
    play(AudioSegment.from_file(path3))


# Load a model
model = YOLO("yolov8n.pt")  # load an official model


# print(results)
# import the opencv library
def ocr2():
    import cv2
    i = 0
    compt = 0
    # define a video capture object
    names = ''
    # file_name = "../usr/local/lib/python3.8/dist-packages/ultralytics/yolo/data/datasets/coco8.yaml"
    with open("coco.names", "r") as stream:
        names = stream.read().splitlines()
    # print(names)
    vid = cv2.VideoCapture(0)

    import os
    import shutil
    try:
        shutil.rmtree('runs')
        os.mkdir("runs/")
        print("ok")
    except:
        pass
    bre = 0
    while (True):

        ret, frame = vid.read()
        w_, h_, r = frame.shape
        a, b = (int(h_ / 10), 0), (int(9*h_/10), w_)
        print(a, b, w_, h_)
        cv2.rectangle(frame, a, b, (0, 255, 255), 2)
        # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if bre == 1:
            return 0
        model.predict(frame, save_txt=True, )
        ph = "runs/detect/predict/labels/image0.txt"
        if os.path.exists(ph):
            lis = open(ph, "r").readlines()
            if lis:
                print(lis)
                for l in lis:
                    ind = int(l.split()[0])
                    print(ind, names[ind])
                    # if names[ind].lower():
                    li = l.split()
                    xc, yc, nw, nh = float(li[1]), float(li[2]), float(li[3]), float(li[4])
                    h, w = frame.shape[0], frame.shape[1]
                    xc *= w
                    yc *= h
                    nw *= w
                    nh *= h
                    x = int(xc - nw / 2)
                    y = int(yc - nh / 2)
                    h = nh
                    w = nw
                    cv2.rectangle(frame, (x, y), (int(xc + nw / 2), int(yc + nh / 2)), (0, 255, 0), 2)
                    cv2.putText(frame, f'Dis: {round(h*2.4, 2)} cm', (x + 5, y + 13), cv2.FONT_HERSHEY_COMPLEX, 0.48, (255, 255, 0), 2)

                    top_left = (int(xc - nw / 2), int(yc - nh / 2))
                    bottom_right = (int(xc + nw / 2), int(yc + nh / 2))
                    long=b[0]-a[0]
                    if a[0]<x<b[0] or a[0]<x+h<b[0]:
                        cv2.putText(frame, f' {names[ind]}', (x + 5, y + 23), cv2.FONT_HERSHEY_COMPLEX, 0.48, (0, 255, 0), 2)

                        if x-(w_-(x+w))>100:
                            if w>100:# & dist<1000:
                                cv2.putText(frame, 'Gauche', (x + 5, y + 53), cv2.FONT_HERSHEY_COMPLEX, 0.48,
                                        (255, 0, 0), 2)
                        elif x-(w_-(x+w))<100:
                            cv2.putText(frame, 'Droite', (x + 5, y + 53), cv2.FONT_HERSHEY_COMPLEX, 0.48,
                                        (255, 0, 0), 2)
                        else:
                            cv2.putText(frame, 'Stop', (x + 5, y + 53), cv2.FONT_HERSHEY_COMPLEX, 0.48,
                                        (255, 0, 0), 2)
                    elif (w>(b[0]-a[0])):
                        cv2.putText(frame, 'Obstacle imminent, a gauche', (x + 5, y + 53), cv2.FONT_HERSHEY_COMPLEX, 0.48,
                                        (255, 0, 0), 2)
                    else:
                        pass

            else:
                pass#cv2.imshow('frame', frame)




            cv2.imshow('frame', frame)
            os.remove(ph)

        """ else:
            print("N'existe pas")
        compt += 1
        if compt == 30:

            talk("temps expiré pour le guide, j'essayerai de vous"
                 " lire votre document mais la précision ne sera peut-etre pas bonne")
            audio("/home/pi/final_glass/cam.wav")
            res = detect_document(content=frame)
            if res:
                talk("Le texte dans votre image est: ")
                talk(correct(res))
                vid.release()
                # Destroy all the windows
                cv2.destroyAllWindows()
                return 0

            else:
                talk("Je n'ai pas pu lire votre document. Désolé")
                return 0
            break"""
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
'''

import requests

url = "https://api.ultramsg.com/instance50674/messages/chat"
def wh(num, mesa):

    payload = f"token=pu9azo9d1cdjbehd&to=%2B228{num}&body={mesa}"
    payload = payload.encode('utf8').decode('iso-8859-1')
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)

    if response.text[0]=='true':
        print('send successfully')
    return
#wh(num=96698114, mesa="Envoi de message whatsapp reussi")

def test_connection(url):
    response=''
    try:
        headers={}
        r = requests.post(url, headers=headers, data=post_data)
        response = r.text
    except HTTPError as e:
        response = e.response.text
    return response


'''import http.client
conn = http.client.HTTPSConnection("api.ultramsg.com")
payload = "token=pu9azo9d1cdjbehd&to=%2B22896698114&audio=https://file-example.s3-accelerate.amazonaws.com/voice/oog_example.ogg&referenceId="
headers = { 'content-type': "application/x-www-form-urlencoded" }
conn.request("POST", "/instance50674/messages/voice", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))'''
#Lien du github: https://github.com/SkyBiometry/python-face-client/tree/master
#lien de l'API: https://manage.skybiometry.com/#/management/subscriptions
#Creer d'autres compte pour changer de clé d'API en cas d'epuisement de l'essai gratuit
from face_client.face_client import FaceClient
api_key='cl6j92k6jn5cvqhdiv7nk76gje'
api_secret="diqr491hrkaq6gm3tfcce2t26p"
client = FaceClient(api_key,api_secret)
def train(image_url_list_str):
    response = client.faces_detect(image_url_list_str)
    tids = [photo['tags'][0]['tid'] for photo in response['photos']]
    print(tids)
    client.tags_save(tids=','.join(tids), uid='guido@visionadmin', label='Guido Van Rossum')
    client.faces_train('guido@visionadmin')
    print(client.tags_get('guido@visionadmin'))
    return
'''response = client.faces_detect('http://farm1.static.flickr.com/43/104506247_c748f20b83.jpg,http://farm1.static.flickr.com/67/200126290_2798330e61.jpg')


#recog=client.faces_recognize('gdo', 'http://farm1.static.flickr.com/41/104498903_bad315cee0.jpg', namespace = 'visionadmin')
#print(recog)'''

from face_client.face_client import FaceClient
api_key='cl6j92k6jn5cvqhdiv7nk76gje'
api_secret="diqr491hrkaq6gm3tfcce2t26p"
client = FaceClient(api_key,api_secret)

from googletrans import Translator
trans=Translator()
def age_gender(url):
    recog=client.faces_recognize('all', url, namespace = 'visionadmin')

    #print(recog['status'], recog['photos'][0]['tags'][0]['uids'])
    att=recog['status'], recog['photos'][0]['tags'][0]['attributes']
    print(type(att))
    t=""
    it=att[1]
    emotions=" "
    nb=0
    for i in it.items():
        try:
          if i[0]=="age_est":
              t+="age: "+i[1]['value']+", "
          elif i[0]=="gender":
              t+="genre: "+i[1]['value']+", "
          elif i[0]=="face":
              if i[1]['value']=="true":
                  nb+=1
          elif i[1]['value']=="true" :
              emotions +=f"with {i[0]}, "
          elif i[1]['value'] == "false":
              emotions +=f"without {i[0]}, "
          else:
              emotions+= f"{i[0]}: {i[1]['value']}, "

        except:
            pass
    if nb:
            nb=f"Je vois {nb} personnes "
    else:
            nb=""
    t= f"{nb},Caractéristiques :{t}; {trans.translate(emotions, dest='fr').text} "
    print(t)
    return t
#age_gender(url='http://farm1.static.flickr.com/41/104498903_bad315cee0.jpg')

'''print(['gender']['value'])
print(recog['status'], recog['photos'][0]['tags'][0]['attributes']['neutral_mood']['value'])
print(recog['status'], recog['photos'][0]['tags'][0]['attributes']['anger']['value'])
print(recog['status'], recog['photos'][0]['tags'][0]['attributes']['disgust']['value'])
'fear' '''
