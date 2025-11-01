import json, ollama, os, sys
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from globals import client, GLOB_MEMORY_PATH, GLOB_SYSTEM_PATH
from checks import get_brstm, data_grab
from utils import *

session = PromptSession(history=FileHistory('src/configs/memory/.commandhistory.txt'))


try:
    t = True
    sys.argv[1]
except:
    t = False
    pass


curr_data = data_grab()



practical, creative, factual, addons = get_brstm()

while True:
    try:
        if t:
            user_input = sys.argv[1]
        else:
            user_input = session.prompt('> ')
        factual_start(factual, client, curr_data, addons, user_input)
        creative_start(creative, client, curr_data, addons, user_input)
        practical_start(practical, client, curr_data, addons, user_input)
        print(f"[*] Asking model '{factual}' to merge all responses to one big response...")
        factual_prompt = f"{curr_data}, using the JSON just passed to you, do not add or modify any information given. Merge all information into one detailed paragraph. Make it sound like one normal merged paragraph that explains everything."
        try:
            response = client.chat(model=factual, messages=[{"role":"user", "content": factual_prompt}])['message']['content']
        except ConnectionError:
            print("[x] Ollama couldnt respond, are you sure Ollama is running or is even installed?")
            exit(1)
        except ollama.ResponseError:
            print("[x] Ollama couldnt respond, you may not have enough RAM to load this model.")
            exit(1)
        curr_data.append(response)
        print(response)
        write_to_communications(curr_data)
        if t:
            t = False
    except (EOFError, KeyboardInterrupt):
        print("quiting..")
        write_to_communications(curr_data)
        break
