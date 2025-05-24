from typing import Dict

from utils.No_01_driver_and_wait_setup import driver_and_wait_setup
from utils.No_02_add_cookies import add_cookies
from utils.No_03_click_daily_problem import click_daily_problem
from utils.No_04_switching_to_the_daily_problelm_tab import switching_to_the_daily_problem_tab
from utils.No_05_getting_to_solution_page import getting_to_solution_page
from utils.No_06_filtering_out_cpp_code import filtering_out_cpp_code
from utils.No_07_clicking_the_first_solution import clicking_the_first_solution
from utils.No_08_extracting_the_solution import extracting_the_solution
from utils.No_09_submit_code_to_editor import submit_code_to_editor


def do_daily(cookies: Dict[str, str] = {}) -> None:
    """
    Perform the daily problem on LeetCode.

    Args:
        cookies: A dictionary of cookies to add. The keys are cookie names,
                 and the values are cookie values (both strings).
                 Default is an empty dictionary.

    Returns:
        None.
    """

    
    # 1. Setup the driver and wait objects
    driver, wait = driver_and_wait_setup()



    # 2. Add cookies to the driver and navigate to the /problemset/all/ page
    add_cookies(driver, cookies)



    # 3. Wait for the daily problem to be clickable and click it
    click_daily_problem(wait)


    
    # 4. Now we need to switch to the Solutions tab of the daily problem page
    switching_to_the_daily_problem_tab(driver)


    
    # 5. Now we need to get to the solutions page
    getting_to_solution_page(driver)
    


    # 6. Now we need to filter out the C++ code from the solutions page
    filtering_out_cpp_code(driver, wait)

    

    # 7. Now we need to click the first solution on the daily problem page
    clicking_the_first_solution(driver, wait)

    

    # 8. Now we need to get the C++ code from the first solution
    cpp_code = extracting_the_solution(wait)    


    # 9. Now we need to submit the code to the Monaco editor on the daily problem page
    submit_code_to_editor(driver, wait, cpp_code)


    # 10. Close the driver
    driver.quit()