import requests

def get_technology_info(domain):
    print("\n===== Website Technology Detection =====")

    try:
        response = requests.get("https://" + domain, timeout=5)

        headers = response.headers
        html = response.text.lower()

        print("Server:", headers.get("Server", "Unknown"))
        print("Powered By:", headers.get("X-Powered-By", "Not Present"))

        if "wordpress" in html:
            print("CMS: WordPress")

        if "react" in html:
            print("Framework: React")

        if "bootstrap" in html:
            print("Framework: Bootstrap")

        if "cloudflare" in headers.get("Server", "").lower():
            print("CDN: Cloudflare")

    except Exception as e:
        print("Error:", e)