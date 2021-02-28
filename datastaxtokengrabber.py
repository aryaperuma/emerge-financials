import requests
import json

url = "https://aca4e01c-1465-4012-8e84-f282757e54f9-us-east1.apps.astra.datastax.com/api/rest/v1/auth"

payload = "{\"username\":\"redacted\",\"password\":\"redacted\"}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "fd91ccce-5703-4cde-ab48-9bee17b2daba"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

rj = json.loads(response.text)

print (rj['authToken'])

