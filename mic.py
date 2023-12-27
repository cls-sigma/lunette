
from __future__ import division

mai = 0
message = '' 
ad_mail = ''

import threading

from  datetime import datetime
print(datetime.now())

import google
import os
from googletrans import Translator
import cv2
from google.cloud import speech
from google.cloud import vision


trans=Translator()

import numpy as np

import re
import sys
import time


import pyaudio
from six.moves import queue

#from pydub import AudioSegment
#from pydub.playback import play
from api import final, bible_command
from vision import ocr1
from ocrguid import ocr2
from talk import talk, audio

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='/home/pi/final_glass/key.json'
global val
# talk("Initialisation")

from email.message import EmailMessage
import smtplib
import ssl

#import webbrowser
#import pyautogui
import re

import smtplib
from email.message import EmailMessage
from twilio.rest import Client


print("Import sucessfull")


print(datetime.now())

def vision2():
   
    vid = cv2.VideoCapture(2)
    
    talk("capture dans quelques secondes")
    t = " "
    c = 0
    while (True):
        ret, frame = vid.read()
        frame = cv2.rotate(frame, cv2.ROTATE_180)
        # cv2.imshow('frame', frame)
        if c == 1:
            audio("/home/pi/final_glass/camera.mp3")
            try:
                t +=ocr1(content=frame) + " \n"
            except:
                pass
            
            break
        c += 1
        #time.sleep(1)

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return t
print(vision2())
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    e = to.replace(' ', '')
    e = e + "@gmail.com"
    try:

        msg['to'] = e  # "sitsopekokou@gmail.com"
        user = 'voicetranslator0@gmail.com'
        password = 'rfqzyhocddgmehbe'
        # user = 'username@gmail.com'
        msg['from'] = user
        # password = 'app_password'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)  # <- UPDATED
        server.quit()
        talk(f"Message envoyée à l'addresse {e}")
        print(e)
    except:
        print(e)
        talk('adresse du destinataire invalide')
    audio("/home/pi/final_glass/audio.mp3")


def find_numero(te):
    validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"
    re.match(validate_phone_number_pattern, "+12223334444")  # Returns Match object
    extract_phone_number_pattern = "\\+?[1-9][0-9]{7,14}"
    print(re.findall(extract_phone_number_pattern, te))
    return re.findall(extract_phone_number_pattern, te)  # returns ['+12223334444', '+56667778888']



import requests, json
#

url="https://api.ultramsg.com/instance60735/messages/chat"
def wh(num, mesa):

    payload = f"token=g0yve4xslzvvg9es&to=%2B228{num}&body={mesa}"
   
    payload = payload.encode('utf8').decode('iso-8859-1')
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)
    response=response.json()
    print(response)
    if response['sent']=='true':
        print('send successfully')
        talk("message envoyé avec succes")
    return


def whatsapp(t, number):
    '''m=message
    te=m.split(' ')
    number=te[te.index("numéro")+1]
    number=find_numero(m)[0]
    m=m.replace('numéro', "").replace(number, '')

    t=te[te.index("message")+1:]
    try:
        t=' '.join(t)
    except:
        pass'''
    """for i in m.split(" "):
        number""" 
    print(number, t)
    talk(f"envoi du message au numero {number}")
    #a = threading.Thread(target=wh, args=[number, t])
    #a.start()
    wh(num=number, mesa=t)





account_sid = "ACa4e5b354c97f8936fe43311fc036470b"
auth_token = "ba80ec37c37316481da6a30ac539e38e"
client = Client(account_sid, auth_token)

def messages(text, number):
    # m = test
    # te = m.split(" ")
    # t = te[te.index("message") + 1]
    # number = te[te.index("numéro") + 1]
    if ' ' in number:
        number = number.replace(' ', '')
    u = ""
    for i in number:
        # print(i)
        if i.isnumeric():
            u += f"{i}"
    print(u)

    number = u  # "96698114"
    print(f"+228{number}")
    talk(f"envoi du message au numero {number}")
    try:
        call = client.messages.create(
            body=text,  # t,
            to=f"+228{number}",
            from_="+13613154273"
        )
        

        print(call.sid)
        print("message envoyé")
        talk('message envoyé')
    except:
        talk("le numero est invalid, veuillez ressayer")
    # audio("/home/pi/final_glass/audio.mp3")


