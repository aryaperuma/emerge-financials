import requests
import uuid
import json


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

utoken = str(uuid.uuid4())
atoken = gimmetoken()

# userid = "115db214-8862-45bd-ad71-3b3ccf0156d7"
userid = "9d8290f2-266f-42d8-8344-516711394743"


url = "https://aca4e01c-1465-4012-8e84-f282757e54f9-us-east1.apps.astra.datastax.com/api/rest/v1/keyspaces/data/tables/users/rows/" + userid

headers = {
    'accept': "application/json",
    'x-cassandra-request-id': utoken,
    'x-cassandra-token': atoken,
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

rjs = json.loads(response.text)

pw = "redacted"
found = 0
if rjs['count'] >0: 
    print (rjs['rows'][0]['password'])
    if rjs['rows'][0]['password'] == pw:
        found = 1

if found == 1:
    print("success")
else:
    print("fail")



