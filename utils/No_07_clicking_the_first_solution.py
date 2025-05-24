from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



def clicking_the_first_solution(driver: WebDriver, wait: WebDriverWait[WebDriver]) -> None:
    """
    Click the first solution on the daily problem page.

    Args:
        wait: The WebDriverWait instance.

    Returns:
        None.
    """

    # Now we need to click the first solution 
    # Wait until at least one solution div is present
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".group.flex.w-full.cursor-pointer.flex-col"))
    )

    # Re-find the first solution div just before clicking
    first_clickable_div = driver.find_elements(By.CSS_SELECTOR, ".group.flex.w-full.cursor-pointer.flex-col")[0]
    first_clickable_div.click()