def radio(command):
    url="http://vis.media-ice.musicradio.com/Capital"
    if "londre" in command:
        url="http://vis.media-ice.musicradio.com/Capital"
    '''if "bbc" in command:
        url="http://stream.live.vc.bbcmedia.co.uk/bbc_radio_one" '''
    if globals().get('player'):
        instance = globals()['instance']
        player = globals()['player']
    else:
        instance = globals()['instance'] = vlc.Instance("--no-video")
        player = globals()['player'] = instance.media_player_new()    

    
    lr=["arrête-moi", "arrête", "stop"]
    instance = vlc.get_default_instance()
    for j in lr:
        if j in command:
            print("yes")
            print('1')
            player.stop()
            print('2')
            # and possibly garbage collect the player
            del globals()['player']
            del globals()['instance']
            return
    talk("Recherche de la radio. patientez s'il vous plait")
    media = instance.media_new(url)
    media.get_mrl()
    player.set_media(media)

    player.play()
    return
    

from youtube_search import YoutubeSearch
import vlc
import yt_dlp as youtube_dl

def youtube(command):
    
    if globals().get('player3'):
        instance = globals()['instance3']
        player = globals()['player3']
    else:
        instance = globals()['instance3'] = vlc.Instance("--no-video")
        player = globals()['player3'] = instance.media_player_new()
    lr=["arrête-moi", "arrête", "stop"]
    
    for j in lr:
        if j in command:
            print("yes")
            print('1')
            player.stop()
            print('2')
            # and possibly garbage collect the player
            del globals()['player3']
            del globals()['instance3']
            return
    talk("Recherche de la vidéo. patientez s'il vous plait")
    
    results = YoutubeSearch(command, max_results=2)
    a=results.to_dict()
    url=""
    for i in a:
        ie=i['url_suffix'].split('&')[0]
        if ie:
            url= f"https://www.youtube.com{ie}"
            break
    '''videosSearch = VideosSearch(command, limit = 2)

    a=videosSearch.result()
    url=a["result"][0]['link']#["thumbnails"]['url'] '''
    print(url)
    ydl_opts = {}
    audio=[]
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                meta = ydl.extract_info(url, download=False)
                formats = meta.get('formats', [meta])
                audio = [(i["url"], i["format_note"], i["ext"]) for i in formats if(i['format_note'] in ["low", "medium"] and i['acodec']!='none')]# or i["ext"] == "m4a")]
                #print(audio)

    playurl =url# audio[0][0].replace("https", "http")
    
    media = instance.media_new(playurl)
    media.get_mrl()
    player.set_media(media)

    player.play()
    return

#youtube("J'ai continué ma route")

import requests
import json
API_ENDPOINT = 'https://api.wit.ai/message'
WIT_ACCESS_TOKEN = 'BVNT7WUMPAURTYREQBZF42HCFXFNMQI4'#B3GHXHLTXIASO7S4KY7UC65LMSTCDEHK'

def witt(mes):
   
    headers = {'Authorization': 'Bearer {}'.format(WIT_ACCESS_TOKEN)}
    query = {'q': str(mes)}

    resp = requests.get(API_ENDPOINT, headers=headers, params=query)
    data = resp.json()

    resp=data["intents"][0]["name"]
    print('Voila wit: ', resp)
    return resp
import random
pp=random.choice(["/home/pi/final_glass/dac.wav", "/home/pi/final_glass/instant.wav",
                  "/home/pi/final_glass/ok.wav","/home/pi/final_glass/patient.wav"])


