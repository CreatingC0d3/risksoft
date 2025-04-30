from termcolor import colored
from functions import back, validarDato
from pymongo_get_database import get_database
from dateutil import parser

dbname = get_database()
collection_name = dbname["team_list"]


def register(main):
    msg = "REGISTER TEAM"
    print("\n")
    print(msg.center(50, " "))
    print("\n")
    team_up = validarDato(info='nombre')

    tot = collection_name.count_documents({})
    if tot > 0:
        #cursor
        item_details = collection_name.find()
        for team in item_details:
            if team_up == team['team_name']:
                print("\n")
                print(colored('This team already exists!', 'red'))
                back(main)

    passw_up = validarDato(info='passw')
    passw_re = validarDato(info='repass')

    if passw_up != passw_re:
        print("\n")
        print(colored('Password do not match!', 'red'))
        back(main)

    expiry_date = '2025-07-13T00:00:00.000Z'
    expiry = parser.parse(expiry_date)

    #new dictionary
    team_dict = {"team_name": team_up, "team_pass": passw_up, "expiry_date" : expiry}
    #insert
    collection_name.insert_one(team_dict)
    print("\n")
    print(colored('Registered team successfully!', 'green'))
    back(main)


