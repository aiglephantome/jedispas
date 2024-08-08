import requests
import time
import webbrowser

proxies = [
    "http://159.69.220.40:3128",
    "http://89.207.129.100:3128",
    "http://64.225.8.192:80",
    # ... add more proxies here
]

url = "https://www.tiktok.com"

for i in range(10):
    proxy = proxies[i % len(proxies)]
    response = requests.get(url, proxies={"http": proxy})
    webbrowser.open(url, new=2) # opens the url in a new tab
    time.sleep(3) # waits for 3 seconds
    # closes the tab
    for j in range(10):
        try:
            webbrowser.get("windows-default").close(url)
        except webbrowser.Error:
            time.sleep(0.1)