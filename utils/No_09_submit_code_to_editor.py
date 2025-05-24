from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time



def submit_code_to_editor(driver: WebDriver, wait: WebDriverWait[WebDriver], cpp_code: str) -> None:    
    """
    Submit the code to the Monaco editor on the daily problem page.

    Args:
        driver: The Selenium WebDriver instance.

    Returns:
        None.
    """



    # Now we need to submit the code to the Editor on the daily problem page

    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "monaco-editor"))
    )

    driver.execute_script(f"""
        var editor = monaco.editor.getModels()[0];
        editor.setValue(`{cpp_code}`);
    """)


    # Wait for the submit button to be clickable

    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-e2e-locator="console-submit-button"]'))
    )

    # Click the submit button
    submit_button.click()


    # This sleep() is required for the submission to complete
    time.sleep(5)