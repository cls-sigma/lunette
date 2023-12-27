
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
from python_face_client_master.face_client.face_client import FaceClient
api_key='cl6j92k6jn5cvqhdiv7nk76gje'
api_secret="diqr491hrkaq6gm3tfcce2t26p"
client = FaceClient(api_key,api_secret)
'''response = client.faces_detect('http://farm1.static.flickr.com/43/104506247_c748f20b83.jpg,http://farm1.static.flickr.com/67/200126290_2798330e61.jpg')

tids = [photo['tags'][0]['tid'] for photo in response['photos']]
print(tids)
client.tags_save(tids = ',' . join(tids), uid = 'guido@visionadmin', label = 'Guido Van Rossum')
client.faces_train('guido@visionadmin')
print(client.tags_get('guido@visionadmin'))
#recog=client.faces_recognize('gdo', 'http://farm1.static.flickr.com/41/104498903_bad315cee0.jpg', namespace = 'visionadmin')
#print(recog)'''

#from .face_client.face_client import FaceClient
api_key='cl6j92k6jn5cvqhdiv7nk76gje'
api_secret="diqr491hrkaq6gm3tfcce2t26p"
client = FaceClient(api_key,api_secret)

from googletrans import Translator
trans=Translator()

def train(image_url_list_str, name):
    response = client.faces_detect(image_url_list_str)
    tids = [photo['tags'][0]['tid'] for photo in response['photos']]
    print(tids)
    client.tags_save(tids=','.join(tids), uid=f'{name}@visionadmin', label='name')
    client.faces_train(f'{name}@visionadmin')
    print(client.tags_get(f'{name}@visionadmin'))
    return

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