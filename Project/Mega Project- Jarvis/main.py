import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx
import musicLibrary
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
engine.setProperty("rate", 144)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
newsApi = "e4138627804e46689e83635678933057"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(text)

def aiProcess(command):
    client = OpenAI(api_key="enter-api_key",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("Opening facebook")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://in.linkedin.com")
        speak("Opening linkedin")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speak("Opening Instagram")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening Youtube")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsApi}")
        if r.status_code == 200:
          # Parse the JSON response
          data = r.json()
          
          # Extract the articles
          articles = data.get('articles', [])
          
          # Print the headlines
          for article in articles:
              speak(article['title'])
    else:
        #let open AI handle the request
        output = aiProcess(c)
        speak(output)
        


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
