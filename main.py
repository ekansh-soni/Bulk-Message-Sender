from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

with open("mess.txt", "r") as file:
    msg = file.read()

# print(quote(msg))
msg = quote(msg)

 
numbers = []
with open('numbers.txt', 'r') as file:
    for num in file.readlines():
        numbers.append(num.rstrip())

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(15)  #login ScreenTime is 15 Sec in which user can login 

for num in numbers:
    link2 = f'https://web.whatsapp.com/send?phone=91{num}&text={msg}'
    driver.get(link2)
    time.sleep(5) # user msg display screen time in which sender can see msg in msg box for 5 sec
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(1) #msg Automatically send in every single second

time.sleep(2000)


#Made By Ekansh
