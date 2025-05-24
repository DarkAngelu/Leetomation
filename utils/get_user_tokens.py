import inquirer


def get_user_tokens(i):
    user_question = [
        inquirer.Editor(f"LEETCODE_SESSION", message=f"Enter the LEETCODE_SESSION token for user {i+1}"),
        inquirer.Editor(f"csrftoken", message=f"Enter the csrftoken token for user {i+1}"),
    ]

    user_data = inquirer.prompt(user_question)

    if user_data is not None and "LEETCODE_SESSION" in user_data and "csrftoken" in user_data:
        return user_data
    else:
        print(f"Invalid input for user {i+1}.")
        return None

