from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

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
        print("Clicked Daily Problem button.")
    except Exception as e:
        print("Could not click Daily Problem button:", e)
        exit(1)

    # Wait for the daily problem page to load
    time.sleep(5)