from gtts import gTTS
import os
import playsound
import speech_recognition
import socketio
sio = socketio.Client()
sio.connect('http://localhost:8080')

# define variables
#file = "file.mp3"

# initialize text-to-speech(tts), create, play, then delete mp3 file(llamaVoice.mp3)
def speak(script):
    tts = gTTS(text=script, lang='en')
    filename = "llamaVoice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


#-------------------------------- SPEECH RECOGNITION START -------------------------------------------------------


# Initialize recognizer class (for recognizing the speech)
speech_listener = speech_recognition.Recognizer()
conversing = False

def text_to_speech(text):
    speak(text)
    conversing = False
    return conversing

def speech_to_text(speech_listener):
    
    print("Talk")
    audio_text = speech_listener.listen(source)
    print("Time over, thanks")
    text = speech_listener.recognize_google(audio_text)
    return (text)

#Correct Passcode must be array
def verify_passcode(passcodes, inputed_passcode):
    for passcode in passcodes:
        if passcode == inputed_passcode:
            return True
    raise Exception("Passcode failed")
        
#Needs asynchronous loop that checks if text is the same as it was 20 sec ago.  If so, break friendship
with speech_listener.Microphone() as source:
    while True:
        try:
            #If we are not in a conversation, scan for voice
            if not conversing:
                passcode = speech_to_text(speech_listener=speech_listener)
                #Initiates conversation and greets user
                my_passcodes=["hello llama", "hey llama"]
                conversing = verify_passcode(passcodes=my_passcodes, passcode=passcode)
                speak("Hello!")

            try:   
                #Listen for user request and turn it into text
                user_request = speech_to_text(speech_listener=speech_listener)

                #Send Request to Server Here
                #Response will be through Websocket
            #When error is thrown during user request phase
            except Exception as e:
                print("Exception Part 2: " + str(e))
                speak("Sorry I didn't quite catch that")
        #When command is thrown during passcode phase
        except Exception as e:
            #if text that is not 
            print("Exception: " + str(e))
            

        
#-------------------------------- SPEECH RECOGNITION END -------------------------------------------------------




