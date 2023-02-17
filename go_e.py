import pandas as pd
import numpy as np
import random

l1 = [1]
l2 = [2]
l3 = [3]
l4 = [4]
l5 = [5]

for _ in range(9):
    l1.append(random.randint(1,5))
    l2.append(random.randint(1,5))
    l3.append(random.randint(1,5))
    l4.append(random.randint(1,5))
    l5.append(random.randint(1,5))
    
go = pd.DataFrame(list(zip(l1,l2,l3,l4,l5)), columns =['e1', 'e2', 'e3', 'e4', 'e5'])
go

def get_sum(es):
    return [
        sum(go[column].iloc[i] == es for i in range(len(go)))
        for column in go.columns]

data = []
for i in range(1,6):
    lst = get_sum(i)
    row = {"list": lst} # create a dictionary for the row
    data.append(row)

data

db = []
for i in data:
    print(i['list'])
    df = pd.DataFrame(i['list'], columns=['e']) # create the DataFrame from the list of dictionaries
    db.append(df)

dtt = pd.concat(db, axis=1)
dtt

e = dtt.sum(axis=0).to_list()
e