from game_data import data
import random

def format(account):
    """This function extracts data from the account"""
    name = account.get("name")
    des = account.get("description")
    country = account.get("country")
    f_c = account.get("follower_count")
    return f"{name}, {des}, from{country}"
A_account = random.choice(data)
B_account = random.choice(data)

print(f"Compare A : {format(A_account)}")
print(f"Compare B : {format(B_account)}")
