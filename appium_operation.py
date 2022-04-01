from appium import webdriver
from appium.webdriver.common.appiumby import By
import time
import requests


def operation():
    desired_caps = {
        'platformName': 'Android',  # 被测手机是安卓
        'platformVersion': '5.1.1',  # 手机安卓版本
        'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
        'appPackage': 'com.ss.android.ugc.aweme',  # 启动APP Package名称
        'appActivity': '.main.MainActivity',  # 启动Activity名称
        'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
        'resetKeyboard': True,  # 执行完程序恢复原来输入法
        'noReset': True,  # 不要重置App
        'newCommandTimeout': 6000,
        'automationName': 'UiAutomator2'
        # 'app': r'd:\apk\bili.apk',
    }

    # 从服务器中获得用户的ID
    response = requests.get("http://10.3.200.45:5000/v1/douyinID/send")
    douyinID = response.text.split('"')[3]

    # 连接Appium Server，初始化自动化环境
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 设置缺省等待时间
    driver.implicitly_wait(100)

    # 根据id定位搜索位置框，点击
    # driver.find_element(By.ID, 'lg4') .click()

    # 单击搜素按钮，进入搜素界面，搜索 ‘f1’之后进入第一个用户的主页，上滑若干次
    # search =
    # douyinID = "f1"
    driver.find_element(By.ID, 'com.ss.android.ugc.aweme:id/d+r').click()
    driver.find_element(By.ID, 'com.ss.android.ugc.aweme:id/et_search_kw').send_keys(douyinID)
    driver.find_element(By.ID, 'com.ss.android.ugc.aweme:id/k4g').click()
    # time.sleep(5)
    # driver.tap([(507, 191)], 10)
    code1 = 'new UiSelector().text("用户").resourceId("android:id/text1")'
    driver.find_element_by_android_uiautomator(code1).click()
    code2 = 'new UiSelector().descriptionContains("F1世界锦标赛官方账号")'
    code3 = 'new UiSelector().resourceId("com.ss.android.ugc.aweme:id/akl")'
    driver.find_element_by_android_uiautomator(code3).click()
    for i in range(20):
        driver.swipe(900, 1575, 900, 400, 800)
        time.sleep(1)
    # //androidx.appcompat.app.a.b[3]
    # input('**** Press to quit..')
    driver.quit()
    return


operation()
