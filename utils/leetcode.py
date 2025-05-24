
from typing import Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from utils.No_1_driver_and_wait_setup import driver_and_wait_setup
from utils.No_2_add_cookies import add_cookies


def do_daily(cookies: Dict[str, str] = {}) -> None:
    """
    Perform the daily problem on LeetCode.

    Args:
        cookies: A dictionary of cookies to add. The keys are cookie names,
                 and the values are cookie values (both strings).
                 Default is an empty dictionary.

    Returns:
        None.
    """

    
    # 1. Setup the driver and wait objects
    driver, wait = driver_and_wait_setup()


    # 2. Add cookies to the driver and navigate to the /problemset/all/ page
    add_cookies(driver, cookies)