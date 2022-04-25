import pymysql
import requests
import time


def download():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/72.0.3626.119 Safari/537.36'}
    douyin_data = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        charset="utf8mb4",
        database="douyindata"
    )
    count = 1
    
    sql = 'select Url,title,ID from douyindata.videos where download = false'
    cursor = douyin_data.cursor()
    cursor.execute(sql)
    videos = cursor.fetchall()
    for video in videos:
        print(video[0])
        videoMp4 = requests.get(video[0], headers=headers).content  # 获取视频二进制代码
        title = str(video[1]).replace('/', '')  # 防止名称中的/被误认为目录分割符
        title = title.replace('*', '')
        title = title.replace('"', '')
        title = title.replace('\\', '')
        title = title.replace('?', '')
        title = title.replace('<', '')
        title = title.replace('>', '')
        title = title.replace('|', '')
        title = title.replace(':', '')
        try:
            with open('D:/programs/lianxi/douyin/videos/{}.mp4'.format(title), 'wb') as f:  # 以二进制方式写入路径，记住要先创建路径
                f.write(videoMp4)  # 写入
            print('视频{}下载完成\n'.format(count))  # 下载提示
            sql2 = 'update videos set download = true where ID = {}'.format(video[2])
            # print(sql2)
            cursor.execute(sql2)
            cursor.connection.commit()
        except:
            print('视频{}下载失败\n'.format(count))
            pass
        count += 1  # 计数+1


download()
