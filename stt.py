# rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
import requests
import speech_recognition as sr 
import subprocess

bot_message= ""
message=""

while bot_mesaage !="Bye":

 r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything:")
        audiom= r.listen(source)
        try:
            message= r.recognize_google(audio)
            print("You said : {}".format(message))
        except:
            print("Sorry couldn't recognize your voice")
    if len(message)==0:
        continue
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": message})

    print ("", end=' ')
    for i in r.json():
        bot_mesaage = i['text']
        print(f"{'bot_message'}")