"""Demo for the HTTP service.

User should change the url if the http service is not running locally.

"""

import requests

url = "http://localhost:8000/upload"
fin = open('fruits.png', 'rb')
files = {'file': fin}
try:
    r = requests.post(url, files=files)
    print(r.text)
finally:
    fin.close()
