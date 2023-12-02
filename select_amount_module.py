from selenium.webdriver.common.by import By
from config import Dollar


def select_amount(driver,n_click,increase):
    print('--> change amount of Dollar')
    if increase:
        amount_btn = driver.find_element(by=By.CSS_SELECTOR, value='button.number-input__button:nth-child(3)')
    else:
        amount_btn = driver.find_element(by=By.CSS_SELECTOR, value='button.number-input__button:nth-child(1)')

    for _ in range(n_click):
        amount_btn.click()

    print(f'-|- put ${Dollar} in each trade')