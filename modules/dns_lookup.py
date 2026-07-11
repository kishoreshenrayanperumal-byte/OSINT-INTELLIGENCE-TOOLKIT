import dns.resolver

def get_dns_info(domain):
    print("\n===== DNS Information =====")

    record_types = [
    "A",
    "AAAA",
    "MX",
    "NS",
    "TXT",
    "CNAME",
    "SOA"
]

    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"\n{record} Records:")
            for answer in answers:
                print(answer)
        except Exception:
            print(f"\n{record} Records: Not Found")