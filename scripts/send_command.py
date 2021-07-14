import requests
import os
from scripts.parse_ports import main_port

def send_command(comm):

    address, port = main_port()

    os.environ['CURRENT_PORT'] = port

    
    os.environ[f'PARAMS_PORT_{port}'] = f'{comm["PROJECT_ID"]};{comm["JOB_ID"]};{comm["SAVE_PATH"]};{comm["CURRENT_FILE"]}'
    

    result = requests.get(f"{address}?command={comm['COMMAND']}")

    return result
