import threading
import socket
from threadingScan import thread_scan

def main():
    ip = input("Enter the IP address for port scanning: ")
    open_ports = []
    threads = []
    try:
        for port in range(1, 1025):
            thread = threading.Thread(target=thread_scan, args=(ip, port, open_ports))
            threads.append(thread)
            thread.start()

            for thread in threads:
                thread.join()
    except KeyboardInterrupt:
        print("\nScan interrupted by the user")
    except socket.gaierror:
        print("Error resolving host")
    except socket.error:
        print("Unable to connect to the server")

    with open("open_ports.txt", "w") as file:
        for port, service  in open_ports:
            file.write(f"Port{port} {service} : Open\n")
if __name__ == "__main__":
    main()
