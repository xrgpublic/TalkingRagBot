from actions import launchwebsite
from actions import recall as recallmodule
import dbcoms

#Recall Function
#def recall(prompt):
   # recallmodule.recall(prompt=prompt)

def launchsite(prompt):
    launchwebsite.create_launch(prompt=prompt)

def checkcommand(prompt, convo):
    if prompt[:7].lower() == '/recall':
        print('recall')
        prompt = prompt[8:]
        recallmodule.recall(prompt=prompt, convo=convo)
        return prompt
    elif prompt[:10].lower() == '/recallall':
        recallmodule.recall_all(prompt=prompt, convo=convo)
    elif prompt[:7].lower() == '/launch':
        prompt = prompt[8:]
        launchsite(prompt=prompt)
        print('launched '+prompt)
        convo.append({'role': 'user', 'content': prompt})
        #dbcoms.stream_response(prompt=prompt)
    elif prompt[:7] == '/forget':
        print('forget')
        dbcoms.remove_last_conversation()
        convo = convo[:-2]
        print('\n') 
    elif prompt[:9].lower() == '/memorize':
        print('memorize')
        prompt = prompt[10:]
        dbcoms.store_conversations(prompt='memory stored', response=prompt)
        print('\n')
    else:
        return