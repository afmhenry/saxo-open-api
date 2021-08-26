import requests
import sys
import json

def getAPI(url, params, headers,):
    Request = requests.get(url,params=params,headers=headers)
    if Request.status_code == 200:
        Response = Request.json()
        return Response
    else:
        return ""

BaseUrl = "https://gateway.saxobank.com/sim/openapi"

AccountKey = sys.argv[1]
ClientKey = sys.argv[2]
AccessToken = sys.argv[3]

Headers = {'Authorization': AccessToken,'Accept': "application/json"}
Parameters = {'AccountKey': AccountKey, 'ClientKey': ClientKey}

GetAccountPath = "/port/v1/balances"

AccountInfo = getAPI(BaseUrl+GetAccountPath,Parameters,Headers)

print(AccountInfo.get("TotalValue"))