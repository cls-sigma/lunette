from talk import talk
'''def talk(mes):
    print(mes)'''
import requests
import cv2


def test_connection(url):
    response=''
    try:
        headers={}
        r = requests.post(url, headers=headers, data=post_data)
        response = r.text
    except HTTPError as e:
        response = e.response.text
    return response



#Lien du github: https://github.com/SkyBiometry/python-face-client/tree/master
#lien de l'API: https://manage.skybiometry.com/#/management/subscriptions
#Creer d'autres compte pour changer de clé d'API en cas d'epuisement de l'essai gratuit
from face_client.face_client import FaceClient

api_key='ti9ubjrgmn3kpr8ldrc805ugd5'
api_secret="j1k96l3b4tv3cs009l1jdb1lkb"
client = FaceClient(api_key,api_secret)
'''response = client.faces_detect('http://farm1.static.flickr.com/43/104506247_c748f20b83.jpg,http://farm1.static.flickr.com/67/200126290_2798330e61.jpg')

tids = [photo['tags'][0]['tid'] for photo in response['photos']]
print(tids)
client.tags_save(tids = ',' . join(tids), uid = 'guido@visionplusadmin', label = 'Guido Van Rossum')
client.faces_train('guido@visionplusadmin')
print(client.tags_get('guido@visionplusadmin'))
#recog=client.faces_recognize('gdo', 'http://farm1.static.flickr.com/41/104498903_bad315cee0.jpg', namespace = 'visionplusadmin')
#print(recog)'''


from googletrans import Translator
trans=Translator()

def train(image_url_list_str, name):
    response = client.faces_detect(image_url_list_str)
    tids = [photo['tags'][0]['tid'] for photo in response['photos']]
    print(tids)
    client.tags_save(tids=','.join(tids), uid=f'{name}@visionplusadmin', label='name')
    client.faces_train(f'{name}@visionplusadmin')
    print(client.tags_get(f'{name}@visionplusadmin'))
    return



def age_gender(content=None):
    paty="/home/pi/final_glass/im1.jpg"#'jkj.png'
    #from io import BytesIO
    cv2.imwrite(paty, content)
    #buff=open(paty, "rb")
    recog=client.faces_recognize(uids='all', file=paty, namespace = 'visionplusadmin')

    #print(recog['status'], recog['photos'][0]['tags'][0]['uids'])
    try:
        att=recog['status'], recog['photos'][0]['tags'][0]['attributes']
        print(type(att))
    except:
        att="Pas de personne devant vous"
        return att
    t=""
    it=att[1]
    emotions=" "
    nb=0
    for i in it.items():
        try:
          if i[0]=="age_est":
              t+="age: "+i[1]['value']+"\n "
          elif i[0]=="gender":
              t+="genre: "+i[1]['value']+"\n "
          elif i[0]=="face":
              if i[1]['value']=="true":
                  nb+=1
          elif i[1]['value']=="true" :
              emotions +=f"with {i[0]} \n"
          elif i[1]['value'] == "false":
              emotions +=f"without {i[0]}\n "
          else:
              emotions+= f"{i[0]}: {i[1]['value']} \n"

        except:
            pass
    if nb:
            nb=f"Je vois {nb} personne "
    else:
            nb=""
    t= f"{nb},les Caractéristiques :{t}\n {trans.translate(emotions, dest='fr').text} "
    print(t)
    return t

#age_gender()


def facial(content):
    att=""
    pat='jkj.jpg'
    
    cv2.imwrite(pat, content)
    
    recog=client.faces_recognize('all', file=pat, namespace = 'visionplusadmin')


    #recog = client.faces_recognize('guido', file=path, namespace='visionplusadmin')
    #print(recog)
    response=recog['photos'][0]['tags']
    #print("response: ,", response)

    if len(response)>0:
        response=response[0]['uids']
        print("response: ,", response)
        try:
            response=response[0]['confidence']
            if int(response)>=30:
                att="admin"
            else:
                att="non"
        except:
            att="non"
    else:
        att="non"
    print("Réponse finale, ", att)
    return att
#age_gender(url='http://farm1.static.flickr.com/41/104498903_bad315cee0.jpg')

def face_init():
    talk("début de la reconnaissance faciale")
    vid = cv2.VideoCapture(0)
    
    text = ''
    compt=0
    en=0
    while (True):

        ret, frame = vid.read()
        frame = cv2.rotate(frame, cv2.ROTATE_180)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        '''if bre == 1:
            return 0'''
        result=facial(content=frame)
        if result=="admin":
            #talk("Bonjour administrateur")
            en=1
           
        cv2.imshow('yur', frame)
        if en==1:
            print("Bonjour administrateur")
            talk('Bonjour administrateur')
            vid.release()
            cv2.destroyAllWindows()
            import mic
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

#face_init()