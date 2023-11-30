import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from config import Initial_Order,PAGE_DELAY,ELEMENT_DELAY


def run_bot(driver: Firefox):
    # GO to BO page
    driver.get('https://my.alpariforex.org/fa/platforms/fix-contractstrader/')
    # wait to load page
    WebDriverWait(driver, PAGE_DELAY).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/div/div[1]/div[3]')))
    # wail to load main frame
    time.sleep(ELEMENT_DELAY)
    driver.switch_to.frame("mainFrame")

    asset_btn = WebDriverWait(driver, PAGE_DELAY).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             '.asset-selector > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')))
    print('main Frame Loaded')
    # Check assets list
    # TODO: Find available symbols list and select one
    asset_btn.click()
    # all_assets_menu = driver.find_element(By.CSS_SELECTOR, value='.asset-selector > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)')
    # all_assets_col = all_assets_menu.find_elements(By.CLASS_NAME, value='menu-item')
    # print([item.text for item in all_assets_col])

    time.sleep(5)

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
