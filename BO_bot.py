import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from select_asset_module import select_asset
from config import Initial_Order, PAGE_DELAY, ELEMENT_DELAY
from select_timeframe_module import select_timeframe


def run_bot(driver: Firefox):
    # GO to BO page
    driver.get('https://my.alpariforex.org/fa/platforms/fix-contractstrader/')
    # wait to load page
    WebDriverWait(driver, PAGE_DELAY).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/div/div[1]/div[3]')))
    time.sleep(ELEMENT_DELAY)
    driver.switch_to.frame("mainFrame")
    # wail to load main frame
    time.sleep(3)
    # choose symbol ----
    select_asset(driver)
    # choose timeframe ----
    select_timeframe(driver)
    # confirm initial order
    buy_btn = driver.find_element(by=By.CSS_SELECTOR,
                                  value='.call-btn')
    sell_btn = driver.find_element(by=By.CSS_SELECTOR,
                                   value='.put-btn')
    if Initial_Order == 'sell':
        sell_btn.click()
    else:
        buy_btn.click()
    confirm_btn = driver.find_element(by=By.CSS_SELECTOR,
                                      value='.primary-button')
    # put an order
    # confirm_btn.click()

    # driver.refresh()
    # Loop for further orders
