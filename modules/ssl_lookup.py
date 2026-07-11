import ssl
import socket

def get_ssl_info(domain):
    print("\n===== SSL Certificate Information =====")

    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as secure_sock:
                cert = secure_sock.getpeercert()

        print("Issuer      :", cert.get("issuer"))
        print("Issued To   :", cert.get("subject"))
        print("Valid From  :", cert.get("notBefore"))
        print("Valid Until :", cert.get("notAfter"))

    except Exception as e:
        print("SSL Error:", e)