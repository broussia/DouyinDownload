import os
import requests


def upload():
    paths = "D:/programs/lianxi/douyin/videos"
    files = os.listdir(paths)
    count = 0
    for f in files:
        file = {'files': open('D:/programs/lianxi/douyin/videos/{}'.format(f), 'rb')}
        count += 1
        response = requests.post("http://8.218.23.31:5000/v1/video/",
                                 files=file)
        print(response.text)
        # if count == 20:
        #     break


upload()

