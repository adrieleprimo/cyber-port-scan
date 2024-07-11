import socket
from portScanner import scan_port

def main():
    ip = input("Enter the IP address for port scanning: ")
    open_ports = []
    
    try:
        for port in range(1, 1025):
            if scan_port(ip, port):
                print(f"Port {port}: Open")
                open_ports.append(port)
    except KeyboardInterrupt:
        print("\nScan interrupted by the user")
    except socket.gaierror:
        print("Error resolving host")
    except socket.error:
        print("Unable to connect to the server")
    with open("open_ports.txt", "w") as file:
        for port in open_ports:
            file.write(f"Port{port}: Open\n")
if __name__ == "__main__":
    main()
