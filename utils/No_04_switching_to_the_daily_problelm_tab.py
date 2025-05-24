from selenium.webdriver.chrome.webdriver import WebDriver


def switching_to_the_daily_problem_tab(driver: WebDriver) -> None:
    """
    Switch to the tab of the daily problem.

    Args:
        driver: The Selenium WebDriver instance.

    Returns:
        None.
    """


    # Switch to the tab of the daily problem
    original_window = driver.current_window_handle

    window_handles = driver.window_handles

    for handle in window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

    # Now Selenium is focused on the new tab (daily problem)