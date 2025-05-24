from selenium.webdriver.chrome.webdriver import WebDriver



def getting_to_solution_page(driver: WebDriver) -> None:
    """
    Get to the solutions page of the daily problem.

    Args:
        driver: The Selenium WebDriver instance.

    Returns:
        None.
    """

    # Get to the Solution tab by changing the URL
    current_url = driver.current_url

    # Replace 'description' with 'solutions'
    solutions_url = current_url.replace('/description/', '/solutions/')

    # Navigate to the solutions URL
    driver.get(solutions_url)