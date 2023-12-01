from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from crash_module import crash_and_close
from config import PAGE_DELAY, SYMBOL


def select_asset(driver):
    print('-->> selecting symbol')
    # check the asset btn
    asset_btn = WebDriverWait(driver, PAGE_DELAY).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             '.asset-selector > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')))
    asset_btn.click()
    # select asset menu
    assets_menu = driver.find_element(By.CSS_SELECTOR,
                                      value='.asset-selector > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)')
    # find all assets and select one
    all_assets = assets_menu.find_elements(By.CLASS_NAME, value='menu-item')
    all_assets_dict = {item.text: item for item in all_assets}
    try:
        all_assets_dict[SYMBOL].click()
    except:
        # crash
        crash_and_close(driver, 'there is no such symbol')
    selected_asset = asset_btn.find_element(by=By.CLASS_NAME, value='value-display-control__value').text
    if selected_asset == SYMBOL:
        print('-|- symbol selected')
    else:
        # crash
        crash_and_close(driver, f'the "{SYMBOL}" symbol is unavailable')

