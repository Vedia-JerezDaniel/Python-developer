import pandas as pd
import random


def ask_her():
    print('Enter the five akas: ')
    aka_1, aka_2, aka_3, aka_4, aka_5 = [str(x) for x in input("Enter five akas: \n").split(', ')]
    print(f"\nThe name of selected girl are:  {aka_1}, {aka_2}, {aka_3}, {aka_4} and {aka_5}")
    return aka_1, aka_2, aka_3, aka_4, aka_5

aka_1, aka_2, aka_3, aka_4, aka_5 = ask_her()

def get_lucky():
    l1 = [1]
    l2 = [2]
    l3 = [3]
    l4 = [4]
    l5 = [5]
    go = pd.DataFrame()
    for _ in range(9):
        l1.append(random.randint(1,5))
        l2.append(random.randint(1,5))
        l3.append(random.randint(1,5))
        l4.append(random.randint(1,5))
        l5.append(random.randint(1,5))
        
    go = pd.DataFrame(list(zip(l1,l2,l3,l4,l5)), columns =['e1', 'e2', 'e3', 'e4', 'e5'])
    if len(aka_5) <= 2:
        go.drop(go.columns[4], axis=1, inplace=True)
    return go

def get_sum(es):
    go = get_lucky()
    return [
        sum(go[column].iloc[i] == es for i in range(len(go)))
        for column in go.columns]

def go_m():
    data = []
    for i in range(1,6):
        lst = get_sum(i)
        row = {"list": lst}
        del lst
        data.append(row)
    db = []
    for i in data:
        df = pd.DataFrame(i['list'], columns=['e']) # create the DataFrame from the list of dictionaries
        db.append(df)
    del data
    return pd.concat(db, axis=1)

def let_go():
    dtt = go_m()
    e = dtt.sum(axis=0).to_list()
    del dtt
    de = {'Escort': [aka_1, aka_2, aka_3, aka_4,aka_5],'Summ points': e}
    ded = pd.DataFrame(de).set_index('Escort')
    print(ded[ded['Summ points'] > 11])
    

if __name__ == "__main__":
    print(f"{'--'*10} \n First run!")
    let_go()
    print(f"{'--'*10} \n Second run!")
    let_go()
    print(f"{'--'*10} \n Last run!")
    let_go()

    print('Make your selection and enjoy!')