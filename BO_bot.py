import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from select_asset_module import select_asset
from config import PAGE_DELAY, ELEMENT_DELAY, MAX_STACK_ORDERS, ORDER_PERIOD, Dollar
from select_timeframe_module import select_timeframe
from platform_order_module import platform_order
from terminate_module import crash_and_close


def run_bot(driver: Firefox):
    try:
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
        time.sleep(ELEMENT_DELAY)
        # choose symbol ----
        select_asset(driver)
        # choose timeframe ----
        select_timeframe(driver)
        # amount of dollar ----
        print('--> change amount of Dollar')
        amount_of_order = driver.find_element(by=By.CSS_SELECTOR, value='button.number-input__button:nth-child(3)')
        for _ in range(Dollar-1):
            amount_of_order.click()
        print(f'-|- put ${Dollar} in each trade')
        # find buy and sell buttons
        buy_btn = driver.find_element(by=By.CSS_SELECTOR,
                                      value='.call-btn')
        sell_btn = driver.find_element(by=By.CSS_SELECTOR,
                                       value='.put-btn')
        base_order, compensation_order = platform_order(driver, sell_btn, buy_btn)
        # Loop for further orders
        stack_of_orders = MAX_STACK_ORDERS
        while True:
            try:
                # sleep and refresh -----
                time.sleep(ORDER_PERIOD)

                stack_of_orders -= 1
                if stack_of_orders < 0:
                    base_order, compensation_order = platform_order(driver, sell_btn, buy_btn)
                    stack_of_orders = MAX_STACK_ORDERS
                    continue

                # place stack of orders ---------
                position = driver.find_element(By.XPATH,
                                               value='/html/body/div/div/div/div/section/div/div[4]/div[2]/div[1]/div[1]/div/ul/li/div[1]/div/div[2]/span[1]/span')
                try:
                    # find last opened position
                    position_mood = position.get_attribute('class').split('_')[-1]
                    # place new order ----
                    if position_mood == 'success':
                        base_order()
                        print('--- success -> new order in pre direction')
                    elif position_mood == 'alert':
                        compensation_order()
                        print(',,, failed -> new order in opp direction')
                        k = base_order
                        base_order = compensation_order
                        compensation_order = k
                    else:
                        # go to platform mood --------
                        base_order, compensation_order = platform_order(driver, sell_btn, buy_btn)
                        continue
                except:
                    # go to platform mood --------
                    base_order, compensation_order = platform_order(driver, sell_btn, buy_btn)
            except:
                print('------- refresh --------')
                return True
    except:
        return False

