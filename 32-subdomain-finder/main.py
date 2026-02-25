import requests

target_input = input("Please enter your target website (example.com): ")

with open("subdomain.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()
        url = "http://" + word + "." + target_input

        try:
            response = requests.get(url, timeout=3)
            print(f"[+] Found: {url} (Status Code: {response.status_code})")
        except requests.ConnectionError:
            pass  # Subdomain does not exist
        except requests.Timeout:
            pass  # Request timed out
        except requests.RequestException:
            pass  # Any other request-related error