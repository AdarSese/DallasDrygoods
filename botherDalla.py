#Here, we will ask Dalla to give us a description of the selected item
#Dear god, it took me two hours to figure out the "You dont have this item" algorithm
#Oh still doesnt work. findItembyName is broken
# IT WORKS NOW
import inventory

def YouDontHaveItem():
    global wordExistsInInventory
    global wordExistsInDallaInventory
    
    for item in inventory.characterInv:
        
        if descThis != item.name:
            wordExistsInInventory = False
            wordExistsInDallaInventory = False
        elif descThis == item.name:
            wordExistsInInventory = True
            wordExistsInDallaInventory = False
            break

    for item in inventory.dallaInv:
        if descThis != item.name:
            wordExistsInDallaInventory = False
        elif descThis == item.name:
            wordExistsInDallaInventory = True
            break

def bother():
    global descThis
    global currentItem
    print("Ughhh. Seriously? I am a shopkeeper. Not a lecturer.")
    descThis = input("Anyways, which item do you want the description of? ")
    for i in range(0,len(inventory.characterInv)):
        currentItem = inventory.characterInv[i]
        if descThis == currentItem.name:
            print(f"Ah... {currentItem.name}  {currentItem.description}")
    
    YouDontHaveItem()
    
    if wordExistsInInventory is False and wordExistsInDallaInventory is False:
        print("There is no such item here.")
    elif wordExistsInInventory is False and wordExistsInDallaInventory is True:
        print("I have this item. YOU DONT. Want to buy it? Or are there scorpions in your wallet?")
          
