import json
import pymysql
import os
import time


def save_in_database():
    videos_list = os.listdir('D:/programs/lianxi/douyin/json/')  # 获取文件夹内所有json包名
    count = 1
    douyin_data = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="Qilei990406!",
        charset="utf8mb4",
        database="douyindata"
    )
    cursor = douyin_data.cursor()
    for videos in videos_list:
        a = open('D:/programs/lianxi/douyin/json/{}'.format(videos), encoding='utf-8')  # 打开json包
        content = json.load(a)['aweme_list']  # 取出json包中所有视频
        for video in content:  # 循环视频列表，选取每个视频
            video_url = video['video']['play_addr']['url_list'][2]  # 获取视频url，每个视频有4个url，我选的第3个
            video_url = video_url.replace('https', 'http')
            video_ID = video['aweme_id']  # 获取视频内部ID
            video_getTime = str(time.time())[:10]
            video_title = video['desc']
            # print(video_title)
            # print("now link is " + str(count))
            print(count)
            count += 1
            sql = 'insert into douyindata.videos (ID,Url,addTime,title) values ({},\'{}\',{},\'{}\')'.format(video_ID, video_url,
                                                                                                video_getTime, video_title)
            # print(sql)
            # cursor.execute(sql)
            try:
                cursor.execute(sql)

            except:
                print(video_ID + '重复')
                pass
    cursor.connection.commit()
    cursor.close()
    douyin_data.close()


save_in_database()