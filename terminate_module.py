import sys
from time import sleep


def crash_and_close(driver, msg):
    print('|********** ERROR: '+msg+' **********|')
    print('------- PROGRAM TERMINATED -------')
    sleep(5)
    # driver.close()
    # driver.quit()
    sys.exit()
