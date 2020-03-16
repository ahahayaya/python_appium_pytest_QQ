from time import sleep
from appium import webdriver
def get_driver():
    desired_caps = {}
    desired_caps['deviceName'] = "xx"
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['appPackage'] = 'com.tencent.mobileqq'
    desired_caps['appActivity'] = '.activity.SplashActivity'
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)