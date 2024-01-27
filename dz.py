import requests
import json
import time
import csv 

url = 'https://jsonplaceholder.typicode.com/posts'
direction = f'posts/'
toload = int(input('Введите сколько постов загрузить с сервера (Больше 0): '))
loaded = 1

try:
    responce = requests.get(url=url)

    posts = json.loads(responce.text)

    print('Данные с сервера получены!')

    print('Начинаем загрузку файлов с сервера')

    for post in posts:
        if(loaded <= toload and toload > 0):

            with open(f'{direction}post_{str(loaded)}.txt', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(['User Id: ' + str(post['userId'])])
                writer.writerow(['Post Id: ' + str(post['id'])])
                writer.writerow(['Title: ' + str(post['title'])])
                writer.writerow(['Post Text: ' + str(post['body'])])

            loaded = loaded + 1
    print(f'loaded {loaded-1}/{toload} files')

            



except Exception as e:
    print(f'Code error! ({e})')
    time.sleep(5)
    exit()