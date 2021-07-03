import requests
import os
from dotenv import dotenv_values

temp = dotenv_values(".env")

def send_command(comm):    

    os.envirot['PROJECT_ID'] = comm['PROJECT_ID']
    os.envirot['JOB_ID'] = comm['JOB_ID']
    os.envirot['SAVE_PATH'] = comm['SAVE_PATH']
    os.envirot['CURRENT_FILE'] = comm['CURRENT_FILE']

    
    address = temp["ADDRESS"]
    port = temp["PORT"]

    result = requests.get(f"{address}:{port}?command={comm['COMMAND']}")
