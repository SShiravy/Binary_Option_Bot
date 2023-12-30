# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium.webdriver import Firefox
from login_module import logging
from BO_bot import run_bot
from terminate_module import crash_and_close


def read_config(path):
    print('-->> reading config.txt')
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            values = [line.split("'")[1] for line in lines]
        lot_multipliers_list = [float(lot) for lot in values[12][1:-1].split(',')]
        time_multipliers_list = [float(lot) for lot in values[13][1:-1].split(',')]
        config_dict = {
            'PAGE_DELAY': int(values[0]),
            'ELEMENT_DELAY': int(values[1]),
            'SYMBOL': str(values[2]),
            'TIMEFRAME': str(values[3]),
            'Dollar': int(values[4]),
            'ORDER_PERIOD': int(values[5]),
            'MAX_STACK_ORDERS': int(values[6]),
            'INITIAL_ORDER': str(values[7]),
            'LOSE_ORDER': str(values[8]),
            'TURBO_ORDER_PERIOD': int(values[9]),
            'TURBO_LOSE_Dollar': float(values[10]),
            '36INPUT_MOOD': True if values[11] == 'ON' else False,
            'Lot_multipliers': lot_multipliers_list,
            'Time_multipliers': time_multipliers_list,
            'Max_Lot': int(values[14]),
            'Max_Time': int(values[15])
        }
        print('-|- reading configs complete')
        return config_dict
    except:
        crash_and_close(0, f'wrong config.txt')
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # read settings from config.txt
    config_dict = read_config('config.txt')
    # log in fields ----
    # LOGIN_NUMBER_or_EMAIL = input('Enter Email or Number:')
    # LOGIN_PASSWORD = input('Enter Password:')
    # config_dict['LOGIN_NUMBER_or_EMAIL'] = LOGIN_NUMBER_or_EMAIL
    # config_dict['LOGIN_PASSWORD'] = LOGIN_PASSWORD
    print('## opening Firefox browser')
    driver = Firefox()
    login_res = logging(driver,config_dict)
    # start bot
    run_bot(driver,config_dict)
