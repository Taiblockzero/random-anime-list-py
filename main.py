import gtts
import requests
import random
from gtts import gTTS
import os

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

mode = input("Write 1 for write-to-file mode, 2 for english tts mode, 3 for japanese tts mode, any other key for print only:")

if mode == '1':
    f = open("C:\\Users\\Ivo\\Documents\\Python\\RandomAnimeListPy\\RandomAnimeList.txt", "a")
    for i in randomAnimeNames:
        f.write(i)
        f.write("\n")
    f.close()

if mode == '2':
    listStr = ','.join(randomAnimeNames)
    myobj = gTTS(text=listStr, lang="en", slow=False)
    myobj.save("C:\\Users\\Ivo\\Documents\\Python\\RandomAnimeListPy\\tts.mp3")

if mode == '3':
    listStr = ','.join(randomAnimeNames)
    myobj = gTTS(text=listStr, lang="ja", slow=False)
    myobj.save("C:\\Users\\Ivo\\Documents\\Python\\RandomAnimeListPy\\tts.mp3")

print(randomAnimeNames)