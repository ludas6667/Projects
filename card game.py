import random, os

def clr():
    os.system("clear")

def start():
    print("*-----------*")
    print("*  -Start-  *")
    print("*  -Rules-  *")
    print("*  -Leave-  *")
    print("*-----------*")
    
    start_select = input("").lower()
    
    if start_select == "rules" or start_select == "2":
        clr()
        rules()
        input()
        clr()
        start()
    elif start_select == "leave" or start_select == "3":
        end()
    elif start_select == "start" or start_select == "1":
        clr()
        game()
        input()
    else:
        print("No valid option selected")
        input("")
        clr()
        start()
    
def rules():
    print(f"Your goal in this game is to\nopen packs and get valuable\ncards. The better cards you\nget the more they are worth.\nHave fun")
    
def end():
    SystemExit    

def game():
    print("Welcome!!! Lets Begin")
    
start()