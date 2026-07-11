import socket

def get_ip_info(domain):
    print("\n===== IP Address Information =====")

    try:
        ip = socket.gethostbyname(domain)
        print("Domain     :", domain)
        print("IP Address :", ip)
    except socket.gaierror:
        print("Unable to find the IP address.")