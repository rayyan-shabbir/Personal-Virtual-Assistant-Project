# Importing packages
# Importing speech recogningtion
import speech_recognition as sr

# Importing libraries to respond back (Using this pkg our assistant can respond to us)
import pyttsx3

# Importing package that make automation of youtube and whatsapp easily (to run functionalities)
import pywhatkit

# getting datetime package
import datetime

# Importing package for searching information through wikepedia
import wikipedia

# Importing package for jokes
import pyjokes


# Creating Listener (which will recognize our voice)
listener = sr.Recognizer()

# Create varibale machine and initialize it with python text to speech
machine = pyttsx3.init()

# Setting Alexa voice to female
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[1].id)

# Starting Alexa
print("***Rayan Here***")
machine.say('I am your Rayan')
machine.say('What can I do for you')
machine.runAndWait()

# Initialize our text to speech audio
# Creating function talk and pass paramter that we want to hear
def talk(text):
    machine.say(text)
    machine.runAndWait()

# talk("Ali Hassan ko do thappar lagao")

# It will manage all that we say as an instruction to JARVIS 
def take_instruction():

    # If our microphone does not works
    try:
        # using microphone
        with sr.Microphone() as source:     # giving a name: source

            # Our assistant is ready to hear to us
            print("Listening...")

            # creating new varibale as speech and force the listener to listen this origin 
            speech = listener.listen(source) 

            # create variable instruction and recognize the origin voice and using google API converted it into text
            instruction = listener.recognize_google(speech)

            # Writing a command to detect the word "ALEXA" (which is our VA name) 
            instruction = instruction.lower()

            if "Rayan" in instruction:
                # If we don't want to print Jarvis in our instruction
                instruction = instruction.replace('Rayan', '')

                # print the instruction (what we are speaking to our system) given by us
                print(instruction)

    except:
        pass
    return instruction


# Creating function to include all the functionalities (play any video on youtube, respond date and time)
def play_alexa():
    instruction = take_instruction()

    print(instruction)

    # Adding functionalities 

    # Playing song on YouTube
    if 'play' in instruction:
        # Adding functionality to talk back like "Playing video etc"
        song = instruction.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    
    # To get current time
    elif "time" in instruction: 
        time = datetime.datetime.now().strftime('%I:%M %p')   # %I:%M %p is the format in which we want time
        print(time)
        talk('Current time is ' + time)

    # To get current date
    elif "date" in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')   # %d /%m /%Y is the format in which we want date
        print(date)
        talk("Today's date " + date)

    # Basic Greetings
    elif "how are you" in instruction:
        print('I am fine, how about you')
        talk('I am fine, how about you')
    
    # VA name
    elif 'What is your name' in instruction:
        talk('I am Alexa, What can I do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is', '')
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)

    # JOKES

    elif 'will you marry me' in instruction:
        print('Sorry, I am not free')
        talk('Sorry, I am not free')


    elif 'are you single' in instruction:
        print('I am in a relationship with wifi')
        talk('I am in a relationship with wifi')

    elif 'joke' in instruction:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    # instruction that Alexa doesn't understand 
    else:
        print("Sorry, I don't understand that") 

while True:
    play_alexa()