from characterai import PyCAI
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

client= PyCAI('Your key')
client.start()

#char=input('Ingrese el Prompt: ')
#Usando el Chat de Mai
char='AEcOCw-PvQyxifqwKoZC93nI3sMtcOD0Z2vRhjaz5YA'
chat=client.chat.get_chat(char)

participants=chat['participants']

if not participants[0]['is_human']:
    tgt = participants[0]['user']['username']
else:
    tgt = participants [1]['user']['username']

#Ingreso de Voz
recognizer=sr.Recognizer()
mic=sr.Microphone()
lang='es-us'
while True:
    print("***")
    with mic as source:
        audio=recognizer.listen(source)
    text=recognizer.recognize_google(audio,language='ES')
    print("You: ",text)
    if text=="salir":
        break
    message=text
    data = client.chat.send_message(
        chat['external_id'],tgt,message
    )
    name=data['src_char']['participant']['name']
    text=data['replies'][0]['text']
    speech=gTTS(text=text,lang=lang,slow=False)
    speech.save("rpta.mp3")
    print(f"{name}:{text}")
    playsound("rpta.mp3",False)
    os.remove("rpta.mp3")
    stoper=input("//")