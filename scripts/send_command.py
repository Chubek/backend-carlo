import requests
import os
from scripts.parse_ports import main_port

def send_command(comm):    

    os.envirot['PROJECT_ID'] = comm['PROJECT_ID']
    os.envirot['JOB_ID'] = comm['JOB_ID']
    os.envirot['SAVE_PATH'] = comm['SAVE_PATH']
    os.envirot['CURRENT_FILE'] = comm['CURRENT_FILE']

    address = main_port()

    result = requests.get(f"{address}?command={comm['COMMAND']}")

    return result
