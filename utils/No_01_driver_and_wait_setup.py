from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


def driver_and_wait_setup(timeout: int = 20) -> tuple[WebDriver, WebDriverWait[WebDriver]]:
    """
    Setup the driver and wait objects for Selenium tests.
    
    Args:
        timeout: The timeout value for the WebDriverWait instance.
            Default is 20 seconds.
    
    Returns:
        A tuple containing the driver and wait instances.
    """


    # Setup Chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    service = Service(executable_path = "chromedriver.exe")
    driver = webdriver.Chrome(service = service, options = chrome_options)

    wait = WebDriverWait(driver, timeout)

    return driver, wait