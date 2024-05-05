# Importing packages
import speech_recognition as sr
from gtts import gTTS
import playsound
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Creating Listener
listener = sr.Recognizer()

# Starting Alexa
print("***Rayan Here***")
tts = gTTS(text='I am your Rayan. What can I do for you?', lang='en')
tts.save("welcome.mp3")
playsound.playsound("welcome.mp3")

# Function to listen for instructions
def take_instruction():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "rayan" in instruction:
                instruction = instruction.replace('rayan', '')
                print(instruction)
    except:
        pass
    return instruction

# Function to play audio
def play_audio(audio_file):
    playsound.playsound(audio_file)

# Function to execute instructions
def play_alexa():
    instruction = take_instruction()
    print(instruction)

    if 'play' in instruction:
        song = instruction.replace('play', '')
        tts = gTTS(text=f"Playing {song} on YouTube", lang='en')
        tts.save("playing.mp3")
        play_audio("playing.mp3")
        pywhatkit.playonyt(song)
    
    elif "time" in instruction: 
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        tts = gTTS(text=f"The current time is {current_time}", lang='en')
        tts.save("time.mp3")
        play_audio("time.mp3")

    elif "date" in instruction:
        current_date = datetime.datetime.now().strftime('%d /%m /%Y')
        print(current_date)
        tts = gTTS(text=f"Today's date is {current_date}", lang='en')
        tts.save("date.mp3")
        play_audio("date.mp3")

    elif "how are you" in instruction:
        print('I am fine, how about you')
        tts = gTTS(text='I am fine, how about you', lang='en')
        tts.save("how_are_you.mp3")
        play_audio("how_are_you.mp3")
    
    elif 'What is your name' in instruction:
        tts = gTTS(text="I am Alexa, What can I do for you?", lang='en')
        tts.save("name.mp3")
        play_audio("name.mp3")

    elif 'who is' in instruction:
        human = instruction.replace('who is', '')
        info = wikipedia.summary(human, 1)
        print(info)
        tts = gTTS(text=info, lang='en')
        tts.save("info.mp3")
        play_audio("info.mp3")

    elif 'will you marry me' in instruction:
        print('Sorry, I am not free')
        tts = gTTS(text="Sorry, I am not free", lang='en')
        tts.save("not_free.mp3")
        play_audio("not_free.mp3")

    elif 'are you single' in instruction:
        print('I am in a relationship with wifi')
        tts = gTTS(text="I am in a relationship with wifi", lang='en')
        tts.save("relationship.mp3")
        play_audio("relationship.mp3")

    elif 'joke' in instruction:
        joke = pyjokes.get_joke()
        print(joke)
        tts = gTTS(text=joke, lang='en')
        tts.save("joke.mp3")
        play_audio("joke.mp3")

    elif 'pubg' in instruction:
        print('Shahmeer Mota hai')
        tts = gTTS(text="Shahmeer Mota hai", lang='en')
        tts.save("pubg.mp3")
        play_audio("pubg.mp3")

    else:
        print("Sorry, I don't understand that") 

# Main loop
while True:
    play_alexa()
