
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from utils.driver_and_wait_setup import driver_and_wait_setup


def do_daily(cookies):
    # Setup the driver and wait objects
    driver, wait = driver_and_wait_setup()


    