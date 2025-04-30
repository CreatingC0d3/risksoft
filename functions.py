import os
import sys
from termcolor import colored
from pymongo_get_database import get_database


def clear():
    #Linux
    if sys.platform.startswith('linux'):
        os.system('clear')
    #Windows
    if sys.platform.startswith('win32'):
        os.system('cls')
    #Mac OS X (10.4, 10.5, 10.7, 10.8)
    if sys.platform.startswith('darwin'):
        os.system('clear')


def back(main):
    print("\n")
    back = str(input("Do you want back? (y/n): "))
    back = back.lower()
    if back == 'y':
        clear()
        return main()
    else:
        clear()
        quit()


def validarDato(info):
    error_dato = True
    msg_dato = 'ok'
    while error_dato == True:
        if msg_dato == 'ok':
            if info == 'nombre':
                data = str(input("Your Team: "))
                data = data.lower()
            if info == 'passw':
                data = str(input("Your Password: "))
            if info == 'repass':
                data = str(input("Repeat Password: "))
        else:
            data = str(input(msg_dato))

        if not data:
            msg_dato = "Dato vacio, volver a intentar: "
        else:
            error_dato = False

    return data


def newElement(team_up, main, team_cals, team_weight):
    print("\n")
    print(colored('Team found!', 'green'))
    
    elem_list = []    
    
    while team_weight<10:
        print('Current calories: ', team_cals)
        print('Current weight: ', team_weight)
        print('\n')
        cal = float(input("Enter calories: "))
        weight = float(input("Enter weight: "))
        
        team_cals = cal + team_cals
        team_weight = weight + team_weight
        
        if team_cals < 15:
            print(colored('Calories is insufficient!', 'red'))
        else:
            print(colored('Calories is good!', 'green'))
            
        if team_weight > 10:
            print(colored('Weight too much!', 'red'))
        else:
            print(colored('Weight is good!', 'green'))
            
        
        #new dictionary
        elem = {"team_name": team_up, "team_cals": cal, "team_weight" : weight}
        if team_weight <= 10:
            elem_list.append(elem)
            
            if team_weight < 10:
                print('\n')
                fin = str(input(colored('Do you want save more records? (y/n): ', 'yellow')))
                if fin == 'y':
                    continue
                else:
                    break
        else:
            print(colored('Weight is wrong, record not saved!', 'red'))
        
        
    #insert
    dbname = get_database()
    collection_name = dbname["elem_list"]
    
    if team_weight >= 10 and team_cals < 15:
        print(colored('It is not possible to save the records because it exceeds the parameters.', 'red'))
        
    elif team_cals >= 15 and team_weight <= 10 or team_cals < 15 and team_weight < 10:
        collection_name.insert_many(elem_list)
        print("\n")
        print(colored('Registered elements successfully!', 'green'))
        
    back(main)