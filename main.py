# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium.webdriver import Firefox
from login_module import logging
from BO_bot import run_bot
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = Firefox()
    login_res = logging(driver)
    run_bot(driver)

    # driver.close()
    # driver.quit()
