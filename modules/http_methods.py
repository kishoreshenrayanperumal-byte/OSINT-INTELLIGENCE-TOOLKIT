import requests

def get_http_methods(domain):
    print("\n====== HTTP Methods ======\n")

    url = f"https://{domain}"

    try:
        response = requests.options(url, timeout=5)

        methods = response.headers.get("Allow")

        if methods:
            print("Allowed Methods:")
            for method in methods.split(","):
                print(f"  {method.strip()}")
        else:
            print("Server did not return an Allow header.")

    except Exception as e:
        print(f"Error: {e}")