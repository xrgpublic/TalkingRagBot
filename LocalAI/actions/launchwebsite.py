import ast
import webbrowser
import ollama


def create_launch(prompt):
    launch_msg = (
        'You are an text parsing AI agent. Your input will be a prompt. '
        'You will not respond as an AI assistant. You will only respond with the website that is relavent to the input prompt.'
    )

    launch_convo = [
        {'role': 'system', 'content': launch_msg},
        {'role': 'user', 'content': 'What is googles website?.'},
        {'role': 'assistant', 'content': 'www.google.com'},
        {'role': 'user', 'content': 'what is githubs website?'},
        {'role': 'assistant', 'content': 'www.github.com'},
        {'role': 'user', 'content': prompt}
    ]
    response = ollama.chat(model='llama3.1', messages=launch_convo)
    webbrowser.open(response["message"]["content"], new=2)
    try:
        return ast.literal_eval(response['message']['content'])
    except:
        return [prompt]