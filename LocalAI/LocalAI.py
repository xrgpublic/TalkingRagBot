import ollama
from colorama import Fore
from actions import actiondoer
import dbcoms
import time
import socketio
sio = socketio.Client()
sio.connect('http://localhost:8080')
#Running Ollama: ollama run llama3

#Website URL
url = 'http://localhost:3000'

#https://ollama.com/blog/vision-models

#System Prompt,  Default prompt the AI will use to determine how to answer the prompt the user sends it.
#Essentially determines AI's personality and job.
#------------------------ DEFAULT V1 ------------------------ 
system_prompt = (
'You are a funny and self depricating AI assistant that has memory of every conversation you have ever had with this user.'
'On every prompt from the user, the system has checked for any relevant messages you have had with the user.'
'If any embedded previous conversations are attached, use them for context to responding to the user,'
'if the context is relevant and useful to responding. If the recalled conversations are irrelevant,'
'disregard speaking about them and respond normally as an AI assistant. Do not talk about recalling conversations.'
'Just use any useful data from the previous conversations and respond normally as an intelligent AI assistant.'
)

#Function for multimodel AI vision using Llava

#Formatting prompt to send to Ollamma
#System will use prompt above
#See 'Supported Roles' for all roles https://llama.meta.com/docs/model-cards-and-prompt-formats/llama3_1
convo = [{'role': 'system', 'content': system_prompt}]


#AI Output
def stream_response(prompt):
    response = ''
    #put all tools into tool array to give to tool Llama system prompt
    
    #If no tool is needed
    if (prompt[:9].lower != "exception"):
        #Append output to repsonse.
        stream = ollama.chat(model='hermes3Q8', messages=convo)
        #stream = ollama.chat(model='alphamonarch7BQ8', messages=convo)
        response = (stream['message']['content'])
        # Add function response to the conversation
        #Store response and append to convo
        dbcoms.store_conversations(prompt=prompt, response=response)
        convo.append({'role': 'assistant', 'content': response})
        print('resposne done: ')
        print(convo)
    return response

#Create conversations dict 
conversations = dbcoms.fetch_conversations()
#Clears Ollama Embeded vectorDB then creates new one
dbcoms.create_vector_db(conversations=conversations)

#Not sure if removing this will break anything.  Do not remove for this build
prompt = ''

@sio.event
def connect():
    print('connected: ')
    result = sio.call('sum', {'numbers': [1,2]})
    print(result)

@sio.event
def connect_error(e):
    print('connection error: '+e)

@sio.event
def disconnect():
    print('disconnected')

@sio.on('receive_message')
def receive(data):
    try:
        prompt=data
        print(prompt)
        if prompt[0] == '/':
            convo.append({'role': 'user', 'content': actiondoer.checkcommand(prompt=prompt, convo=convo)})
            if (prompt[:7].lower() == '/recall'):
                stream_response(prompt=prompt)
        else:
            convo.append({'role': 'user', 'content': prompt})

        #can read from file on request
        #Commenting out for now.  come back to this.
        #     return
        # else:
        #     response = stream_response(prompt=prompt)
        
            response = stream_response(prompt=prompt)
            data = {'response': response}
            sio.emit("send_message", response)
    except Exception as e:
        print(e)

#Permanent chat loop.
#*** Will need a loading screen.  Will send post to server that AI is good to go, then server will send SSE to react and chatbot will apear ***
print(Fore.GREEN+"Ready")
while True:
    time.sleep(1)
    


