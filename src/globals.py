import ollama


client = ollama.Client(host="http://localhost:11434")
GLOB_MEMORY_PATH = "src/configs/memory/communication.json"
GLOB_SYSTEM_PATH = "src/configs/system.brstm"