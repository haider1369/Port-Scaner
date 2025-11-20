import socket
import threading
from datetime import datetime

# Timeout for each connection attempt
socket.setdefaulttimeout(1)

print_lock = threading.Lock()

def scan_port(target, port):
    """Scan a single port."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        result = s.connect_ex((target, port))
        if result == 0:
            with print_lock:
                print(f"[OPEN] Port {port} is OPEN")

                # Try grabbing banner
                try:
                    s.send(b"Hello\r\n")
                    banner = s.recv(1024).decode().strip()
                    if banner:
                        print(f"    Banner: {banner}")
                except:
                    pass

    except:
        pass

    finally:
        s.close()


def main():
    print("===== PYTHON PORT SCANNER =====")
    target = input("Enter target IP or domain: ").strip()

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("❌ Invalid domain or IP")
        return

    print(f"\nTarget: {target} ({target_ip})")
    print("Scan Types:")
    print("1. Single Port")
    print("2. Port Range")
    print("3. Full Scan (1–65535)\n")

    choice = input("Select option (1/2/3): ")

    ports = []

    if choice == "1":
        port = int(input("Enter port: "))
        ports.append(port)

    elif choice == "2":
        start = int(input("Start port: "))
        end = int(input("End port: "))
        ports = list(range(start, end + 1))

    elif choice == "3":
        print("⚠️ Full scan selected. This may take time.")
        ports = list(range(1, 65536))

    else:
        print("❌ Invalid option")
        return

    print("\n===== Scanning Started =====")
    print(f"Start Time: {datetime.now()}\n")

    threads = []

    for port in ports:
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n===== Scan Complete =====")
    print(f"End Time: {datetime.now()}")


if __name__ == "__main__":
    main()
