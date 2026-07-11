import requests

def get_robots_info(domain):
    print("\n===== robots.txt =====")

    try:
        url = "https://" + domain + "/robots.txt"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print("Status : Found\n")
            print(response.text)
        else:
            print("robots.txt not found.")

    except Exception as e:
        print("Error:", e)