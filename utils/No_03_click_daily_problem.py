from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time




def click_daily_problem(wait: WebDriverWait[WebDriver]) -> None:
    """
    Click the daily problem button on the LeetCode page.

    Args:
        wait: The WebDriverWait instance.

    Returns:
        None.
    """



    # Click the Daily Problem button
    try:
        # Find the button based on the structure, ignoring the exact text in the span
        daily_problem_button = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button/a[span]"
            ))
        )

        # This sleep() is required for the daily problem button to load
        # ; will fix later  
        time.sleep(2)

        # Click the button
        daily_problem_button.click()

    except Exception as e:
        print(f"Error clicking the daily problem button: {e}")
        exit(1)

    # Wait for the daily problem page to load
    time.sleep(5)