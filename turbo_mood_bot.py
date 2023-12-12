from selenium.webdriver.common.by import By
from select_amount_module import select_amount
from platform_order_module import platform_order
from selenium.webdriver import Firefox
import time
from select_asset_module import select_asset


def turbo_mood(driver: Firefox, config_dict):
    # select Turbo mood
    mood_selector = driver.find_element(By.CSS_SELECTOR, '.adaptive_selector')
    mood_selector.click()
    mood_menu = driver.find_element(By.CLASS_NAME, 'button-group_adaptive')
    mood_btns = mood_menu.find_elements(By.CLASS_NAME, 'button')
    {mood.text: mood for mood in mood_btns}['توربو'].click()
    # one click switch --------
    # one_click_trade = driver.find_element(By.CSS_SELECTOR, '.toggler__invisible-checkbox')
    # one_click_trade.click()
    # confirm_one_click = driver.find_element(By.CSS_SELECTOR, 'button.button:nth-child(1)')
    # confirm_one_click.click()
    # amount of dollar ----
    select_amount(driver, config_dict['Dollar'] - 1, True)
    # choose symbol ----
    select_asset(driver, config_dict)
    # find buy and sell buttons
    buy_btn = driver.find_element(by=By.CSS_SELECTOR,
                                  value='.call-btn')
    sell_btn = driver.find_element(by=By.CSS_SELECTOR,
                                   value='.put-btn')
    # find amount of Fund
    fund = driver.find_element(by=By.CSS_SELECTOR,
                               value='.account-panel__info-block > span:nth-child(3) > span:nth-child(1)')
    pre_fund = int(fund.text[1:])
    # find amount of Order
    order_amount = driver.find_element(by=By.CSS_SELECTOR, value= '.number-input__field')
    # base order
    base_order, compensation_order = platform_order(driver, sell_btn, buy_btn, config_dict)
    win_click = base_order
    lose_click = compensation_order if config_dict['INITIAL_ORDER'] != config_dict['LOSE_ORDER'] else base_order
    # Loop for further orders
    wait_to_execute_order = config_dict['TURBO_ORDER_PERIOD']
    while True:
        try:
            # sleep to execute initial order
            time.sleep(wait_to_execute_order)
            new_fund = int(fund.text[1:])
            # place new order ----
            if pre_fund > new_fund:
                print(',,, failed -> new Lose order')
                # change price
                clicks_amount = round(int(order_amount.get_property('value')) * config_dict['TURBO_LOSE_Dollar']) - int(order_amount.get_property('value'))
                select_amount(driver, clicks_amount, True)
                # put lose order and change base direction
                pre_fund = new_fund
                lose_click()
            else:
                # position_mood == 'success'
                print('--- success -> new Win order')
                pre_fund = new_fund
                clicks_amount = int(order_amount.get_property('value')) - config_dict['Dollar']
                select_amount(driver, clicks_amount, False)
                win_click()

        except:
            print('------- refresh --------')
            time.sleep(wait_to_execute_order)
            return True
