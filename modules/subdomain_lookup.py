import socket

def get_subdomain_info(domain):
    print("\n====== Subdomain Finder ======\n")

    subdomains = [
        "www",
        "mail",
        "ftp",
        "api",
        "admin",
        "blog",
        "dev",
        "test",
        "cdn",
        "shop"
    ]

    for sub in subdomains:
        subdomain = f"{sub}.{domain}"

        try:
            ip = socket.gethostbyname(subdomain)
            print(f"[FOUND] {subdomain} --> {ip}")
        except socket.gaierror:
            print(f"[NOT FOUND] {subdomain}")