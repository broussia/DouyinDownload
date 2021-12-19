import os, json, requests
import pymysql


def download():
    # 请求头
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/72.0.3626.119 Safari/537.36'}

    videos_list = os.listdir('D:/programs/lianxi/douyin/json/')  # 获取文件夹内所有json包名

    count = 1  # 计数，用来作为视频名字

    for videos in videos_list:  # 循环json列表，对每个json包进行操作
        a = open('D:/programs/lianxi/douyin/json/{}'.format(videos), encoding='utf-8')  # 打开json包
        content = json.load(a)['aweme_list']  # 取出json包中所有视频

        for video in content:  # 循环视频列表，选取每个视频
            video_url = video['video']['play_addr']['url_list'][2]  # 获取视频url，每个视频有4个url，我选的第3个
            video_url = video_url.replace('https', 'http')
            # print(video_url)
            videoMp4 = requests.get(video_url, headers=headers).content  # 获取视频二进制代码
            # print('video loads success {}'.format(count))
            with open('D:/programs/lianxi/douyin/videos/{}.mp4'.format(count), 'wb') as f:  # 以二进制方式写入路径，记住要先创建路径
                f.write(videoMp4)  # 写入
                print('视频{}下载完成'.format(count))  # 下载提示
            count += 1  # 计数+1
    return


download()
