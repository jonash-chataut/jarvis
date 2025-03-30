import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibary
import requests
from openai import OpenAI

# API key and URL for news 
myAPI = "4a1a7bdb09c54353976fff55ab65d07b"
URL = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={myAPI}"

recognizer=sr.Recognizer()
engine = pyttsx3.init()
# function for text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()
# can also use gTTs for better 

# function for ai working
def aiProcess(command):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key= "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"
    )

    completion = client.chat.completions.create(
    model="google/gemini-2.0-flash-lite-preview-02-05:free",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis which performs basic tasks like alexa. Provide very short and concise answers, no more than 1-2 sentences."},
        {
            "role": "user",
            "content": command
        }
    ]
    )

    return (completion.choices[0].message.content)

# function for processing command
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(URL)
        if r.status_code == 200:
            data = r.json()
            for article in data["articles"]:
                speak(article["title"])  # Speaks headlines
        else:
            speak("Failed to fetch news:", r.status_code)
    else:
        # open AI will handle now
        output=aiProcess(c)
        speak(output)

        
if __name__=="__main__":
    speak("Initializing Jarvis")
    while True:
        #Listen for the wake word i.e. Jarvis
        #obtain audio from the microphone
        r = sr.Recognizer() #recognizer=sr.Recognizer() can also be used not necessary to make this
        print("Recognizing....")
        try:
             with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1) #will be lisenting for 2 second and 1 sec of phrase time limit
                 # recognize speech using Google
                word = r.recognize_google(audio)
                # print(word)
                if (word.lower()=="jarvis"):
                    speak("Yaa")
                    with sr.Microphone() as source:
                        # Listening for the command
                        print("Jarvis Active....")
                        audio = r.listen(source) 
                        command = r.recognize_google(audio)
                        processCommand(command)
                        # one time only running making
                        break


        except Exception as e:
            print(f"Error; {e}")

            