def bible_command(test):
    audio(str(pp))
    test=test.lower()
    liv=""
    chp=""
    ve=""
    
    r=test.split()
    url="https://bible-api.com/"
    t=re.findall(r'\d+',test)#
    print(t, r)
    enz=0
    for i in r:
        if i in l3:
            print("bbb", r[r.index(i)-1])
            if type(r[r.index(i)-1])==int:
                print("oui")
                liv=f"{t[0]}"+l4[l3.index(i)]
                t=t[1:]
            else:
                liv=l2[l1.index(i)]
        elif i in l1:
            
            print("yes")
            
            liv=l2[l1.index(i)]
        if liv:   
            chp=t[0]
            ve=t[1]
            url=f"https://bible-api.com/{liv}+{chp}:{ve}"
            if ve!=t[-1]:
                if ve==t[-2]:
                    url+=f"-{t[-1]}"
                    break
                else:
                    u=""
                    n=[]
                    if "à" in test:
                        url+=f"-{t[2]}"
                        n=t[3:]
                    else:
                      n=t[2:]
                    print(t,n)
                    for i in n:
                        if n.index(i)==0:
                            u+=","
                        u+= f"{i}"
                        if i!=n[-1]:
                            u+=","
                    url+=f"{u}"
                    break
    print(url)                        
    resp=requests.get(url)
    response_dict = json.loads(resp.text)
    res=trans.translate(f"{response_dict['text']}", dest="fr").text
    print(res)
    return res



import threading
def trea(fonction, param):
    a = threading.Thread(target=fonction, args=[param])
    a.start()
 
 
def greet ():
    talk("Salut")
    

audio("/home/pi/final_glass/debut.mp3")
        
# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms



class MicrophoneStream:
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b"".join(data)


global ma
global mesag
global me
global mwsag
global mw
global oc
mesag = ""
me = 0
message = ''
ma = 0
mwsag = ""
mw = 0
oc = 0



def listen_print_loop(responses):
    global ma
    global message
    global mesag
    global me
    global mwsag
    global mw
    global oc

    num_chars_printed = 0
    l = ' '
    for response in responses:

        # print(1)
        if not response.results:
            continue

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript
        overwrite_chars = " " * (num_chars_printed - len(transcript))

        if not result.is_final:
            pass


        else:
            transcript = transcript.lower()
            en = 0
            print("Transcription: ", transcript)
            l += transcript + ' '  # + overwrite_chars+' '

            lb = ['sms', 'mms']
            lc = ['whatsapp', 'WhatsApp', 'gb whatsapp']
            ld = ["lecture ", "lire", "texte", "lis-moi", "lis"]
            la=['gmail', 'email', 'mail']
            # print(transcript.replace(i, ""))
            lh = ['mail', 'gmail', 'email', 'sms',
                  'mms', 'whatsapp', 'gb whatsapp',
                  "WhatsApp", "lecture", "lire","lis-moi", "lis"
                   ]
            if (ma == 0 and mw == 0 and oc == 0 and me == 0):
                for i in transcript.split(" "):
                    if i in ["glace", "glass", "classe ", "blast", "place"]:
                        # talk("oui monsieur")
                        audio("/home/pi/final_glass/audio.mp3")
                        l4=["radio", "web radio" ]
                        spl=transcript.split()
                        for n in l4:
                                if n in spl :
                                    #a = threading.Thread(target=youtube, args=[test])
                                    #a.start()
                                    radio(transcript.replace(i, ""))
                                    en=1
                                    break
                        l5=["youtube", "video", "vidéo" ]
                        
                        for nl in l5:
                                if nl in spl :
                                    
                                    '''a = threading.Thread(target=youtube, args=[test])
                                    a.start()'''
                                    youtube(transcript.replace(i, ""))
                                    en=1
                                    break
                        lbi=["bible", "biblique"]
                        witmess=""
                        for c in lbi:
                            if c in spl:
                                final(transcript.replace(c, ""))
                                en=1
                                break# change age_gender param from url to content
                
                        for h in lh:
                            print(h)
                            if en==1:
                                break
                            if not h in transcript.split(' ') and h == lh[-1]:
                                # print(h, 'envoi', transcript)
                                print("Message non trouvé")
                                final(transcript.replace(i, ""))
                                en = 1
                                break
                            elif not h in transcript:
                                pass
                            else:
                                print("Message trouvé", h, transcript.split(' '))
                                if en==1:
                                    break
                                else:
                                    if h in la:
                                        talk('quel message dois-je envoyer ?')
                                        ma = 1
                                        break
                                    elif h in lb:
                                        talk('quel message dois-je envoyer ?')
                                        me = 1
                                        break
                                    elif h in lc:
                                        talk('quel message dois-je envoyer ?')
                                        mw = 1
                                        break
                                    elif h in ld:
                                        '''if "localis" in transcript:
                                            final(transcript)
                                            break'''
                                        talk("Voulez vous un guide intelligent pour vous aider à la prise d'une photo convenable?")
                                        oc = 1
                                        break

                                break
                        audio("/home/pi/final_glass/audio.mp3")
                        break
            else:
                if ma == 1:
                    print("OK")
                    message = transcript
                    talk("à quelle adresse dois-je l'envoyer ?")
                    audio("/home/pi/final_glass/audio.mp3")
                    ma = 2
                    # time.sleep(2)
                elif ma == 2:
                    # ad_mail=transcript
                    a = transcript
                    talk("envoi en cours")
                    print(message)
                    email_alert("Vision Plus Message", message, a)
                    ma = 0
                    message = ''
                elif me == 1:
                    print("OK")
                    mesag = transcript
                    talk("à quelle numero dois-je l'envoyer ?")
                    audio("/home/pi/final_glass/audio.mp3")
                    me = 2
                    # time.sleep(2)
                elif me == 2:
                    # ad_mail=transcript
                    a = transcript
                    talk("envoi en cours")
                    print(mesag)
                    messages(mesag, a)
                    me = 0
                    messag = ''
                    audio("/home/pi/final_glass/audio.mp3")
                elif mw == 1:
                    print("OK")
                    mwsag = transcript
                    talk("à quelle numero dois-je l'envoyer ?")
                    audio("/home/pi/final_glass/audio.mp3")
                    # time.sleep(2)
                    mw = 2
                    # time.sleep(1)
                elif mw == 2:
                    # ad_mail=transcript
                    a = transcript
                    talk("envoi en cours")
                    print(mwsag)
                    whatsapp(mwsag, a)
                    mw = 0
                    messag = ''
                    # ma=0
                elif oc == 1:
                    oc = 0
                    a = transcript
                    if "non" in transcript.lower():
                        talk(vision2())
                        audio("/home/pi/final_glass/audio.mp3")
                    else:

                        talk('dans quelques secondes')
                        ocr2()
                        audio("/home/pi/final_glass/audio.mp3")

        
            if re.search(r"\b(exit|quit)\b", transcript, re.I):
                print("Exiting..")
                break

            # num_chars_printed = 0

        # print('Total:', l)








 







