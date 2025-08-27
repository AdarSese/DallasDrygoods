import random
import gold
import inventory


#we want to buy items into our inventory. Erase the item from dalla's inventory and append() it into our own
#Optional: Shuffle the shop item list
#.pop(1)

def transfer():
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
                        break
                # if i == False:
                #     print("there is no such item")
                #     break
        transfer()
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
       
