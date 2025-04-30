from register import register
from login import login
from search import search
from view import home, list, errorPage
from elements import regElements

def main():

    nav = str(input("Home(h) | Login(l) | Register(r) | Elements(e) | View(v) | Search(s): "))
    nav = nav.lower()

    if nav == 'h' or nav == 'l' or nav == 'r' or nav == 'e' or nav == 'v' or nav == 's':
        if nav == 'h':
            home(main=main)
        elif nav == 'l':
            login(main=main)
        elif nav == 'r':
            register(main=main)
        elif nav == 'e':
            regElements(main=main)
        elif nav == 'v':
            list(main=main)
        elif nav == 's':
            search(main=main)
    elif nav != 'h' or nav != 'l' or nav != 'r' or nav != 'e' or nav != 'v' or nav != 's':
        errorPage(main=main)

main()
