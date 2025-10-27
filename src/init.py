import os, sys

try:
    t = True
    sys.argv[1]
except:
    t = False
    pass

if not os.path.exists("src/configs/memory/communication.json"):
    os.system("mkdir src/configs/memory; touch src/configs/memory/communication.json")

if not os.path.exists("src/configs/system.brstm"):
    os.system("mkdir src/configs/system.brstm; touch src/configs/system.brstm")

if not t:
    os.system("python3 src/core.py")
else:
    os.system(f"python3 src/core.py {sys.argv[1]}")
exit(0)