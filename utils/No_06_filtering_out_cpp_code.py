from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time



def filtering_out_cpp_code(driver: WebDriver, wait: WebDriverWait[WebDriver]) -> None:
    """
    Filter out the C++ code from the daily problem page.

    Args:
        driver: The Selenium WebDriver instance.
        wait: The WebDriverWait instance.

    Returns:
        None.
    """


    # Wait until at least one span is present
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cursor-pointer")))

    # Get all clickable language spans
    language_spans = driver.find_elements(By.CSS_SELECTOR, "span.cursor-pointer")

    # Loop and click the one that says 'C++'
    for span in language_spans:
        if span.text.strip() == "C++":
            driver.execute_script("arguments[0].scrollIntoView(true);", span)
            span.click()
            break
    else:
        print("Error: C++ language span not found.")
        exit(1)

    
    # This sleep() is required for the filtered solutions to load
    # ; will fix later
    time.sleep(5)