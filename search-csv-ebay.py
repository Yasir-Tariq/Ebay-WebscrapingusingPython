import math
import pandas as pd #using panda library and it's modules for proper indexing

#Defining a function to search according to the user's budget
def searchbybudget():
    budget=float(input('Enter budget: '))
    csv_file=pd.read_csv('/Users/apple/Desktop/webscrapping/dataaa.csv')
    pricelist = list(csv_file.iloc[:, 1])
    shiplist = list(csv_file.iloc[:, 2])
    namelist = list(csv_file.iloc[:, 0])
    resultlist=[]
    [resultlist.append(pricelist[i]+shiplist[i]) for i in range(0,55)]
    index=-1
    for row in resultlist:
      index+=1
      if budget >= row:
        print("Product Name: ",namelist[index])
        print("Total Cost: ",row)

#main body
if __name__ == "__main__":
    searchbybudget() #function call in main body
