from functions import back, validarDato, newElement
from termcolor import colored
from pymongo_get_database import get_database

dbname = get_database()
collection_team = dbname["team_list"]
collection_elem = dbname["elem_list"]

def regElements(main):
    msg = "REGISTER ELEMENTS"
    print("\n")
    print(msg.center(50, " "))
    print("\n")
    team_up = validarDato(info='nombre')

    tot_team = collection_team.count_documents({})
    if tot_team > 0:
        #cursor
        item_details = collection_team.find()
        
        sum_weight = 0
        sum_cals = 0
        
        for team in item_details:
            if team_up == team['team_name']:
                
                tot_elem = collection_elem.count_documents({})
                if tot_elem > 0:
                    #cursor
                    item_elements = collection_elem.find()
                    for elem in item_elements:
                        
                        if elem['team_name'] == team['team_name']:
                            
                            sum_weight = elem['team_weight'] + sum_weight
                            sum_cals = elem['team_cals'] + sum_cals                                                       
                    
        if sum_weight == 10:
            print("\n")
            print(colored('Weight is limited!', 'red'))
            back(main) 
        
        elif sum_weight < 10:
            newElement(team_up=team_up, main=main, team_cals=sum_cals, team_weight=sum_weight)

    else:
        print("\n")
        print(colored('Team no found!', 'red'))
        back(main)
        
        
        