import random
import gold
import inventory


#we want to buy items into our inventory. Erase the item from dalla's inventory and append() it into our own
#Optional: Shuffle the shop item list
#.pop(1)

def transfer():
        global spent_gold
        global cost_of_bought_Item
        global trueboughtitemname
        cost_of_bought_Item = inventory.dallaInv[idItem].price
        trueboughtitemname = inventory.dallaInv[idItem].name
        gold.owned_gold =  gold.owned_gold - cost_of_bought_Item
        
        item = inventory.dallaInv.pop(idItem)
        inventory.characterInv.append(item)  # DIFFERENCE BETWEEN APPEND AND POP! Now i understand it. Its a simple reason.
        
        



def shuffle():
        random.shuffle(inventory.dallaInv)

def buy():
        global idItem
        print("\n")
        print("-------So how does my shop look?--------")
        print("Here's the list of my goods. Be careful with them: ")
        #shuffle()
        #STUDY THIS
        for item in inventory.dallaInv:
                print(f"{item.name:.<20} | {item.price:.>5} gold")
        
        print()
        boughtItem = input("Which item do you wish to buy?: ")
        
        for i in range(0,len(inventory.dallaInv)):
                if boughtItem == inventory.dallaInv[i].name:
                        idItem = i
                        print(f"idItem is: {idItem}")
                        print(f"Your gold was: {gold.owned_gold}")
                        transfer()
                        print(f"idItem is: {idItem}")
                        print(f"true bough item name: {trueboughtitemname}")
                        print(f"cost of bought item is: {cost_of_bought_Item}")
                       
                        print(f"now your gold is: {gold.owned_gold}")
                        


                        break
                # if i == False:
                #     print("there is no such item")
                #     break
        
        # THIS CODE REVEALS A HIDDEN BuG print(f"Hmm..{inventory.dallaInv[idItem].name}, it wortheth {inventory.dallaInv[idItem].price} gold")
        print("\n")
        print("Now your inventory is: ")
        print("------------------------------")
        for itemm in inventory.characterInv:
                print(f"{itemm.name}")
       











# x = [1,5,21,2]
# y = [3,7]
# transferredUnit = int(input("Which number you want trasfered into y? " ))
# for i in range(0,len(x)-1):
    
#     while transferredUnit == x[i]:
#        x.pop(i)
#        y.append(transferredUnit)
       
# print(x)
# print(y)
       
