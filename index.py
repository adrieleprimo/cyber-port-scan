import socket
from portScanner import scan_port

def main():
    ip = input("Enter the IP address for port scanning: ")
    open_ports = []
    
    try:
        for port in range(1, 1025):
            is_open, service = scan_port(ip, port)
            if is_open:
                print(f"Port {port} ({service}): Open")
                open_ports.append((port, service))
    except KeyboardInterrupt:
        print("\nScan interrupted by the user")
    except socket.gaierror:
        print("Error resolving host")
    except socket.error:
        print("Unable to connect to the server")

    with open("open_ports.txt", "w") as file:
        for port in open_ports:
            file.write(f"Port{port} {service} : Open\n")
if __name__ == "__main__":
    main()
