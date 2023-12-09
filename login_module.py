from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from terminate_module import crash_and_close


def logging(driver,config_dict):
    driver.get('https://alpariforex.org/fa/login/')
    print('-->> logging in')
    # # filling
    # login_email = driver.find_element(by=By.NAME, value='authorization_login')
    # login_email.send_keys(config_dict['LOGIN_NUMBER_or_EMAIL'])
    #
    # login_pass = driver.find_element(by=By.NAME, value='authorization_password')
    # login_pass.send_keys(config_dict['LOGIN_PASSWORD'])
    # captcha --------------
    # find it
    # captcha = WebDriverWait(driver, config_dict['ELEMENT_DELAY']).until(
    #     EC.presence_of_element_located(
    #         (By.CSS_SELECTOR,
    #          '.geetest_radar_tip')))
    # if captcha != None:
    #     captcha.click()
    #
    # # click on login button
    # login_btn = driver.find_element(by=By.XPATH,
    #                                    value='/html/body/div[1]/div/div[1]/div/div/div[4]/div[1]/div[4]/button')
    # login_btn.click()

    # try:
    #     WebDriverWait(driver, config_dict['PAGE_DELAY']*2).until(
    #         EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/div[2]/div/div[7]/ul/li[3]/a'))
    #     )
    # except:
    #     # crash
    #     crash_and_close(driver,'log in Failed')
    # else:
    #     print('-|- Bot is in now')
    #     return True
    input('login and when page fully loaded, hit Enter hire:')
    return True
