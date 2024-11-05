import ast
import chromadb
from colorama import Fore
import ollama
from tqdm import tqdm

client=chromadb.Client()

def create_queries(prompt):
    query_msg = (
        'You are a first principle reasoing search query AI agent. '
        'Your list of search queries will be ran on an embedding database of all your conversations'
        'you have ever had with the user. With first principles create a Pythoon list of queries to '
        'serach the embeddings database for any data tha would be necessary to have access to in '
        'order to correctly respond to the prompt. Your response must be a Python list with no syntax errors. '
        'Do not explain anything and do not ever generate anything but perfect synteax Python list'
    )
    #Fine Tuning skipped. Took easier route
    query_convo = [
        {'role': 'system', 'content': query_msg},
        {'role': 'user', 'content': 'Write an email to my car insurance company and create a pursuasive request for them to lower my monthly rate.'},
        {'role': 'assistant', 'content': '["What is the users name?", "what is the users current auto insurance provider?", "What is the onthly rate the user currently pays for auto insurance?]'},
        {'role': 'user', 'content': 'how can i convert the speak function in my llama3 python voice assistant to use pyttsx3 instead of OpenAi implementation?'},
        {'role': 'assistant', 'content': '["Llama 3 voice assistant", "Python voice assistant", "OpenAI TTS", "openai speak"]'},
        {'role': 'user', 'content': prompt}
    ]

    response = ollama.chat(model='llama3.1', messages=query_convo)
    print (Fore.YELLOW + f'\nVector database queries: {response["message"]["content"]}\n')

    try:
        return ast.literal_eval(response['message']['content'])
    except:
        return [prompt]

#test number of query results 21:51 https://www.youtube.com/watch?v=5xPvsMX2q2M
def retrieve_embeddings(queries, results_per_query=5):
    embeddings = set()
    
    #For each query, get embedding from vector database that is most related to the query(tqdm is for loading bar)
    for query in tqdm(queries, desc='Processing queries to vector database'):

        #Query for Embedding from vector database
        response = ollama.embeddings(model='nomic-embed-text', prompt=query) 
        query_embedding = response['embedding']

        #Get embeddings from vector database that are most related to the query
        vector_db= client.get_collection(name='conversations')
        results = vector_db.query(query_embeddings=[query_embedding], n_results=results_per_query)
        print('LOOK HERE')
        print(results['documents'][0])
        best_embeddings = results['documents'][0]

        for best in best_embeddings:
            print('for embed ')
            print(best)
            if best not in embeddings: #If embedding has not been added to 'embeddings' set yet.
                print(best)
                if 'yes' in classify_embedding(query=query, context=best):
                    print('if yes ')
                    print(best)
                    embeddings.add(best)

    return embeddings

def classify_embedding(query, context):
    classify_msg = (
        'You are an embedding classification AI agent. Your input will be a prompt and one embedded chunk of text. '
        'You will not respond as an AI assistant. You only response "yes" or "no". '
        'Determine whether the context contains data that directly is related to the search query. '
        'If the context is seemingly exactly what the search query needs, respond "yes" if it is anything but directly '
        'related respond "no". Do not respond "yes" unless the content is highly relavent to the search query.'
    )

    classify_convo = [
        {'role': 'system', 'content': classify_msg},
        {'role': 'user', 'content': f'SEARCH QUERY: What is the users name? \n\nEMBEDDED CONTEXT: You are Pluto. How can I help you today X?'},
        {'role': 'assistant', 'content': 'yes'},
        {'role': 'user', 'content': f'Llama 3 Python Voice Assistant \n\nEMBEDDED CONTEXT: Siri is a voice assistant on Apple iOS and Mac OS. The voice assistant is designed to take voice prompts and help the user complete simple tasks on the device. '},
        {'role': 'assistant', 'content': 'no'},
        {'role': 'user', 'content': f'SEARCH QUERY: {query} \n\nEMBEDDED CONTEXT: {context}'}
    ]

    response = ollama.chat(model='llama3.1', messages=classify_convo)
    
    return response['message']['content'].strip().lower()
def recall_all(prompt, convo):
    queries = create_queries(prompt=prompt)
    embeddings = retrieve_embeddings(queries=queries, results_per_query=200)
    convo.append({'role': 'user', 'content': f'MEMORIES: {embeddings} \n\n USER PROMPT: {prompt}'})
    print (f'\n{len(embeddings)} message:response embeddings added for context.')

def recall(prompt, convo):
    queries = create_queries(prompt=prompt)
    embeddings = retrieve_embeddings(queries=queries)
    convo.append({'role': 'user', 'content': f'MEMORIES: {embeddings} \n\n USER PROMPT: {prompt}'})
    print (f'\n{len(embeddings)} message:response embeddings added for context.')
