import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")

        sock.close()
    except socket.error:
        print(f"Error connecting to port{port}")

if __name__ == "__main__":
    ip = "108.179.252.93"
    ports =  [80, 443, 22]

    for port in ports:
        scan_port(ip, port)
