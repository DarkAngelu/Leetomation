from typing import Dict, List

from utils.add_more_users import add_more_users
from utils.get_number_of_users import get_number_of_users
from utils.get_user_tokens import get_user_tokens
from utils.leetcode import do_daily


# Initialize an empty list to store the user data
users: List[Dict[str, str]] = []

# Initial user input
n = get_number_of_users()
if n is None:
    exit(1)

# Collect initial users
for i in range(n):
    user_data = get_user_tokens(i)
    if user_data is not None:
        users.append(user_data)

# Ask if the user wants to proceed or add more users
add_more_users(users)


# Perform the daily problem for each user
for user in users:
    do_daily(user)