import requests
import os
from PIL import Image
# from pytube import YouTube
import json


def ImDownload(links, target_dir='download/imgs/'):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    for url in links:
        file_name = os.path.split(url)[1]
        img = Image.open(requests.get(url, stream = True).raw)
        img.save(f'{os.path.join(target_dir,file_name)}.{img.format.lower()}')
        print('Download is completed successfully')


with open('./data.json','r') as file:
    data = json.load(file)
    for d in data:
        for folder in data[d].keys():
            if not os.path.exists(folder):
                os.mkdir(folder)
            if not isinstance(data[d][folder], list):
                urls = [data[d][folder]]
            else:
                urls = data[d][folder]
            # print(urls[0])
            ImDownload(urls, folder)

print()
print('Complete')