import requests
from time import sleep
from datetime import datetime
import urllib3

def get_match():
    return requests.get(
        url= "https://temporeal.lance.com.br/storage/matches/copa-do-mundo-2022-27-11-2022-espanhaxalemanha.json"
    ).json()

# print(get_match())

getMatchJsonStats = get_match()
getMatchJsonStats1 = getMatchJsonStats['match']['team_a']['players']
getMatchJsonStats2 = getMatchJsonStats1[1]
getMatchJsonStats3 = getMatchJsonStats2['name']
print(getMatchJsonStats3)

last_update = None

while True:
    match_data = get_match()

    narracao = match_data['match']['narrations']
    last_narration = narracao[len(narracao) - 1]
    last_narration_time = datetime.strptime(last_narration['created_at'], '%Y-%m-%dT%H:%M:%S.000000Z')

    if (not last_update) or (last_narration_time > last_update):
        last_update = last_narration_time
        last_narration_moment = narracao[len(narracao) - 1]['moment']
        last_narration_text = narracao[len(narracao) - 1]['text']
        print(f'.\n.\n.\n{last_narration_moment} - {last_narration_text}')

    sleep(30)