# A terminal app where you have a random amount of gold, you can buy goods and add it to your inventory
# Optional: add descriptions to the items souls like. a way for the user to ask for a spesific 

# Avoid Cicular Importing
import inventory
import checkInv
import botherDalla
import buyItem
import toDO
print("\n")
print("-----Welcome to the Dalla's Drygoods.-----")
print("If it's fancy shoes and perfumes you are looking for, you are lost.")
print("Dried meat, sturdy tools, thick clothing... I got all an adventurer needs on their next attempt at dying in a misirable way.")
x = 0
clumsyMeter = 0
enteringCounter = 0
unex = True
iss = True
# def buy():

# def bother():




# def entering():
#     print()
#     global clumsyMeter, enteringCounter, unex

#     while True:
#         x = input("Alright. Just careful now, don't clumsy over anything sharp. Enter. [Enter]")
#         while iss == True:
#             if x != "Enter":
#                 clumsyMeter = clumsyMeter + 1
#                 if(clumsyMeter > 2):
#                     print("SLAP, Get out!")
#                     break
#                 x = input("Watch out! Don't break that. Lets try this again. Enter.")
#             elif x == "Enter":
#                 continue             
        
#             entering2()
        

# def entering2():
#     selectableMenuChar = ["C", "B", "O", "E"]
#     print("\n")
#     menuClick = input("Tell me what you wish to do. You can [C]heck your inventory, [B]uy stuff, you can b[O]ther me about items, or you can [E]xit if your wallet is empty!")
#     if menuClick in selectableMenuChar:
#         print(f"You are doing[{menuClick}]")
#         if menuClick == "C":
#             checkInv.check()
#         if menuClick == "B":
#             buyItem.buy()
#         if menuClick == "E":
#             unex = True
#         if menuClick == "O":
#             botherDalla.bother()
#         print("\n")
#     else:
#         print("You typed wrong.")


     
   
# def entering():
#     print()
#     global clumsyMeter, enteringCounter
#     x = input("Alright. Just careful now, don't clumsy over anything sharp. Enter. [Enter]")
#     while True:
#         while clumsyMeter == 1:
#             x = input("Watch out! Don't break that. Lets try this again. Enter.")
#             clumsyMeter = clumsyMeter + 1
#         if x == "Enter":
#             selectableMenuChar = ["C", "B", "O", "E"]
#             print("\n")
#             menuClick = input("Tell me what you wish to do. You can [C]heck your inventory, [B]uy stuff, you can b[O]ther me about items, or you can [E]xit if your wallet is empty!")
#             if menuClick in selectableMenuChar:
#                 print(f"You are doing[{menuClick}]")
#                 if menuClick == "C":
#                     checkInv.check()
#                 if menuClick == "B":
#                     buyItem.buy()
#                 if menuClick == "E":
#                     break
#                 if menuClick == "O":
#                     botherDalla.bother()
#                 print("\n")
#             else:
#                 print("You typed wrong.")
            
#         else:
#             clumsyMeter = clumsyMeter + 1
#             if clumsyMeter >= 2:
#                 print("SLAP, Get out!")
#                 break

def entering():
    global menuCharInput
    print()
    x = input("Just careful now, don't clumsy over anything sharp. Enter. [Enter]")
    if x == "Enter":
        menuCharInput = input("Tell me what you wish to do. You can [C]heck your inventory, [B]uy stuff, you can b[O]ther me about items, or you can [E]xit if your wallet is empty!")
    elif x != "Enter":
        x2 = input("Watch out! Don't break that. Lets try this again. Enter.")
        if x2 == "Enter":
            menuCharInput = input("Tell me what you wish to do. You can [C]heck your inventory, [B]uy stuff, you can b[O]ther me about items, or you can [E]xit if your wallet is empty!").upper()
        else:
            print("SLAP, Get out!")
            exit()
    entering2()

def entering2():

    wrong_count = 0  
    global menuCharInput
    choice =  menuCharInput
    while True:
        
        if choice == "C":
            checkInv.check()
            panelRepeat()
            break
        elif choice == "B":
            buyItem.buy()
            panelRepeat()
            break
        elif choice == "O":
            botherDalla.bother()
            panelRepeat()
            break 
        elif choice == "E":
            if buyItem.total_spent == 0:
                print("Hmph… all that chatter and not a single coin spent.")

            elif buyItem.total_spent >= 100:
                print("Have a great day mister!")
            
            elif buyItem.total_spent >= 30:
                print("Alright. Have a good day.")
            
            
            break
        elif choice == "TODO":
            print("You have entered the secret realm where Dalla does not exist. Here you can update to do list.")
            toDO.todo()
            panelRepeat()
            break
        else: 
            wrong_count += 1

            if wrong_count == 3:
                print("Gods above, are you thick? It's not that hard!")
                break
            choice = input("[C]heck, [B]uy, b[O]ther, [E]xit: ").upper()


def panelRepeat():
    global menuCharInput
    print()
    menuCharInput = input("Tell me what you wish to do. You can [C]heck your inventory, [B]uy stuff, you can b[O]ther me about items, or you can [E]xit if your wallet is empty!").upper()
    entering2()


entering()