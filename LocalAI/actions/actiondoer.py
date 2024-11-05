from actions import launchwebsite
from actions import read_code
from actions import recall as recallmodule
from actions.createfile import create_file
import dbcoms

#Recall Function
#def recall(prompt):
   # recallmodule.recall(prompt=prompt)

def readfile():
    read_code.readfile()

def launchsite(prompt):
    launchwebsite.create_launch(prompt=prompt)

def checkcommand(prompt, convo):
    print('in here')
    if prompt[:5].lower() == '/read':
        print('read')
        read_code.readFile()
    elif prompt[:7].lower() == '/recall':
        print('recall')
        prompt = prompt[8:]
        recallmodule.recall(prompt=prompt, convo=convo)
        return prompt
    elif prompt[:7].lower() == '/launch':
        prompt = prompt[8:]
        launchsite(prompt=prompt)
        print('launched '+prompt)
        convo.append({'role': 'user', 'content': prompt})
        dbcoms.stream_response(prompt=prompt)
    elif prompt[:7] == '/forget':
        print('forget')
        dbcoms.remove_last_conversation()
        convo = convo[:-2]
        print('\n') 
    elif prompt[:9] == '/switchdb':
        prompt = prompt[9:]
        dbcoms.change_db('public_database') 
        dbcoms.store_conversations(prompt='memory stored', response=prompt)
    elif prompt[:9].lower() == '/memorize':
        print('memorize')
        prompt = prompt[10:]
        dbcoms.store_conversations(prompt='memory stored', response=prompt)
        print('\n')
    elif prompt[:13] == "/creatingFile":
        prompt = prompt[14:]
        create_file(prompt)

    else:
        return