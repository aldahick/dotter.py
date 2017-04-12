import json
import os
import shutil

def load():
    config_path = "./config.json"
    if not os.path.exists(config_path):
        shutil.copy("./config.default.json", config_path)
    file_handle = open("./config.json", "r")
    config = json.loads(file_handle.read())
    file_handle.close()
    return config
