import requests
import json

url = "https://gwtest.bisan.com/api/v2/DEMOAIC/REPORT/salesByCustomerPerItemRpt"

payload = json.dumps({
  "TRANSACTION_ID": "5634317",
  "record": {
    "name": "My New Contact",
    "phone": "022961111",
    "email": "info@test.com",
    "area": "1",
    "isCustomer": "True",
    "cusPriceList": "S",
    "cusAccount": "1300"
  }
})
headers = {
  'Content-Type': 'application/json',
  'BSN-apiID': 'AIC',
  'BSN-apiSecret': 'vELYp42pzXTLNYlJupXjEJKeypVrepTWLNOXe9D4',
  'BSN-token': '4f817018'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
