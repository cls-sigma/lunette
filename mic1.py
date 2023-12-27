
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
#import speech_recognition
#from ultralytics import YOLO
#import openai

#import pandas as pd

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

from youtube_search import YoutubeSearch
import vlc
import yt_dlp as youtube_dl
print("Import sucessfull")


print(datetime.now())


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
url = "https://api.ultramsg.com/instance51200/messages/chat"
def wh(num, mesa):

    payload = f"token=e1rtvgpzsd18n19p&to=%2B228{num}&body={mesa}"
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
   
    print(number, t)
    talk(f"envoi du message au numero {number}")
 
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
    



def youtube(command):
    
    if globals().get('player1'):
        instance = globals()['instance1']
        player = globals()['player1']
    else:
        instance = globals()['instance1'] = vlc.Instance("--no-video")
        player = globals()['player1'] = instance.media_player_new()
    lr=["arrête-moi", "arrête", "stop"]
    
    for j in lr:
        if j in command:
            print("yes")
            print('1')
            player.stop()
            print('2')
            # and possibly garbage collect the player
            del globals()['player1']
            del globals()['instance1']
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

    print(url)
    ydl_opts = {}
    audio=[]
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                meta = ydl.extract_info(url, download=False)
                formats = meta.get('formats', [meta])
                audio = [(i["url"], i["format_note"], i["ext"]) for i in formats if(i['format_note'] in ["low", "medium"] and i['acodec']!='none')]# or i["ext"] == "m4a")]
                #print(audio)

    playurl = audio[0][0]
    
    media = instance.media_new(playurl)
    media.get_mrl()
    player.set_media(media)

    player.play()
    return

import threading
def trea(fonction, param):
    a = threading.Thread(target=fonction, args=[param])
    a.start()
 
 
def greet ():
    talk("Salut")
  
#audio("/home/pi/final_glass/debut.mp3")
# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

class MicrophoneStream:
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(
            self: object,
            rate: int = RATE,
            chunk: int = CHUNK
    ) -> None:
        """The audio -- and generator -- is guaranteed to be on the main thread.
        """
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self: object) -> object:
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            #input_device_index=1,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )
        
        self.closed = False

        return self

    def __exit__(
            self: object,
            type: object,
            value: object,
            traceback: object,
    ) -> None:
        """Closes the stream, regardless of whether the connection was lost or not."""
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(
            self: object,
            in_data: object,
            frame_count: int,
            time_info: object,
            status_flags: object,
    ) -> object:
        """Continuously collect data from the audio stream, into the buffer.

        Args:
            in_data: The audio data as a bytes object
            frame_count: The number of frames captured
            time_info: The time information
            status_flags: The status flags

        Returns:
            The audio data as a bytes object
        """
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self: object) -> object:
        """Generates audio chunks from the stream of audio data in chunks.

        Args:
            self: The MicrophoneStream object

        Returns:
            A generator that outputs audio chunks.
        """
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

def listen_print_loop(responses: object) -> str:
    
    num_chars_printed = 0
    for response in responses:
        if not response.results:
            continue

        
        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript

       
        overwrite_chars = " " * (num_chars_printed - len(transcript))

        if not result.is_final:
            sys.stdout.write(transcript + overwrite_chars + "\r")
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:
            print(transcript + overwrite_chars)
            talk("oui monsieur")

            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r"\b(exit|quit)\b", transcript, re.I):
                print("Exiting..")
                break

            num_chars_printed = 0

        

def main() -> None:
    """Transcribe speech from audio file."""
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
    language_code = "fr-FR"  # a BCP-47 language tag

    client = speech.SpeechClient.from_service_account_json('/home/pi/final_glass/key.json')
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
        listen_print_loop(responses)

if __name__ == "__main__":
    talk("Bienvenue monsieur")
    main()
