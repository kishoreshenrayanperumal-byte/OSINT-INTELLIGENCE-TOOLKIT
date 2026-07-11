import socket

def port_scan(domain):
    print("\n====== Port Scan ======")

    try:
        ip = socket.gethostbyname(domain)
        print(f"Scanning {domain} ({ip})...\n")

        ports = {
            21: "FTP",
            22: "SSH",
            25: "SMTP",
            53: "DNS",
            80: "HTTP",
            110: "POP3",
            143: "IMAP",
            443: "HTTPS",
            3306: "MySQL",
            3389: "RDP"
        }

        for port, service in ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"[OPEN]   {port} ({service})")
            else:
                print(f"[CLOSED] {port} ({service})")

            sock.close()

    except Exception as e:
        print(f"Port Scan Error: {e}")