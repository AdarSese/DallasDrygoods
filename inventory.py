class Items:
    def __init__(self,name,price,description):
        self.name = name
        self.price = price
        self.description = description

i1 = Items("Rusted Dagger", 13, "This dagger is hardly capable of cutting a bug. Try nails instead.")
i2 = Items("Old coin", 24, "This coin belongs to the times of Tesseth the Inflameable. The red poppy symbol signifies the protection agains the Flame.")
i3 = Items("Mushroom", 2, "It is said that mushrooms grow more the more you stare at them." )
id1 = Items("Flint and Steel", 10, "Essential for starting fires in the wild, though sparks can fly at the worst times.")
id2 = Items("Sturdy Rope", 15, "Coiled and ready for climbing, tying, or any desperate measures.")
id3 = Items("Water Skin", 8, "Holds water enough for a day’s march, if you ration carefully.")
id4 = Items("Hardtack Biscuits", 5, "Dry and hard, but keeps for weeks in a backpack.")
id5 = Items("Dried Meat", 12, "Slightly tough, but a reliable source of protein on long journeys.")
id6 = Items("Thick Wool Cloak", 20, "Protects against cold wind, rain, and the occasional suspicious glance.")
id7 = Items("Leather Gloves", 7, "Good for handling hot coals or thorny branches.")
id8 = Items("Oil Lantern", 18, "A flickering light to guide adventurers through caves and forests.")
id9 = Items("Tent", 25, "A small, foldable tent to provide shelter from rain or snow.")
id10 = Items("Bedroll", 10, "Simple padding for sleeping under the stars or in a dank tavern.")
id11 = Items("Cooking Pot", 15, "Useful for making stew, soup, or anything that can survive boiling.")
id12 = Items("Pickaxe", 30, "For mining rocks or defending yourself if no other weapon is at hand.")
id13 = Items("Crowbar", 22, "Handy for prying open crates, doors, or stubborn chests.")
id14 = Items("Fishing Line & Hooks", 12, "Catch a meal from rivers, lakes, or ponds if you’re patient enough.")
id15 = Items("Small Shovel", 10, "Digging holes, trenches, or hiding ill-gotten treasures.")
id16 = Items("Barrel of Salt", 18, "Preserve food, flavor meals, or trade with other travelers.")
id17 = Items("Torch Bundle", 14, "Keep one lit while the others wait in case darkness grows heavy.")
id18 = Items("Canteen of Oil", 20, "Useful for lanterns, fires, or less savory purposes.")
id19 = Items("Rations Pack", 25, "Enough dried food to last a small party for several days.")
id20 = Items("Blanket", 12, "Thick enough to stay warm on cold nights, light enough to carry.")
id21 = Items("Hooded Rain Cloak", 18, "Water rolls off, and the hood keeps your head dry.")
id22 = Items("Hammer & Nails", 15, "Essential for repairs, camp setups, or ad hoc barricades.")
id23 = Items("Fishing Net", 22, "Catch multiple fish at once — requires patience and skill.")
id24 = Items("Signal Whistle", 8, "Make noise to alert others, or scare off wildlife.")
id25 = Items("Bear Trap", 35, "Heavy and dangerous, but effective for hunting or defense.")
id26 = Items("Iron Bucket", 10, "Carry water, mix ingredients, or hold whatever else you need.")
id27 = Items("Spare Shoes", 20, "Extra footwear for long journeys, or in case of mud or rain damage.")

characterInv = [i1, i2, i3]
dallaInv = [id1, id2, id3, id4, id5, id6, id7, id8, id9, id10,
            id11, id12, id13, id14, id15, id16, id17, id18, id19, id20,
            id21, id22, id23, id24, id25, id26, id27]
allInv = characterInv + dallaInv


# def findItembyName():
    
#     for item in allInv:
#         if "Mushroom" is item.name:
#             wordExistsInInventory = True
        
            










# new_item = Items(input("enter name"),input("enter price"),input("enter desc"))
# itemsList.append(new_item)




# for number in range(0,len(itemsList)):
    
#     print(f"{itemsList[number].description}")




# listt = ["aa", 12, "fav"]
# for i in range(3):
#     print(listt[i])