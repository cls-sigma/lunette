
import os
import vlc
from vision import read,objects,analyse
#from pydub import AudioSegment
#from pydub.playback import play
from io import BytesIO

import openai
import time
import sys
import speech_recognition as sr
#import pywhatkit
import datetime
import wikipedia
from urllib.request import urlopen
import json
import random
import wolframalpha
from googletrans import Translator
import threading
import pip
import time
import pygame
from map import gsearch, myadress
from map3 import directions, position
trans=Translator()
import random
#import pandas as pd

from age_gender import age_gender
from talk import audio
import io
from io import BytesIO
import string
from picotts import PicoTTS
picotts = PicoTTS()
picotts.voice = 'fr-FR'
from pygame import mixer, time
mixer.pre_init(8000, -16, 2, 2048 )
mixer.init()

def talk(text):
    if text:

        wavs = picotts.synth_wav(text)
        sound = mixer.Sound(buffer=wavs)
        aud = sound.play()
        while aud.get_busy() == True:
            continue

l1=["Genèse", "Exode", "Lévitique", "Nombres", "Deutéronome", "Josué","Juges",
    "Ruth","1 Samuel","2 Samuel","1 Rois","2 Rois","1 Chroniques","2 Chroniques"
    ,"Esdras","Néhémie","Esther",
    "Job","Psaumes", "Proverbes", "Ecclésiaste", "Cantique des cantiques","Ésaïe","Jérémie","Lamentations","Ézéchiel","Daniel","Osée","Joël","Amos"
,"Abdias","Jonas","Michée","Nahum","Habacuc","Sophonie","Aggée","Zacharie",
    "Malachie","Matthieu","Marc","Luc","Jean", "Actes des Apôtres","Romains",
"1 Corinthiens","2 Corinthiens"
,"Galates","Éphésiens",'Philippiens','Colossiens',
    "1 Thessaloniciens","2 Thessaloniciens","1 Timothée","2 Timothée","Tite",
    "Philémon","Hébreux","Jacques",
    "1 Pierre","2 Pierre","1 Jean","2 Jean", "3 Jean", "Jude" ,"apocalypse"]



l2=["Genesis","Exodus","Leviticus","Numbers","Deuteronomy",
    "Joshua","Judges","Ruth","1 Samuel","2 Samuel","1 Kings",
        "2 Kings","1 Chronicles","2 Chronicles"
,"Ezra","Nehemiah","Esther","Job","Psalms","Proverbs",
    "Ecclesiastes","Song of Solomon","Isaiah"
,"Jeremiah","Lamentations","Ezekiel","Daniel","Hosea","Joel",
    "Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah"
    ,"Haggai","Zechariah"
,"Malachi", "Matthew","Mark","Luke","John","Acts","Romans",
    "1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians"
,"Colossians",
    "1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy","Titus",
    "Philemon","Hebrews","James","1 Peter","2 Peter","1 John","2 John","3 John",
    "Jude","Revelation"]


l3=["Samuel","Rois","Chroniques",
    "Corinthiens","Thessaloniciens"
    ,"Timothée", "Pierre","Jean",
   ]
l4= ["Samuel",
        "Kings","Chronicles",
     "Corinthians","Thessalonians",
     "Timothy",
     "Peter","John"]
#print(len(l3), len(l4))
l=[f.lower() for f in l1]
l1=l
l=[f.lower() for f in l3]
l3=l
#l1=[f.lower() for f in l1]
print(len(l1), len(l2))
import json
import re
import requests
from googletrans import Translator
trans=Translator()

pp=random.choice(["/home/pi/final_glass/dac.wav", "/home/pi/final_glass/instant.wav",
                  "/home/pi/final_glass/ok.wav","/home/pi/final_glass/patient.wav"])


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
            
            if  r[r.index(i)-1].isnumeric():
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

#bible_command("lis moi dans la bible  chapitre 1 verset 2") 
'''def ocr1():
    print("fonction ocr1")'''
    
