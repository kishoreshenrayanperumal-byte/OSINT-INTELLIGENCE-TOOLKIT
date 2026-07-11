import requests

def get_headers_info(domain):
    print("\n===== HTTP Security Headers =====")

    try:
        url = "https://" + domain
        response = requests.get(url, timeout=5)

        headers = response.headers

        security_headers = [
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Referrer-Policy"
        ]

        for header in security_headers:
            print(f"{header}: {headers.get(header, 'Not Present')}")

    except Exception as e:
        print("Error:", e)