import json, ollama
from globals import GLOB_MEMORY_PATH

def write_to_communications(new_data:dict):
    with open(GLOB_MEMORY_PATH, "w") as f:
        f.write(json.dumps(new_data, indent=4))


def factual_start(factual, clients, curr_data, addons, user_input):
    print(f"[*] Asking model '{factual}' for factual take...")
    factual_prompt = f"give a factual/proven/focused answer/choice to this text from a user, be detailed too, {addons}: {user_input}"
    try:
        curr_data.append(clients.chat(model=factual, messages=[{"role":"user", "content": factual_prompt}])['message']['content'])
    except ConnectionError:
        print("[x] Ollama couldnt respond, are you sure Ollama is running or is even installed?")
        exit(1)
    except ollama.ResponseError:
        print("[x] Ollama couldnt respond, you may not have enough RAM to load this model.")
        exit(1)
    print(f"[*] Finished asking '{factual}'...")

def creative_start(creative, clients, curr_data, addons, user_input):
    print(f"[*] Asking model '{creative}' for a creative take...")
    creative_prompt = f"{curr_data}, give a creative/out-of-the-box/intresting answer/choice to this text from a user, you may use the JSON response from a model ment to give a factual response to the said text to use it on your own way, be detailed too, {addons}: {user_input}"
    try:
        curr_data.append(clients.chat(model=creative, messages=[{"role":"user", "content": creative_prompt}])['message']['content'])
    except ConnectionError:
        print("[x] Ollama couldnt respond, are you sure Ollama is running or is even installed?")
        exit(1)
    except ollama.ResponseError:
        print("[x] Ollama couldnt respond, you may not have enough RAM to load this model.")
        exit(1)
    print(f"[*] Finished asking '{creative}'...")

def practical_start(practical, clients, curr_data, addons, user_input):
    print(f"[*] Asking model '{practical}' for a practical take...")
    practical_prompt = f"{curr_data}, give a practical/consise/conventional answer/choice to this text from a user, you may use the JSON response from 2 models ment to give a factual and creative choice to said text response to the said text to use it on your own way, be detailed too, {addons}: {user_input}"
    try:
        curr_data.append(clients.chat(model=practical, messages=[{"role":"user", "content": practical_prompt}])['message']['content'])
    except ConnectionError:
        print("[x] Ollama couldnt respond, are you sure Ollama is running or is even installed?")
        exit(1)
    except ollama.ResponseError:
      print("[x] Ollama couldnt respond, you may not have enough RAM to load this model.")
      exit(1)
    print(f"[*] Finished asking '{practical}'...")

