from portScanner import scan_port

def thread_scan(ip, port, open_ports):
    is_open, service = scan_port(ip, port)
    if is_open:
        print(f"Port {port} {service}: Open")
        open_ports.append((port, service))