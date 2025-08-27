import inventory
import gold
import botherDalla


#I think it is safe to assume, that this works.
#You can check your inventory items and their price. 
#You can check your current gold.

def check():
    print("Welcome to your Inventory")
    print("Here's the list of your items :")
    for i in range(0,len(inventory.characterInv)):
        print(f"{inventory.characterInv[i].name}  worth {inventory.characterInv[i].price} gold")
    print(f"You have {gold.owned_gold} gold")
    botherOrNo = input("Want to bother Dalla to inspect an item for you? [y or n]")
    if botherOrNo == "y":
        botherOrNo = True
        botherDalla.bother()
    elif botherOrNo == "n":
        botherOrNo = False
