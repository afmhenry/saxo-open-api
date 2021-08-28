import requests
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date, timedelta


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

#AccountInfo = getAPI(BaseUrl+GetAccountPath,Parameters,Headers)
#print(AccountInfo.get("TotalValue"))

GetAccountHistoryPath = "/hist/v3/accountvalues/"+ClientKey

MockParam = {"MockDataId":"001"}
AccountHistory = getAPI(BaseUrl+GetAccountHistoryPath,MockParam,Headers).get("Data")

today = date.today()
lastMonth = today - timedelta(days=30)
lastYear = today - timedelta(days=365)

for account in AccountHistory:
    values =  [account["AccountValue"],account["AccountValueMonth"],account["AccountValueYear"]]
    dates = [lastYear, lastMonth, today]
    plt.plot(dates,values)
plt.show()
exit()

