import math
import time
from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from platform_order_module import platform_order
from select_amount_module import select_amount


def multi_input_mood(driver: Firefox, config_dict, fund):
    print('|| 36 input mood started')
    # find buy and sell buttons
    buy_btn = driver.find_element(by=By.CSS_SELECTOR,
                                  value='.call-btn')
    sell_btn = driver.find_element(by=By.CSS_SELECTOR,
                                   value='.put-btn')
    # base order
    base_order, compensation_order = platform_order(driver, sell_btn, buy_btn, config_dict)
    wait_to_execute_order = config_dict['TURBO_ORDER_PERIOD']
    # put initial order until lose
    while True:
        print('--- new base order')
        pre_fund = int(fund.text[1:])
        # sleep to execute order
        time.sleep(wait_to_execute_order)
        new_fund = int(fund.text[1:])
        # check for lose
        if new_fund < pre_fund:
            break
        base_order()
    # after lose, put opposite then initial order repeatedly
    # Start 36 order --------------
    print(',,, lose -> start 36 orders')
    delay = wait_to_execute_order
    lot = config_dict['Dollar']
    next_order = compensation_order
    i = 1
    for delay_multiplier, lot_multiplier in zip(config_dict['Time_multipliers'], config_dict['Lot_multipliers']):
        # change lot and delay and handle the max condition ---------------
        delay = min(math.ceil(delay * delay_multiplier), config_dict['Max_Time'])
        lot = min(math.ceil(lot * lot_multiplier), config_dict['Max_Lot'])
        # sleep to execute order
        print(f'*** delay:{delay}')
        time.sleep(delay)
        # is page still there ? -------------
        try:
            # find amount of order
            order_amount = driver.find_element(by=By.CSS_SELECTOR, value='.number-input__field')
            # increase order lot
            pre_amount = int(order_amount.get_property('value'))
            select_amount(driver, abs(lot - pre_amount), lot - pre_amount > 0)
            print(f'*** lot:{lot}')
        except:
            # refresh BO page
            print('----- return to platform -----')
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
            # increase order lot
            select_amount(driver, lot - 1, True)
            print(f'*** lot:{lot}')
        # go to next order
        print(f'--- {i}th order from 36')
        next_order()
        next_order = base_order if next_order == compensation_order else compensation_order
        i += 1

    return True
