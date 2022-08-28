from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Twitter_Bot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login")#https://twitter.com/i/flow/login
        time.sleep(8)
        #xpath copied by right clicking on the element and selecting "Copy XPath"
        email = bot.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(self.username)
        time.sleep(3)
        email.send_keys(Keys.RETURN)
        time.sleep(3)
        password = bot.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(self.password)
        time.sleep(2)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def like_tweet(self, search_item):
        time.sleep(3)
        bot = self.bot
        bot.get("https://twitter.com/search?q="+search_item+"&src=typed_query")
        time.sleep(5)
        for i in range(1,3):
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            tweets = bot.find_elements(By.CLASS_NAME, "css-1dbjc4n")
            links = [elem.get_attribute('data-permalink-path')for elem in tweets] # Has a error need to update this code
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    print("liked tweet")
                    time.sleep(5)
                except Exception as ex:
                    print('Did not work! Trying again in a minute')
                    time.sleep(20)
            
        
    



test = Twitter_Bot("Testing72571041", "R35409708")
test.login()
test.like_tweet("automationpython")

# copied Xpath for skip notification after login
"""
//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/span/span
"""