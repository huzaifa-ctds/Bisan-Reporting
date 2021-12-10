import requests
import json

url = "https://gwtest.bisan.com/api/v2/DEMOAIC/login"

payload = json.dumps({
  "user": "test",
  "password": "a12345"
})
headers = {
  'Content-Type': 'application/json',
  'BSN-apiID': 'AIC',
  'BSN-apiSecret': 'vELYp42pzXTLNYlJupXjEJKeypVrepTWLNOXe9D4',
  '': ''
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
