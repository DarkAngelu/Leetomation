
from typing import Dict
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from utils.No_1_driver_and_wait_setup import driver_and_wait_setup
from utils.No_2_add_cookies import add_cookies
from utils.No_3_click_daily_problem import click_daily_problem
from utils.No_4_switching_to_the_daily_problelm_tab import switching_to_the_daily_problem_tab


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



    # 3. Wait for the daily problem to be clickable and click it
    click_daily_problem(wait)


    
    # 4. Now we need to switch to the Solutions tab of the daily problem page
    switching_to_the_daily_problem_tab(driver)