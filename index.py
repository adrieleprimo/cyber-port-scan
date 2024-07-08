import socket
from portScanner import scan_port

def main():
    ip = input("Enter the IP address for port scanning: ")
    try:
        for port in range(1, 1025):
            scan_port(ip, port)
    except KeyboardInterrupt:
        print("\nScan interrupted by the user")
    except socket.gaierror:
        print("Error resolving host")
    except socket.error:
        print("Unable to connect to the server")
if __name__ == "__main__":
    main()
