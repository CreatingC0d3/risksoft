from termcolor import colored
from functions import back
from pymongo_get_database import get_database

dbname = get_database()
collection_name = dbname["team_list"]


def home(main):
    home = "RISK SOFT"
    print("\n")
    print(home.center(50, " "))
    text = "Una serie de excursionistas desea crear un software  \nque permita determinar los elementos que pueden usarse \npara escalar un risco, basado en las propiedades caloricas \ny peso de cada elemento. Para escalar el risco se especificara \nla cantidad minima de calorias, ademas del peso maximo que se \npuede llevar. El software debera indicar al usuario el conjunto \nde elementos optimos, basado en que cumplan el minimo de \ncalorias y llevar el menor peso posible."
    print("\n")
    print(text.center(50, " "))
    print("\n")
    back(main)


def list(main):
    msg = "TEAMS LIST"
    print("\n")
    print(msg.center(50, " "))
    tot = collection_name.count_documents({})

    if tot > 0:
        print("\n")
        item_details = collection_name.find()
        init = 0
        while init < tot:
            print(colored('Name: ', 'green'), item_details[init]['team_name'], colored(' Password: ', 'yellow'), item_details[init]['team_pass'])
            init = init+1
        back(main)

    else:
        print("\n")
        print(colored('No data to display!', 'red'))
        back(main)
        
def admin(main, team):
    wellcome = "WELLCOME TO SOFT-RISK APP"
    hello = "Hello " + team
    print("\n")
    print(wellcome.center(50, "="))
    print("\n")
    print(hello.center(50, " "))
    back(main)
    
    
def navbar():
    nav = "Home(h) | Login(l) | Register(r) | Elements(e) | View(v) | Search(s): "
    print(nav.center(50, " "))
    print("\n")
    
    
def errorPage(main):
    error_page = "Oups! Page not found!"
    er_404 = "404"
    print("\n")
    print(colored(error_page.center(50, " "), 'red'))
    print("\n")
    print(er_404.center(50, " "))
    back(main)
