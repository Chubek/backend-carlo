from dotenv import dotenv_values
import socket
import os

temp = dotenv_values(".env")

def test_port_free(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((temp['ADDRESSS'], port)) == 0


def test_or_assign_port_busy(port, action="test"):
    if action == "test":
        with open(temp['BUSY_PORT_LOC'] + ".port", 'r') as pf:
            ports = pf.readlines()
        busy_ports = list(set([int(p.strip()) for p in ports]))

        if not port in busy_ports:
            return True
    else:
        with open(temp['BUSY_PORT_LOC'] + ".port", "a" if os.path.exists(temp['BUSY_PORT_LOC'] + '.port') else 'w') as pf:
            pf.write(f"{port}\n")

        return []



def read_or_write_port(port, action="read"):
    if action == "write":
        with open(temp['ASSIGN_PORT_LOC'] + ".port", "a" if os.path.exists(temp['ASSIGN_PORT_LOC'] + ".port") else 'w') as pf:
            pf.write(f"{port}\n")

        return []

    else:
        with open(temp['ASSIGN_PORT_LOC'] + ".port", 'r') as pf:
            ports = pf.readlines()

        return list(set([p for p in ports if p.isnumeric()]))






