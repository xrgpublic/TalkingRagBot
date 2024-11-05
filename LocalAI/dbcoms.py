import chromadb
from colorama import Fore
import ollama
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv, dotenv_values
import os

client=chromadb.Client()

load_dotenv()
#If you want to put your passwoird in the .env file
DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_PARAMS = {
    'dbname': 'memory_agent',
    'user': 'mruser',
    'password': "isSuperCool",
    'host': 'localhost',
    'port': '5432',
}





def connect_db():
    conn = psycopg.connect(**DB_PARAMS)
    return conn


def change_db(dbname):
    DB_PARAMS.update({
        'dbname': dbname,
        'user': 'mruser',
        'password': "isSuperCool",
        'host': 'localhost',
        'port': '5432',
    })


def fetch_conversations():
    conn = connect_db()
    with conn.cursor(row_factory=dict_row) as cursor:
        cursor.execute('SELECT * FROM conversations')
        conversations = cursor.fetchall()
    conn.close()
    return conversations

def store_conversations(prompt, response):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            'INSERT INTO conversations (timestamp, prompt, response) VALUES (CURRENT_TIMESTAMP, %s, %s)',
            (prompt, response)
        )
        conn.commit()
    conn.close()

def remove_last_conversation():
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM conversations WHERE id = (SELECT MAX(id) FROM conversations)')
        conn.commit()
    conn.close()

def create_vector_db(conversations):
    vector_db_name = 'conversations'
    try:
        client.delete_collection(name=vector_db_name)
    except ValueError:
            pass
    vector_db = client.create_collection(name=vector_db_name)
    print(Fore.YELLOW + "Loading")
    for c in conversations:
        serialized_convo = f'prompt: {c['prompt']} response: {c['response']}'
        response = ollama.embeddings(model='nomic-embed-text', prompt=serialized_convo)
        embedding = response['embedding']
        vector_db.add(
            ids=[str(c['id'])],
            embeddings=[embedding],
            documents=[serialized_convo]
        )
    

    