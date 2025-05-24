import inquirer

def get_number_of_users():
    """
    Get the number of users to be added.

    Args:
        None.

    Returns:
        The number of users as an integer, or None if the input is invalid.
    """

    questions = [
        inquirer.Text("n", message="How many numbers do you want to enter"),
    ]

    answers = inquirer.prompt(questions)

    if answers is not None and "n" in answers:
        try:
            n = int(answers["n"])
            return n
        except ValueError:
            print("Please enter a valid number.")
            return None
    else:
        print("Invalid input")
        return None