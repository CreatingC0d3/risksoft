from termcolor import colored
from functions import back
from pymongo_get_database import get_database

dbname = get_database()
collection_name = dbname["elem_list"]


def search(main):
    msg = "SEARCH TEAM"
    print("\n")
    print(msg.center(50, " "))

    tot = collection_name.count_documents({})
    if tot > 0:
        search = str(input("Find Team: "))
        search = search.lower()

        item_details = collection_name.find()
        
        sum_cals = 0
        sum_weight = 0
        element = 0
        
        for team in item_details:
            if search == team['team_name']:
                
                element = element+1
                sum_cals = team['team_cals'] + sum_cals
                sum_weight = team['team_weight'] + sum_weight
                
                print(colored('Element', 'dark_grey'), element, colored(' Calories: ', 'green'), team['team_cals'], colored(' Weight: ', 'yellow'), team['team_weight'])
        
        print('\n')
        print('Total Calories: ', sum_cals)
        print('Total Weight: ', sum_weight)
        back(main)
            
    else:
        print("\n")
        print(colored('This team does not exist!', 'red'))
        back(main)