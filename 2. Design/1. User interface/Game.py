import os
def play():
    print("Press any key to start")
    
while x == True:
    print("Welcome to Snake Game")
    menu = input("What would you like to do? ")
    if menu == "start":
        play()
    elif menu == "quit":
        exit()
    else:
        os.system('cls')