from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



def extracting_the_solution(wait: WebDriverWait[WebDriver]) -> str:
    """
    Extract the solution from the daily problem page.

    Args:
        driver: The Selenium WebDriver instance.

    Returns:
        The C++ code as a string.
    """

    
    # Now we need to extract the C++ code from the solution



    # Wait until the code block is present
    code_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "code.language-cpp"))
    )

    # Extract and print the code
    cpp_code: str = code_element.text

    return cpp_code

    # Optional: save the code to a file 

    # with open("leetcode_solution.cpp", "w", encoding="utf-8") as file:
    #     file.write(cpp_code)
    #     print("✅ Code saved to leetcode_solution.cpp")