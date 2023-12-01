from selenium.webdriver.common.by import By
from terminate_module import crash_and_close
from config import TIMEFRAME


def select_timeframe(driver):
    print('-->> selecting timeframe')
    # select timeframe menu
    timeframe_btn = driver.find_element(By.CSS_SELECTOR,
                        value='.time-frame-selector > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)')
    timeframe_btn.click()
    timeframe_menu = driver.find_element(By.CSS_SELECTOR, value='.bali-select-field__menu')
    # find all timeframe and select one
    all_timeframes = timeframe_menu.find_elements(By.CLASS_NAME, value='time-frame-menu__item')
    # interpret timeframe text
    if TIMEFRAME[-1] == 's':
        unit = 'ثانیه'
    elif TIMEFRAME[-1] == 'm':
        unit = 'دقیقه'
    elif TIMEFRAME[-1] == 'h':
        unit = 'ساعت'
    else:
        # crash
        crash_and_close(driver,f'wrong unit {TIMEFRAME[-1]}')

    for timeframe in all_timeframes:
        timeframe_text = timeframe.text
        n,u = timeframe_text.split()
        if u == unit and n == TIMEFRAME[:-1]:
            timeframe.click()
            selected_timeframe = timeframe_btn.find_element(By.CLASS_NAME, value='value-display-control__value').text
            if selected_timeframe == timeframe_text:
                print('-|- timeframe selected')
                # END OF PROGRAM ---
                return True

            else:
                # crash
                break
    # if still function running :
    crash_and_close(driver, 'there is no such timeframe')





