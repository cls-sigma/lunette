import requests
#from ..talk import talk
def talk(test):
    print(test)
url = "https://api.ultramsg.com/instance50674/messages/chat"
def wh(num, mesa):

    payload = f"token=pu9azo9d1cdjbehd&to=%2B228{num}&body={mesa}"
    payload = payload.encode('utf8').decode('iso-8859-1')
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)

    if response.text[0]=='true':
        print('send successfully')
        talk("message envoyé avec succes")
    return


def test_connection(url):
    response=''
    try:
        headers={}
        r = requests.post(url, headers=headers, data=post_data)
        response = r.text
    except HTTPError as e:
        response = e.response.text
    return response


from face_client.face_client import FaceClient


api_key='ti9ubjrgmn3kpr8ldrc805ugd5'
api_secret="j1k96l3b4tv3cs009l1jdb1lkb"
client = FaceClient(api_key,api_secret)
def train(image_url_list_str):
    response = client.faces_detect(image_url_list_str)
    #

    tids = []
    response = response['photos']
    i=0
    for photo in response:
        try:
             tids.append(photo['tags'][0]['tid'] )
        except:
            print(i)
        i+=1
    print(tids)
    client.tags_save(tids=','.join(tids), uid='administrateur@visionplusadmin', label='administrateur')
    client.faces_train('administrateur@visionplusadmin')
    print(client.tags_get('administrateur@visionplusadmin'))
    return


li=[
    "http://raw.githubusercontent.com/kokou-sekpona/voicelab/main/2.jpg",
    "http://raw.githubusercontent.com/kokou-sekpona/voicelab/main/IMG_20230607_105449.jpg",
    "http://raw.githubusercontent.com/kokou-sekpona/voicelab/main/p.jpg",
    "http://raw.githubusercontent.com/kokou-sekpona/voicelab/main/IMG_20230622_005410.jpg",
    "http://raw.githubusercontent.com/kokou-sekpona/voicelab/main/im103.jpg",
    #"http://raw.githubusercontent.com/kokou-sekpona/voicelab/main/IMG_20230612_131827.jpg?token=GHSAT0AAAAAACCPBPQXPNFCKZV6EVGW4RL2ZETUBOQ0",

    "http://raw.githubusercontent.com/kokou-sekpona/voicelab/main/im122.jpg",
    "http://raw.githubusercontent.com/kokou-sekpona/voicelab/main/im60.jpg",
    #"http://raw.githubusercontent.com/kokou-sekpona/voicelab/main/im60.jpg",
    "http://raw.githubusercontent.com/kokou-sekpona/voicelab/main/IMG_20230612_181013.jpg"]


client = FaceClient(api_key,api_secret)

def age_gender(file):

    recog=client.faces_recognize('all', file=file, namespace = 'visionplusadmin')
    print(recog)

    try:
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
        t= f"{nb},Caractéristiques :{t}; {emotions}" #{trans.translate(emotions, dest='fr').text} "
        print(t)
        return t
    except:
        t="rien n'est detecté"
        return t
age_gender(file='/home/pi/final_glass/im1.jpg')

def facial(path):
    att=""
    recog = client.faces_recognize('all', file=path, namespace='visionplusadmin')
    #print(recog)
    response=recog['photos'][0]['tags']
    #print("response: ,", response)
    print(len(response))
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
