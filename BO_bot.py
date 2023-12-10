import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from base_mood_bot import base_mood
from turbo_mood_bot import turbo_mood
from terminate_module import crash_and_close


def run_bot(driver: Firefox,config_dict):
    # GO to BO page
    driver.get('https://my.alpariforex.org/fa/platforms/fix-contractstrader/')
    # wait to load page
    WebDriverWait(driver, config_dict['PAGE_DELAY']).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/div/div[1]/div[3]')))
    time.sleep(config_dict['ELEMENT_DELAY'])
    driver.switch_to.frame("mainFrame")
    # wail to load main frame
    time.sleep(config_dict['ELEMENT_DELAY'])
    mood = input('Enter 1 for Call/Put , 2 for Turbo mood:')
    if mood == '1':
        print('#### script started ####')
        base_mood(driver,config_dict)
    elif mood == '2':
        print('#### script started ####')
        turbo_mood(driver,config_dict)
    else:
        crash_and_close(driver,'wrong input mood')
