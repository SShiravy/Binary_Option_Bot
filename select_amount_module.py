from selenium.webdriver.common.by import By


def select_amount(driver, n_click, increase):
    if n_click == 0:
        return False
    print('--> change amount of Dollar')
    if increase:
        amount_btn = driver.find_element(by=By.CSS_SELECTOR, value='button.number-input__button:nth-child(3)')
    else:
        amount_btn = driver.find_element(by=By.CSS_SELECTOR, value='button.number-input__button:nth-child(1)')
    s = 1
    for _ in range(n_click):
        amount_btn.click()
        s += 1
    print(f'-|- amount changed {s} Dollar')
