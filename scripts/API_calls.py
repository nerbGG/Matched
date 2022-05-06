import http.client
from json import dumps
import json
def getSport(sport):
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com/v2/",
        'x-rapidapi-key': "091af43047177809fa22fb38cfcecd4d"
        }

    conn.request("GET", "/leagues?country=Germany", headers=headers)

    res = conn.getresponse()
    # data = res.read()
    data_json = json.load(res)
    print(data_json)


def run():
    getSport("soccer")