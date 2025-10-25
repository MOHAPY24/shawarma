import os

if not os.path.exists("src/configs/memory/communication.json"):
    os.system("mkdir src/configs/memory; touch src/configs/memory/communication.json")

if not os.path.exists("src/configs/system.brstm"):
    os.system("mkdir src/configs/system.brstm; touch src/configs/system.brstm")

os.system("python3 src/core.py")
exit(0)