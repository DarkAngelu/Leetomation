import inquirer

from utils.get_number_of_users import get_number_of_users
from utils.get_user_tokens import get_user_tokens



def add_more_users(users):
    while True:
        # Ask if they want to proceed or add more users
        proceed_question = [
            inquirer.List("action", message="Do you want to proceed or add more users", choices=["Proceed", "Add More Users"]),
        ]
        
        proceed_answer = inquirer.prompt(proceed_question)

        if proceed_answer is not None and proceed_answer["action"] == "Proceed":
            break  # Exit the loop if they choose to proceed
        
        elif proceed_answer is not None and proceed_answer["action"] == "Add More Users":
            n = get_number_of_users()
            if n is None:
                continue  # Ask again if the number is invalid

            for i in range(n):
                user_data = get_user_tokens(len(users) + i)
                if user_data is not None:
                    users.append(user_data)
        else:
            print("Invalid choice, please select 'Proceed' or 'Add More Users'.")

