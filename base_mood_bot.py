from selenium.webdriver.common.by import By
from select_amount_module import select_amount
from select_asset_module import select_asset
from select_timeframe_module import select_timeframe
from platform_order_module import platform_order
import time


def base_mood(driver, config_dict):
    # choose symbol ----
    select_asset(driver, config_dict)
    # choose timeframe ----
    wait_to_execute_order = select_timeframe(driver, config_dict)
    # amount of dollar ----
    select_amount(driver, config_dict['Dollar'] - 1, True)
    clicks_amount = config_dict['Dollar']
    # find buy and sell buttons
    buy_btn = driver.find_element(by=By.CSS_SELECTOR,
                               value='.call-btn')
    sell_btn = driver.find_element(by=By.CSS_SELECTOR,
                                   value='.put-btn')
    base_order, compensation_order = platform_order(driver, sell_btn, buy_btn,config_dict)
    # Loop for further orders
    stack_of_orders = config_dict['MAX_STACK_ORDERS']
    while True:
        try:
            # sleep and refresh -----
            time.sleep(config_dict['ORDER_PERIOD'])
            stack_of_orders -= 1
            if stack_of_orders < 0:
                # return True to refresh and back to platform
                time.sleep(wait_to_execute_order)
                print('----- return to platform -----')
                return True

            # place stack of orders ---------
            position = driver.find_element(By.XPATH,
                                           value='/html/body/div/div/div/div/section/div/div[4]/div[2]/div[1]/div[1]/div/ul/li/div[1]/div/div[2]/span[1]/span')
            try:
                # find last opened position
                position_mood = position.get_attribute('class').split('_')[-1]
                # place new order ----
                if position_mood == 'alert':
                    print(',,, failed -> new order in opp direction')
                    # double price
                    select_amount(driver, clicks_amount, True)
                    clicks_amount *= 2
                    # put opposite order and change base direction
                    compensation_order()
                    k = base_order
                    base_order = compensation_order
                    compensation_order = k
                else:
                    # position_mood == 'success'
                    base_order()
                    print('--- success -> new order in pre direction')

            except:
                # go to platform mood --------
                print('------- refresh --------')
                time.sleep(wait_to_execute_order)
                return True
        except:
            print('------- refresh --------')
            time.sleep(wait_to_execute_order)
            return True
