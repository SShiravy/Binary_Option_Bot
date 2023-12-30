from selenium.webdriver.common.by import By
from terminate_module import crash_and_close


def platform_order(driver, sell_btn, buy_btn,config_dict):
    print('-->> working on platform orders')
    if config_dict['INITIAL_ORDER'] == 'sell':
        initial_order = sell_btn
        other_order = buy_btn

    else:
        initial_order = buy_btn
        other_order = sell_btn

    def base_order():
        initial_order.click()
        confirm_btn = driver.find_element(by=By.CSS_SELECTOR,
                                          value='.primary-button')
        confirm_btn.click()
        #crash_and_close(driver,"Can not place order")

    def compensation_order():
        try:
            other_order.click()
            confirm_btn = driver.find_element(by=By.CSS_SELECTOR,
                                              value='.primary-button')
            confirm_btn.click()
        except:
            crash_and_close(driver, "Can not place order")

    # confirm initial order ----
    base_order()
    print('-|- Platform order placed')
    return base_order, compensation_order