def greetMe ():
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
        talk('Bonjour, Je suis Vision Pluse, votre assistant virtuel. Je suis à votre service')

    if 12 <= current_hour < 18:
        talk('Bonne après midi !, Je suis Vision Pluse, votre assistant virtuel. Je suis à votre service')

    if current_hour >= 18 and current_hour != 0:
        talk('Bonsoir, Je suis Vision Pluse, votre assistant virtuel. Je suis à votre service')

def heure():
        date = datetime.datetime.now().strftime("%D")
        date = date.split("/")
        mois = ['Janvier', "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre",
                "novembre", "décembre"]

        heure = datetime.datetime.now().strftime("%H:%M:%S")
        date=datetime.datetime.now().strftime("%Y-%m-%d")
        print(heure)
        talk(f'il est actuelement {heure}, Nous sommes le {date}')#{date[1]} {mois[int(date[0]) - 1]} 20{date[-1]}')
        
        
def alarme(tes):
    a=0
    for i in range(tes):
        time.sleep(1)
    print('time over')
    from pygame import mixer
    pygame.mixer.music.load("audio.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


meteo_key='b300ac8123331e1d48227eaff6e29f32'

import requests
import json
import datetime

import openai







villes=["lome", "sokode", "kara", "kpalime", "atakpame", "kpalime",
 "bassar","tsevie", "atakpame", "aneho", "mango", "dapaong",
 "tchamba", "niamtougou", "bafilo", "notse", "badou", "tabligbo",
 "biankouri", "vogan", "sotouboua", "kande", "amlame", "Galangachi", "Kpagouda"
        , "kante"]

def alpha(test):
    app_id = "AXE7WX-5U96VJLJUJ"
    client = wolframalpha.Client(app_id)
    t=trans.translate(test, dest="en").text
    res = client.query(t)
    print(t)
    # Includes only text from the response
    try:
        answer = next(res.results).text
        answer=trans.translate(answer, dest="fr").text
        print(answer)
        return answer
    except:
        return mes(test)
# récupération de la ville choisie par l'utilisateur
def meteo(test):
   
    audio(str(pp))
    test=test.replace("é", "e").replace('è', 'e')
    ville=""
    l=test.split()
    for i in l:
        if i in villes:
            print("ville: ", i)
            ville=i
            break
    try:
        if not ville:
            ville="lome"
    # récupère le temps actuel
        url_weather = "http://api.openweathermap.org/data/2.5/weather?q=" + ville + f"&APPID={meteo_key}"
        print(url_weather)
        t1=' '
        r_weather = requests.get(url_weather)
        data = r_weather.json()
        if (ville =="lome"):
            ville='lomé'
            
        t1+="Vous etes a " + ville+ "\n"

        # temperature moyenne
        t = data['main']['temp']
        t=f"{t - 273.15}"[:5]
        t1+="La température moyenne est de {} degres Celsiuse".format(t) + "\n"
        # écart de température
        t_min = f"{data['main']['temp_min'] - 273.15}"[:5]
        t_max = f"{data['main']['temp_max'] - 273.15}"[:5]
        t1+="Les températures varient entre {}".format(t_min) + " a {} degrés Celsiuse".format(t_max) + "\n"
        # taux d'humidité
        humidite = data['main']['humidity']
        t1+="Taux d'humidité de {}".format(humidite) + "%"+ "\n"
        # état du ciel
        temps = data['weather'][0]['description']
        t1+="Conditions climatiques : {}".format(trans.translate(temps, dest="fr").text)+ "\n"

        url_forecast = "http://api.openweathermap.org/data/2.5/forecast?q=" + ville + f"&APPID={meteo_key}"
        r_forecast = requests.get(url_forecast)
        data = r_forecast.json()
        # print(data)

        for i in range(0, 3):
            t= data['list'][i]['main']['temp']
            t = f"{t - 273.15}"[:5]
            temps = data['list'][i]['weather'][0]['description']
            time = data['list'][i]['dt_txt']
            t1+="Previsions pour le {}".format(time)+"\n"
            t1+="La température moyenne est de {} degrés Celsiuse".format(t)+"\n"
            t1+="Conditions climatiques : {}".format(trans.translate(temps, dest="fr").text)+"\n"
        return t1
    except:
        print("ville non trouvé")
        talk("J'ai quelqueux difficultés à trouver les informations, patientez")
        return alpha(test).replace("|", ":").replace("°C", "degré Celsiuse")


def trea(fonction, param):
    a=threading.Thread(target=fonction,args=[param])
    a.start()



from GoogleNews import GoogleNews
def news():
    audio(str(pp))
    googlenews = GoogleNews(period='2d', lang='fr')
    print(datetime.datetime.now())
    #talk("patientez s'il vous plait")
    googlenews.search('nouvelles du jour')
    news=googlenews.get_texts()
    news='; '.join(news)
    print(news)
    print(datetime.datetime.now())
    if news:
       return news
    else:
       return "Je n'ai pas pu trouver les nouvelles, Vous pouvez réessayer"


import json
def storie():
  audio(str(pp))
  url = "http://shortstories-api.onrender.com/" 
  try:
    response = requests.get(url)#, params=payload)
    data = response.json()
    t=f"Le titre de l'histoire est: {trans.translate(data['title'], dest='fr').text}\n "
    t+=f" Auteur: {trans.translate(data['author'], dest='fr').text}\n"
    t+=f"{trans.translate(data['story'], dest='fr').text}"
    t+=f"la leçon de morale est: {trans.translate(data['moral'], dest='fr').text}"
  except:
    t="Une erreur s'est produite. Veuillez ressayer svp"
  audio('/home/pi/final_glass/notif.mp3')
  return t

import requests


def blagues():
  t=''
  audio(str(pp))
  url="https://api.blablagues.net/?rub=blagues"
  try:
    response = requests.get(url)#, params=payload)
    data = response.json()
    
    i=data
    t=''
    
    t+=i["data"]['content']['text_head']+"\n"
    t+=i["data"]['content']['text']+"\n"
    t+=i["data"]['content']['text_hidden']+"\n"
    print(t)
  except:
    t="Je rencontre une erreur. Vous pouvez ressayer plus tard. "
  return t


import cv2  
from vision import sentiment, analyse, localize_objects, ocr1, read, objects  
def vision1():

    vid = cv2.VideoCapture(0)
    
    talk("capture dans quelques secondes")
    t = " "
    c = 0
    while (True):

        ret, frame = vid.read()
        frame = cv2.rotate(frame, cv2.ROTATE_180)# cv2.imshow('frame', frame)
        if c == 1:
    
            try:
                t += analyse(img=frame) + " \n"
            except:
                pass
            
            try:
                t +=ocr1(content=frame) + " \n"
            except:
                pass
            try:
                t += objects(content=frame) + " \n"
            except:
                pass
        
            
            break
        c += 1
        
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return t


def vision2():

    vid = cv2.VideoCapture(0)
    vid = cv2.rotate(vid, cv2.ROTATE_180)
    talk("capture dans quelques secondes")
    t = " "
    c = 0
    while (True):

        ret, frame = vid.read()        # cv2.imshow('frame', frame)
        if c == 2:
            audio("/home/pi/final_glass/camera.mp3")
            try:
                t +=ocr1(content=frame) + " \n"
            except:
                pass
            
            break
        c += 1
      
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return t


def localize_capture():
    vid = cv2.VideoCapture(2)
    talk("capture dans quelques secondes")
    t = " Aucun object devant vous "
    c = 0
    while (True):

        ret, frame = vid.read()        # cv2.imshow('frame', frame)
        if c == 1:
            audio("/home/pi/final_glass/camera.mp3")
           
            try:   
                t = localize_objects(content=frame) + " \n"
            except:
                pass
            try:   
                t = objects(content=frame) + " \n"
            except:
                pass
           
            
            break
        c += 1
        return t
        #time.sleep(1)

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return t


def final(test):
    test=test.lower()
    l=test.split()
    l1=["heure", "date"]
    for i in l1:
        if i in l:
            print("heure actuele")
            heure()
            return
    l6=["nouvelles", "nouvelle", "nouvel","journal", "infos"]
    for i in l6:
        if i in l:
            trea(talk, news())
            return
    l7=["histoire", "conte", "histoires" ]
    for i in l7:
        if i in l:
            
            trea(talk, storie())
            return
    l13=["blagues", "blague", "comédie", "drole","drôle", "connerie" ]
    for i in l13:
        if i in l:
            talk(blagues())
            return
    witmess=""
    try:    
        witmess=witt(test)
    except:
        pass
    if witmess:
        if (witmess=='recherche'):
                audio(str(pp))
                talk(gsearch(test.replace(i, '')))
                return
        elif (witmess=='saluation'):
               print("Salutation")
               greetMe()
               return
        elif (witmess=='meteo'):
       
                print("meteo actuele")
                talk(meteo(test))
                return
        elif (witmess=='math'):
                print("operation mathematique")
                audio(str(pp))
                talk(alpha(test))
                return
        
        elif (witmess=='vision'):
                
                talk(vision1())# change age_gender param from url to content
                return
        elif (witmess=='bible'):
                
                
                talk(bible_command(test.replace(i, '')))# change age_gender param from url to content
                return
        elif (witmess=='object'):
                
                
                talk(localize_capture())# change age_gender param from url to content
                return
               
        
        elif (witmess=='localisation'):
                talk("patientez s'il vous plait")
                print("t: ", test)
                trea(talk, directions(destination=test.split(i)[-1], language="fr"))#directions(destination=, language="fr"))
                return
        elif (witmess=='position'):
        
                print("ma localisation")
                talk(position())
                return
        elif (witmess=='desactive'):
                mixer.init()
                mixer.quit()
            
    else:
        l10=["cherche", "recherche","qu'est-ce", "google", "wikipedia", "wikipédia",
             "internet", "ligne", "qui est"]
        for i in l10:
            if i in l:
                audio(str(pp))
                talk(gsearch(test.replace(i, '')))
                return
        l0=["bonjour", "bonsoir", "salut", "bon apres midi", "allo"]
        for i in l0:
            if i in l:
               print("Salutation")
               greetMe()
               return
        
        l2=["meteo", "moment", "météo" ]
        for i in l2:
            if i in l:
                print("meteo actuele")
                talk(meteo(test))
                return
        l3=["calcul", "calcule","calcule-moi", ]
        for i in l3:
            if i in l:
                print("operation mathematique")
                audio(str(pp))
                talk(alpha(test))
                return
        
        
        
        
        l8=["décris", "decrire","décrire", "devant", "devant-moi",
           "vois" ]
        for i in l8:
            if i in l:
                
                talk(vision1())# change age_gender param from url to content
                return
        l9=["bible", "biblique","bibliquement" ]
        for i in l9:
            if i in l:
                
                
                talk(bible_command(test.replace(i, '')))# change age_gender param from url to content
                return
               
        
        l11=[ "localisation", "localise", "trouve", "trouve-moi","où",
              "où se trouve","localise-moi", "localises-moi"]
        for i in l11:
            if i in l:
                print("t: ", test.split(i)[-1])
                talk(directions(destination=test.split(i)[-1], language="fr"))#directions(destination=, language="fr"))
                return
        l12=[ "adresse", "position", "perdu"]
        for i in l12:
            if i in l:
                print("ma localisation")
                talk(position())
                return
        l0=["stop", "coupe", "arrête"]
        for i in l0:
            if i in l:
                mixer.init()
                mixer.quit()
                return
        
        
