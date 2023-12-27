

from __future__ import division

mai = 0
message = ''
ad_mail = ''

import threading

import google
import speech_recognition
from  datetime import datetime
print(datetime.now())
from api import final, audio, bible_command, ocr1
from yolo import ocr2
from talk import talk
print(datetime.now())
import re
import sys
import time

from google.cloud import speech

import pyaudio
from six.moves import queue
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ='/home/pi/final_glass/key.json'
global val
# talk("Initialisation")

from email.message import EmailMessage
import smtplib
import ssl

import webbrowser
import pyautogui
import re

import smtplib
from email.message import EmailMessage
print("Import sucessfull")

audio("/home/pi/final_glass/audio.mp3")

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


def wh(num, mesa):
    url = f'https://web.whatsapp.com/send?phone={num}&text={mesa}'
    webbrowser.open(url)
    time.sleep(100)
    try:
        pyautogui.click(941, 732)
        pyautogui.press("enter")
        time.sleep(2)
        # pyautogui.hotkey('ctrl', 'w')
        # print("tab closed")
    except:
        pyautogui.click(941, 732)
        pyautogui.press("enter")
        time.sleep(2)
        # pyautogui.hotkey('ctrl', 'w')
        # print("tab closed")
    audio("/home/pi/final_glass/audio.mp3")


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
        pass
    """for i in m.split(" "):
        number""" '''
    print(number, t)
    a = threading.Thread(target=wh, args=[number, t])
    a.start()

    # pywhatkit.sendwhatmsg_instantly(phone_no=number, message=t,tab_close=True)
    talk(f"Votre message sera envoyé dans près de 30 secondes au numero {number}")
    # pyautogui.hotkey('ctrl', 'w')
    print("tab closed")


from twilio.rest import Client

account_sid = "ACc83428ecac55a44928c5a45a1ba52be3"
auth_token = "76ebe0a28f53d1c9056008180d8babee"
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
            from_="+13854798988"
        )
        print(call.sid)
        print("message envoyé")
        talk('message envoyé')
    except:
        talk("le numero est invalid, veuillez ressayer")
    # audio("/home/pi/final_glass/audio.mp3")


# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


class MicrophoneStream(object):
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
            # print(".")
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

            # close_tab()
            # sys.exit()
            # return 0
            lb = ['sms', 'mms']
            lc = ['whatsapp', 'WhatsApp', 'gb whatsapp']
            ld = ["lecture ", "lire", 'lis ', "lis-moi"]
            # print(transcript.replace(i, ""))
            lh = ['mail', 'gmail', 'email', 'sms',
                  'mms', 'whatsapp', 'gb whatsapp',
                  "WhatsApp" "lecture", "lire",
                  'lis', "lis-moi"]
            if (ma == 0 and mw == 0 and oc == 0 and me == 0):
                for i in transcript.split(" "):
                    if i in ["glace", "glass", "classe ", "blast"]:
                        # talk("oui monsieur")

                        audio("/home/pi/final_glass/audio.mp3")
                        # print("Voila Trans", transcript)
                        # print(transcript.split(' '))

                        for h in lh:
                            print(h)

                            if not h in transcript.split(' ') and h == lh[-1]:
                                # print(h, 'envoi', transcript)
                                print("Message non trouvé")
                                final(transcript.replace(i, ""))
                                en = 1
                                #break
                            elif not h in transcript:
                                pass
                            else:
                                print("Message trouvé", h, transcript.split(' '))
                                for tje in ['gmail', 'email']:
                                    # print(tje)
                                    if en == 1:
                                        break
                                    if tje in transcript.lower():
                                        talk('quel message dois-je envoyer ?')
                                        # time.sleep(2)
                                        # audio("/home/pi/final_glass/audio.mp3")
                                        ma = 1
                                        break

                                for tj in lb:
                                    if en == 1:
                                        break
                                    if tj in transcript.replace(i, "").lower():
                                        talk('quel message dois-je envoyer ?')

                                        # audio("/home/pi/final_glass/audio.mp3")
                                        me = 1
                                        # time.sleep(2)
                                        break

                                for tj in lc:
                                    if en == 1:
                                        break
                                    if tj in transcript.replace(i, "").lower():
                                        talk('quel message dois-je envoyer ?')
                                        # time.sleep(2)
                                        # audio("/home/pi/final_glass/audio.mp3")
                                        mw = 1
                                        break

                                for tj in ld:
                                    if en == 1:
                                        break
                                    if "localis" in transcript:
                                        final(transcript)
                                        break
                                    if tj in transcript.replace(i, "").lower():
                                        print(tj)
                                        talk(
                                            "Voulez vous un guide intelligent pour vous aider à la prise d'une photo convenable?")
                                        # time.sleep(1)
                                        # audio("/home/pi/final_glass/audio.mp3")
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
                if me == 1:
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
                if mw == 1:
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
                if oc == 1:
                    oc = 0
                    a = transcript
                    if "non" in transcript.lower():
                        ocr1()
                        audio("/home/pi/final_glass/audio.mp3")
                    else:

                        talk('dans quelques secondes')
                        ocr2()
                        audio("/home/pi/final_glass/audio.mp3")

                elif i in ['stop']:
                    # TimeClass(command=transcript.replace(i, "")).stop()
                    print("Tout stopé")
                    break

            # audio("/home/pi/final_glass/audio.mp3")

            # yield transcript
            # print(transcript + overwrite_chars)
            # print('Total:', l)

            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r"\b(exit|quit)\b", transcript, re.I):
                print("Exiting..")
                break

            # num_chars_printed = 0

        # print('Total:', l)


def main():
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
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
    # audio('/home/pi/final_glass/debut.mp3')

    with MicrophoneStream(RATE, CHUNK) as stream:
        try:
            audio_generator = stream.generator()
            requests = (
                speech.StreamingRecognizeRequest(audio_content=content)
                for content in audio_generator
            )

            responses = client.streaming_recognize(streaming_config, requests)

            # Now, put the transcription responses to use.
            try:
                a = listen_print_loop(responses)
                if a == 0:
                    return 0
            except:
                responses = client.streaming_recognize(streaming_config, requests)
                listen_print_loop(responses)

        except google.api_core.exceptions.Unknown as e:
            audio_generator = stream.generator()
            requests = (
                speech.StreamingRecognizeRequest(audio_content=content)
                for content in audio_generator
            )

            responses = client.streaming_recognize(streaming_config, requests)

            # Now, put the transcription responses to use.
            try:
                a = listen_print_loop(responses)
                if a == 0:
                    return 0
            except:
                responses = client.streaming_recognize(streaming_config, requests)
                listen_print_loop(responses)

import speech_recognition as sr

listener = sr.Recognizer()


def trea(fonction, param):
    a = threading.Thread(target=fonction, args=[param])
    a.start()



class TimeClass(threading.Thread):

    def __init__(self, command):
        threading.Thread.__init__(self)
        self.command = command

    def run(self):
        print('Debut de tread!!!')
        try:
            final(command=self.command)

        except Exception as e:
            print(e)

    def stop(self):
        # engine.stop()
        self.stopped = True


import time, webbrowser, pyautogui


def close_tab():
    pyautogui.hotkey('ctrl', 'w')
    print("tab closed")



main()
# if (KeyboardInterrupt):
# print('===> Finished Recording')
# break



