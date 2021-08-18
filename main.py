import requests
import random

randomAnimeNames = []
while len(randomAnimeNames) < 10:
    n = random.randint(1, 15000)
    response = requests.get("https://kitsu.io/api/edge/anime/" + str(n))
    if response.status_code == 200:
        try:
            randomAnimeNames.append(response.json()['data']['attributes']['titles']['en'])
        except KeyError:
            randomAnimeNames.append(response.json()['data']['attributes']['titles']['en_jp'])

print(randomAnimeNames)