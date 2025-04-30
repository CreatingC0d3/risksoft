from termcolor import colored
from functions import back, clear
from view import admin, navbar
from pymongo_get_database import get_database

dbname = get_database()
collection_name = dbname["team_list"]


def login(main):
    msg = "ENTER TEAM DATA"
    print("\n")
    print(msg.center(50, " "))
    print("\n")
    team = str(input("Your Team: "))
    team = team.lower()

    tot = collection_name.count_documents({})
    if tot > 0:
        item_details = collection_name.find()
        for item in item_details:
            if team == item['team_name']:
                passw = str(input("Your Password: "))
                
                pass_conf = item['team_pass']

                if passw == pass_conf:
                    clear()
                    navbar()
                    admin(team=team, main=main)
                else:
                    print("\n")
                    print(colored('Your password is wrong!', 'red'))
                    back(main)
            
        print("\n")
        print(colored('This team does not exist!', 'red'))
        back(main)
    else:
        print("\n")
        print(colored('Not Team!', 'red'))
        back(main)