from selenium.webdriver.common.by import By
from select_amount_module import select_amount
from platform_order_module import platform_order
import time
from selenium.webdriver import Firefox


def turbo_mood(driver:Firefox, config_dict):
    # select Turbo mood
    mood_selector = driver.find_element(By.CSS_SELECTOR,'.adaptive_selector')
    mood_selector.click()
    turbo_btn = driver.find_element(By.CSS_SELECTOR, 'button.button:nth-child(2)')
    turbo_btn.click()
            # one click switch --------
            # one_click_trade = driver.find_element(By.CSS_SELECTOR, '.toggler__invisible-checkbox')
            # one_click_trade.click()
            # confirm_one_click = driver.find_element(By.CSS_SELECTOR, 'button.button:nth-child(1)')
            # confirm_one_click.click()
    # amount of dollar ----
    select_amount(driver, config_dict['Dollar'] - 1, True)
    # added amount for back to base amount order after lose
    added_amount = 0
    # find buy and sell buttons
    buy_btn = driver.find_element(by=By.CSS_SELECTOR,
                                  value='.call-btn')
    sell_btn = driver.find_element(by=By.CSS_SELECTOR,
                                   value='.put-btn')
    # find amount of Fund
    fund = driver.find_element(by=By.CSS_SELECTOR,value='.account-panel__info-block > span:nth-child(3) > span:nth-child(1)')
    pre_fund = int(fund.text[1:])
    # base order
    base_order, compensation_order = platform_order(driver, sell_btn, buy_btn,config_dict)
    win_click = base_order if config_dict['INITIAL_ORDER'] != config_dict['LOSE_ORDER'] else compensation_order
    lose_click = compensation_order if config_dict['INITIAL_ORDER'] != config_dict['LOSE_ORDER'] else base_order
    # Loop for further orders
    wait_to_execute_order = config_dict['TURBO_ORDER_PERIOD']
    while True:
        try:
            # sleep to execute initial order
            time.sleep(wait_to_execute_order)
            try:
                # place new order ----
                if pre_fund>int(fund.text[1:]):
                    print(',,, failed -> new Lose order')
                    # change price
                    select_amount(driver, config_dict['TURBO_LOSE_Dollar'], True)
                    added_amount += config_dict['TURBO_LOSE_Dollar']
                    # put lose order and change base direction
                    pre_fund = int(fund.text[1:])
                    lose_click()
                else:
                    # position_mood == 'success'
                    print('--- success -> new Win order')
                    pre_fund = int(fund.text[1:])
                    select_amount(driver, added_amount, False)
                    added_amount = 0
                    win_click()

            except:
                # go to platform mood --------
                print('------- refresh --------')
                time.sleep(wait_to_execute_order)
                return True
        except:
            print('------- refresh --------')
            time.sleep(wait_to_execute_order)
            return True
