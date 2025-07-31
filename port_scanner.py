import socket

def scan_ports(target, port_range):
    print(f"[+] Scanning target: {target}")
    for port in port_range:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            sock.close()
        except KeyboardInterrupt:
            print("\n[!] Interrupted by user")
            break
        except Exception as e:
            print(f"[ERROR] {e}")

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    port_start = int(input("Enter start port: "))
    port_end = int(input("Enter end port: "))
    port_range = range(port_start, port_end + 1)
    scan_ports(target_ip, port_range)