import requests
import json

url = "https://gwtest.bisan.com/api/v2/DEMOAIC/REPORT/stockBalance?BSN-token=22095634"

payload={}
headers = {
  'Content-Type': 'application/json',
  'BSN-apiID': 'AIC',
  'BSN-apiSecret': 'vELYp42pzXTLNYlJupXjEJKeypVrepTWLNOXe9D4'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
