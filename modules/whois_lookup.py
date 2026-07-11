import whois

def get_whois_info(domain):
    info = whois.whois(domain)

    print("\n===== WHOIS Information =====")
    print("Domain Name    :", info.domain_name)
    print("Registrar      :", info.registrar)
    print("Creation Date  :", info.creation_date)
    print("Expiration Date:", info.expiration_date)
    print("Name Servers   :", info.name_servers)