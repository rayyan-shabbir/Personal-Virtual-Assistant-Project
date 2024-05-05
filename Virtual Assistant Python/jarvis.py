# Importing speech recogningtion
import speech_recognition as sp

# Importing libraries to respond back (Using this pkg our assistant can respond to us)
import pyttsx3

# Importing package that make automation of youtube and whatsapp easily (to run functionalities)
import pywhatkit

# getting datetime package
import datetime

# Importing package for searching information through wikepedia
import wikipedia



# Creating Listener (which will recognize our voice)
listener = sp.Recognizer()

# Create varibale machine and initialize it with python text to speech
machine = pyttsx3.init()

# Initialize our text to speech audio
# Creating function talk and pass paramter that we want to hear
def talk(text):
     machine.say(text)
     machine.runAndWait()

# It will manage all that we say as an instruction to JARVIS 
def input_instruction():
    global instruction

    # If our microphone does not works
    try:
        # using microphone
        with sp.Microphone() as origin:      # giving a name origin

            # Our assistant is ready to hear to us
            print("Listening...")

            # creating new varibale as speech and force the listener to listen this origin 
            speech = listener.listen(origin) 

            # create variable instruction and recognize the origin voice and using google API converted it into text
            instruction = listener.recognize_google(speech)

            # Writing a command to detect the word "JARVIS" (which is our VA name) 
            instruction = instruction.lower()

            if "jarvis" in instruction:
                # If we don't want to print Jarvis in our instruction
                instruction = instruction.replace("jarvis", " ")
                # print the instruction (what we are speaking to our system) given by us
                print(instruction)


            # print(instruction)

    except:
        pass
    return instruction


# Creating function to include all the functionalities (play any video on youtube, respond date and time)
def play_jarvis():
    instruction = input_instruction()
    print(instruction)

    # Adding functionalities 

    # Playing song on YouTube
    if "play" in instruction:
        # Adding functionality to talk back like "Playing video etc"
        song = instruction.replace('play', "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    # To get current time
    elif "time" in instruction: 
        time = datetime.datetime.now().strftime('%I:%M%p')   # %I:%M%p is the format in which we want time
        talk("Current time" + time)

    # To get current date and date
    elif "date" in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')   # %d /%m /%Yis the format in which we want date
        talk("Today's date " + date)

    # Basic Greetings
    elif "how are you" in instruction:
        talk('I am fine, how about you')

    # VA name
    elif 'What is your name' in instruction:
        talk('I am Jarvis, What can I do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)

    # instruction that Jarvis doesn't understand 
    else:
        print("Sorry, I don't understand that") 

play_jarvis()
