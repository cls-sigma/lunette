
import requests
#from talk import talk
url = "https://api.ultramsg.com/instance50674/messages/chat"
def wh(num, mesa):

    payload = f"token=pu9azo9d1cdjbehd&to=%2B228{num}&body={mesa}"
    payload = payload.encode('utf8').decode('iso-8859-1')
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text.split())
    if dict(response.text)['sent']=='true':
        print('send successfully')
        #talk("message envoyé avec succes")
    return
wh(num=96698114,mesa= "Bonjour vision plus")