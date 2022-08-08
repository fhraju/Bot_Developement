from selenium import webdriver
from time import sleep
import json
import os

def Facebook(usr,pwd,path,desc,speed):
    if usr:
        driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        #<--- code to login --->
        driver.get('https://en-gb.facebook.com/login')
        usr_box = driver.find_element_by_id('email')
        usr_box.send_keys(usr)
        pwd_box = driver.find_element_by_id('pass')
        pwd_box.send_keys(pwd)
        login_button = driver.find_element_by_id('loginbutton')
        login_button.submit()
        #<--- / code to login --->
        #Wait until login
        sleep(speed*4)
        remover = driver.find_element_by_tag_name('body').click()
        # remover = driver.find_element_by_tag_name('body').click()
        # # sleep(speed*2)
        #<--- code to remove opaque screen --->
        # remover = driver.find_element_by_tag_name('body').click()
        # # remover = driver.find_element_by_tag_name('body').click()
        #<--- / code to remove opaque screen --->
        #WALL
        give = driver.find_element_by_xpath("//*[@name='xhpc_message']")
        #Wait for wall
        sleep(speed)

        #DESCRIPTION
        give.send_keys(desc)
        sleep(speed)

        #ATTACH MEDIA
        # file = driver.find_element_by_xpath('//input[@data-testid="media-sprout"]')
        file = driver.find_element_by_css_selector('input[data-testid="media-sprout"]')
        sleep(speed)

        #sending media
        file.send_keys(path)
        #wait while it uploads
        sleep(speed*3)

        #POST
        post = driver.find_element_by_css_selector('button[data-testid="react-composer-post-button"]')
        post.click()
        #wait for post to be made
        sleep(speed*5)
        driver.refresh()
        driver.close()
        # faceDone = 1
        return 1
    pass
