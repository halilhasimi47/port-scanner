Port Scanner
A simple Python port scanner that scans a specified IP address within a given port range and lists open ports.

Requirements
Python 3.x

Usage
Open your terminal or command prompt.

Navigate to the directory containing port_scanner.py.

Run the script:

bash
Kopyala
Düzenle
python port_scanner.py
Enter the requested information:

Target IP address

Start port number

End port number

Example
less
Kopyala
Düzenle
Enter target IP address: 192.168.1.1
Enter start port: 20
Enter end port: 80
[+] Scanning target: 192.168.1.1
[OPEN] Port 22
[OPEN] Port 80
Warning
Do not scan systems without proper authorization.

This program uses simple socket connections and does not include advanced features.
