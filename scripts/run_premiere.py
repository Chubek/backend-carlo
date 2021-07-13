import subprocess
import os
from dotenv import dotenv_values
import scripts.parse_ports as pp
import sandboxie
temp = dotenv_values(".env")

sbie = sandboxie.Sandboxie()
settings = sbie.make_sandbox_setting('default')

def run_stop_premiere(port, action="start"):
    if action == "start":
        if not 'PORT_FREE' in os.environ:
            os.environ['PORT_FREE'] = "0"

        print(f'Starting Premiere on port {port}')
        
        sbie.create_sandbox(f'{port}', settings=settings)

        try:
            proc = sbie.execute([temp['PATH_TO_PREMIERE']], f'{port}')
            wait_res = proc.wait()

            if wait_res:
                pp.read_or_write_port(port=port)

        except:
            return False
    else:
        try:
            sbie.terminate_sandbox_processes(f'{port}')
            sbie.delete_content(f'{port}')   
            sbie.remove_sandbox(f'{port}')

            return True
        except:
            return False


