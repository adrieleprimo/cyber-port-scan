<p align="center"><img align="center" width="280" src="./assets//cyber-port-scan.gif"/></p>


# Cyber Port Scan
Cyber Port is intended to be its own tool, with the aim of scanning open ports of a given ip. The focus is on improving notions of cybersecurity and having our own projects focused on this area.

**Please note that this repository is for educational purposes only!**

## How to use
1. Clone the repository:

```bash
git clone https://github.com/adrieleprimo/cyber-port-scan
cd cyber-port-scanner
```

2. Create and activate a virtual environment:
 ```bash
    python3 -m venv venv
    source venv/bin/activate   # Unix System
    .\venv\Scripts\activate    # Windows System
    ```

    3. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```

    ## Features

- Port scanning from 1 to 1024.
- Displays open ports in the terminal.
- Saves open ports in an `open_ports.txt` file.