from globals import GLOB_SYSTEM_PATH, GLOB_MEMORY_PATH
import json, os


def get_brstm():
    with open(GLOB_SYSTEM_PATH, "r") as f:
        configs = json.loads(f.read())
        try:
            practical = configs["practical"]
            creative = configs["creative"]
            factual = configs["factual"]
            try:
                addons = configs["addons"]
            except KeyError:
                addons = ""
            finally:
                return practical, creative, factual, addons
        except KeyError:
            print("[x] Missing a NEEDED value in system.brstm..")
            quit(1)


def data_grab():
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
    return curr_data