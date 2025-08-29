
list_of_things_to_do = ["Make a ToDo List system where you can add stuff in it ", "aa"] 
#buying "a" or other things result in a random buy. Fix it
#not a single coin spent fix
#money is not functional 


def addTodo():
    addedElement = input("What element do you wish to add: ")
    list_of_things_to_do.append(addedElement)

def eraseTodo():
    erasedElement = input("What element do you wish to erase: ")
    list_of_things_to_do.remove(str(erasedElement))

def checkTodo():
    print()
    for i, todoElement in enumerate(list_of_things_to_do, start=1):
        print(f"{i}. {todoElement}")
    print()

def todo():
    print("Welcome to the ToDo.")
    print("Here's the ToDo list:")
    print()
    for i, todoElement in enumerate(list_of_things_to_do, start=1):
        print(f"{i}. {todoElement}")
    print()
    while True:
        todoInput = input("[A]dd element. [E]rase element. [C]heck list.  [Anything else] to back to Dalla")
        if todoInput == "A":
            addTodo()
            continue
        elif todoInput == "E":
            eraseTodo()
            continue
        elif todoInput == "C":
            checkTodo()
        else: break
           
