import socket

def get_reverse_dns(domain):
    print("\n====== Reverse DNS Lookup ======\n")

    try:
        # Get IP from domain
        ip = socket.gethostbyname(domain)

        # Get hostname from IP
        hostname, alias, address = socket.gethostbyaddr(ip)

        print(f"IP Address : {ip}")
        print(f"Hostname   : {hostname}")

    except socket.herror:
        print("No Reverse DNS (PTR) record found.")

    except Exception as e:
        print(f"Error: {e}")