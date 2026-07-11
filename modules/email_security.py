import dns.resolver

def get_email_security(domain):
    print("\n====== Email Security Checker ======\n")

    # ---------- SPF ----------
    print("SPF Record:")
    try:
        answers = dns.resolver.resolve(domain, "TXT")

        found = False
        for answer in answers:
            text = answer.to_text().replace('"', '')
            if "v=spf1" in text:
                print(text)
                found = True

        if not found:
            print("Not Found")

    except Exception:
        print("Not Found")

    # ---------- DMARC ----------
    print("\nDMARC Record:")
    try:
        dmarc = "_dmarc." + domain
        answers = dns.resolver.resolve(dmarc, "TXT")

        for answer in answers:
            print(answer.to_text().replace('"', ''))

    except Exception:
        print("Not Found")

    # ---------- DKIM ----------
    print("\nDKIM Record:")

    selectors = [
        "default",
        "google",
        "selector1",
        "selector2"
    ]

    found = False

    for selector in selectors:
        try:
            record = f"{selector}._domainkey.{domain}"
            answers = dns.resolver.resolve(record, "TXT")

            print(f"{selector}: Found")
            found = True

        except Exception:
            pass

    if not found:
        print("No common DKIM selectors found")