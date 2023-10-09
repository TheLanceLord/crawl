import time
import os
import uuid
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

# Add a random delay to the start so we don't overload the server all at once
delay = random.randint(0, 600)
time.sleep(delay)

# Set and fetch the variables we will need.
unique_id = str(uuid.uuid4()).replace('-', '')[0:20]
LOADBALANCER_IP = os.getenv('LOADBALANCER_IP')
address = 'http://' + LOADBALANCER_IP
play_url = address + '/#play-dcss-web-trunk'
print(unique_id)

# Setup our test to be headless so it runs without trying to open the
# Chrome GUI
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

# Navigate to the dungeon crawl stone soup site and register our account
driver.get(address)
time.sleep(10)
driver.find_element(By.ID, "reg_link").click()
time.sleep(20)
driver.find_element(By.ID, "reg_username").send_keys(unique_id)
driver.find_element(By.ID, "reg_password").send_keys(unique_id)
driver.find_element(By.ID, "reg_repeat_password").send_keys(unique_id)
driver.find_element(By.ID, "reg_submit").click()
time.sleep(20)

# Play games forever
while True:
    driver.get(play_url)
    time.sleep(15)
    try:
        Alert(driver).accept()
    except:
        time.sleep(2)
        continue

    # Choose a random character with the '!' key, then confirm the character
    # with 'Y'
    time.sleep(15)
    ActionChains(driver).send_keys("!").perform()
    time.sleep(5)
    ActionChains(driver).send_keys("Y").perform()
    time.sleep(5)

    # Take the recommended weapon with the '+' key
    ActionChains(driver).send_keys("+").perform()
    time.sleep(5)
    ActionChains(driver).send_keys(Keys.RETURN).perform()
    time.sleep(5)

    # Spam the 'o', TAB, and '.' keys to play the game and the 'S' and RETURN
    # keys for level ups
    for n in range(0, 50):
        ActionChains(driver).send_keys("o").perform()
        time.sleep(1)
        ActionChains(driver).send_keys(Keys.TAB).perform()
        time.sleep(1)
        ActionChains(driver).send_keys(".").perform()
        time.sleep(1)
        ActionChains(driver).send_keys("S").perform()
        time.sleep(1)
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        time.sleep(1)
