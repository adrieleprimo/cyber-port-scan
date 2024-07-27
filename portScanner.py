import socket
from services import port_services

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            service = port_services.get(port, "Unknown Service")
            return True, service
        else:
            return False,""

    except socket.error:
        return False, ""

