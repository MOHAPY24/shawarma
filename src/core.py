import json, ollama, os, sys
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory


session = PromptSession(history=FileHistory('src/configs/memory/.commandhistory.txt'))


try:
    t = True
    sys.argv[1]
except:
    t = False
    pass



client = ollama.Client(host="http://localhost:11434")
GLOB_MEMORY_PATH = "src/configs/memory/communication.json"
GLOB_SYSTEM_PATH = "src/configs/system.brstm"

if os.path.exists(GLOB_MEMORY_PATH):
    with open(GLOB_MEMORY_PATH, "r") as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                curr_data = data 
            else:
                curr_data = [] 
        except json.JSONDecodeError:
            curr_data = [] 
else:
    curr_data = []

with open(GLOB_SYSTEM_PATH, "r") as f:
    configs = json.loads(f.read())
    if not configs["practical"] and not configs["creative"] and not configs["factual"]:
        print("[x] Missing a NEEDED value in system.brstm..")
        quit(1)
    practical = configs["practical"]
    creative = configs["creative"]
    factual = configs["factual"]



def write_to_communications(new_data:dict):
    with open(GLOB_MEMORY_PATH, "w") as f:
        f.write(json.dumps(new_data, indent=4))


def factual_start():
    print(f"[*] Asking model '{factual}' for factual take...")
    factual_prompt = f"give a factual/proven/focused answer/choice to this text from a user, be detailed too: {user_input}"
    curr_data.append(client.chat(model=factual, messages=[{"role":"user", "content": factual_prompt}])['message']['content'])
    print(f"[*] Finished asking '{factual}'...")

def creative_start():
    print(f"[*] Asking model '{creative}' for a creative take...")
    creative_prompt = f"{curr_data}, give a creative/out-of-the-box/intresting answer/choice to this text from a user, you may use the JSON response from a model ment to give a factual response to the said text to use it on your own way, be detailed too: {user_input}"
    curr_data.append(client.chat(model=creative, messages=[{"role":"user", "content": creative_prompt}])['message']['content'])
    print(f"[*] Finished asking '{creative}'...")

def practical_start():
    print(f"[*] Asking model '{practical}' for a practical take...")
    practical_prompt = f"{curr_data}, give a practical/consise/conventional answer/choice to this text from a user, you may use the JSON response from 2 models ment to give a factual and creative choice to said text response to the said text to use it on your own way, be detailed too: {user_input}"
    curr_data.append(client.chat(model=practical, messages=[{"role":"user", "content": practical_prompt}])['message']['content'])
    print(f"[*] Finished asking '{practical}'...")


while True:
    try:
        if t:
            user_input = sys.argv[1]
        else:
            user_input = session.prompt('> ')
        factual_start()
        creative_start()
        practical_start()
        print(f"[*] Asking model '{factual}' to merge all responses to one big response...")
        factual_prompt = f"{curr_data}, using the JSON just passed to you, do not add or modify any information given. Merge all information into one detailed paragraph. Make it sound like one normal merged paragraph that explains everything."
        response = client.chat(model=factual, messages=[{"role":"user", "content": factual_prompt}])['message']['content']
        curr_data.append(response)
        print(response)
        write_to_communications(curr_data)
        if t:
            t = False
        
        
        
    except (EOFError, KeyboardInterrupt):
        print("quiting..")
        write_to_communications(curr_data)
        break   
