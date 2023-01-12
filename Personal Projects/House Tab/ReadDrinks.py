import pandas as pd
from DrinkClass import *

drinkid = "2"

#creating dataframe of drinks list by reading excel sheet
drinks = pd.read_excel("DrinksList.xlsx")

#creating variables for each column
ids = drinks["ID"]
names = drinks["Name"]
prices = drinks["Price"]

#function to create index list based off how many drinks, n, there are
def indexCreator(n):
    listy = []
    for i in range(1,n+1):
        listy.append(str(i))
    return listy

#applying index list to drinks dataframe
drinks.index = indexCreator(2)

#creating drink object using dataframe
drinkOfNight = drink(drinks.loc[drinkid]["ID"], drinks.loc[drinkid]["Name"], drinks.loc[drinkid]["Price"])

print(drinkOfNight.getName())
print(drinkOfNight.getPrice())
