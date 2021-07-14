from dotenv import dotenv_values
import socket
import os

temp = dotenv_values(".env")

def test_port_free(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((temp['ADDRESSS'], port)) == 0


def test_or_assign_port_busy(port, action="test"):
    if action.lower() == "test":
        with open(temp['BUSY_PORT_LOC'] + ".port", 'r') as pf:
            ports = pf.readlines()
        busy_ports = list(set([int(p.strip()) for p in ports]))

        if not port in busy_ports:
            return True
        else:
            return False
    elif action == "assign":
        with open(temp['BUSY_PORT_LOC'] + ".port", "a" if os.path.exists(temp['BUSY_PORT_LOC'] + '.port') else 'w') as pf:
            pf.write(f"{port}\n")

        return []
    elif action == "unassign":
        with open(temp['BUSY_PORT_LOC'] + ".port", 'r') as pf:
            ports = pf.readlines()
        busy_ports = list(set([int(p.strip()) for p in ports]))

        if port in busy_ports:
            busy_ports = busy_ports.remove(port)
            with open(temp['BUSY_PORT_LOC'] + ".port", 'w') as pf:
                pf.writelines(busy_ports)
                return True
        else:
            return False



def read_or_write_port(port=None):
    if port is not None:
        with open(temp['ASSIGN_PORT_LOC'] + ".port", "a" if os.path.exists(temp['ASSIGN_PORT_LOC'] + ".port") else 'w') as pf:
            pf.write(f"{port}\n")

        return []

    else:
        with open(temp['ASSIGN_PORT_LOC'] + ".port", 'r') as pf:
            ports = pf.readlines()

        return list(set([p for p in ports if p.isnumeric()]))


def generate_address(port):
    return f"{temp['ADDRESS']}:{port}"


def main_port():
    current_ports = read_or_write_port()

    if len(current_ports) == 0:
        return generate_address(8000)

    non_busies = [test_or_assign_port_busy(port) for port in current_ports]

    while not True in non_busies:
        non_busies = [test_or_assign_port_busy(port) for port in current_ports]

    non_busy_index = non_busies.index(True)

    non_busy_port = current_ports[non_busy_index]

    if not test_port_free(non_busy_port):
        test_or_assign_port_busy(non_busy_port, action="assign")
        return generate_address(non_busy_port), non_busy_port

    return generate_address(8000), 8000







