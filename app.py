import sys
import os 
import time
import eel
import datetime
from selenium import webdriver

eel.init('web')

@eel.expose
def sendDataToPy(rcname,tm,msg):
    print("[Info] Message Scheduled for {} at {}".format(rcname,tm))
    browser = webdriver.Chrome("./chromedriver")
    browser.get("https://web.whatsapp.com/")
    time.sleep(3)
    wait = True
    while wait == True:
        if tm != str(datetime.datetime.now().time())[0:5]:
            wait=True
        else:
            wait=False

    browser.find_element_by_xpath("//span[@title='{}']".format(rcname)).click()
    browser.find_element_by_xpath("//div[@class='_3uMse']").send_keys(msg)
    browser.find_element_by_xpath("//button[@class='_1U1xa']").click()
    browser.close()

if __name__=="__main__":
    eel.start("index.html",size=(500,300))