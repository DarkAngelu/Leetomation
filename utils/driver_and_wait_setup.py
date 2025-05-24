from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def driver_and_wait_setup(timeout = 20):
    """
    Setup the driver and wait objects for Selenium tests.
    
    Args:
        nothing
    
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