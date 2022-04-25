import os
import requests


def upload():
    ip1 = "http://8.218.23.31:5000/v1/video/"
    ip2 = "http://49.235.154.162:5000/v1/video/"
    paths = "D:/programs/lianxi/douyin/videos"
    files = os.listdir(paths)
    count = 0
    for f in files:
        file = {'files': open('D:/programs/lianxi/douyin/videos/{}'.format(f), 'rb')}
        count += 1
        response = requests.post(ip2,
                                 files=file)
        print(response.text + str(count))
        # if count == 20:
        #     break


upload()

