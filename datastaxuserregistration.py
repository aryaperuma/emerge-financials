import uuid
import time
import requests
import json

utoken = str(uuid.uuid4())
time.sleep(1)
utoken2 = str(uuid.uuid4())
time.sleep(1)
utoken3 = str(uuid.uuid4())


def gimmetoken():
    url = "https://aca4e01c-1465-4012-8e84-f282757e54f9-us-east1.apps.astra.datastax.com/api/rest/v1/auth"

    payload = "{\"username\":\"redacted\",\"password\":\"redacted\"}"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "fd91ccce-5703-4cde-ab48-9bee17b2daba"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    # print(response.text)

    rj = json.loads(response.text)

    # print (rj['authToken'])

    return rj['authToken']




username = "redacted"
pw = "redacted"
role = "donor"

imgurl = "https://pickaface.net/gallery/avatar/unr_sample_161118_2054_ynlrg.png"


url = "https://aca4e01c-1465-4012-8e84-f282757e54f9-us-east1.apps.astra.datastax.com/api/rest/v1/keyspaces/data/tables/users/rows"

atoken = gimmetoken()

payload = {}
pc = []
pc.append({"name":"id","value":utoken})
pc.append({"name":"name","value":username})
pc.append({"name":"password","value":pw})
pc.append({"name":"role","value":role})

payload ['columns'] = pc

jpayload = json.dumps(payload)

# payload = "{\"columns\":[,,,]}"
headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'x-cassandra-request-id': utoken2,
    'x-cassandra-token': atoken,
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=jpayload, headers=headers)

print(response.text)
