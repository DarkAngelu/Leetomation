from selenium.webdriver.remote.webdriver import WebDriver
from typing import Dict

import time


def add_cookies(driver: WebDriver, cookies: Dict[str, str]) -> None:
    """
    Add cookies to the Selenium driver.

    Args:
        driver: The Selenium WebDriver instance.
        cookies: A dictionary of cookies to add. The keys are cookie names,
                 and the values are cookie values (both strings).

    Returns:
        None.
    """
    
    # Navigate to LeetCode
    driver.get("https://leetcode.com")

    # Add cookies to the driver
    for name, value in cookies.items():
        driver.add_cookie({
            'name': name,
            'value': value,
            'domain': '.leetcode.com',
            'path': '/',
            'secure': True,
            'httpOnly': False
        })

    # Go to problemset page
    driver.get("https://leetcode.com/problemset/all/")

    ## This sleep() is required for rendering of whole page
    #  ; will fix later
    time.sleep(5)
