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
            try:
                randomAnimeNames.append(response.json()['data']['attributes']['titles']['en_jp'])
            except KeyError:
                pass

mode = input("Write 1 for write-to-file mode, any other key for print only:")

if mode == '1':
    f = open("C:\\Users\\Ivo\\Documents\\Python\\RandomAnimeListPy\\RandomAnimeList.txt", "a")
    for i in randomAnimeNames:
        f.write(i)
        f.write("\n")
    f.close()

print(randomAnimeNames)