def main():
    language_code = "fr-FR"  # a BCP-47 language tag

    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code,
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config, interim_results=True
    )

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()

        requests = (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

        responses = client.streaming_recognize(streaming_config, requests)


        # Now, put the transcription responses to use.
        #listen_print_loop(responses)
        try:
            listen_print_loop(responses)
        except Exception as e:
            print(e)
            audio("/home/pi/final_glass/down.wav")
            return "Fin" 

#main()
import pyaudio
import struct
audi=pyaudio.PyAudio()              
import time
ACCESS_KEY='ZYreIahGLHskfNPw6lwWyrEi1FHrvLuY2M/H2nosz/3NmA5kRiS/1g=='
#'Xxjep0iYH3IuIopKJ5tN5usjCsCwFg5FHAztt2FkxhbM8hCCd76omA=='

import pvporcupine

porcupine = pvporcupine.create(
  access_key='Xxjep0iYH3IuIopKJ5tN5usjCsCwFg5FHAztt2FkxhbM8hCCd76omA==',
  keyword_paths=["/home/pi/final_glass/monsieur-glace_fr_raspberry-pi_v2_2_0.ppn"],
model_path='/home/pi/final_glass/porcupine_params_fr.pv'
)
#main()
greet()
while True:
    z=str(main())
    z="Fin"
    print(z, type(z))

    if z=="Fin":
        print("yes")
        try:

            audio_stream = audi.open(
                rate=porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=porcupine.frame_length)

            while True:
                pcm = audio_stream.read(porcupine.frame_length)
                pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

                keyword_index = porcupine.process(pcm)
                if keyword_index >= 0:
                    talk("Oui, je suis là.")
                    print("Hotword Detected")
                    audio_stream.stop_stream()  # "Stop Audio Recording
                    audio_stream.close()  # "Close Audio Recording
                    audi.terminate()
                    main()
                    break

                else:

                 print("Computer online")
        except:
                pass
    else:
        print("nono")
porcupine.delete()
