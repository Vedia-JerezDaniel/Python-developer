# Dynamic Programming
#  Ugly number
# DP method

def nthUgly(n):
    dpUgly = [0] * n
    dpUgly[0] = 1

    u2 = u3 = u5 = 0

    multiple_2 = 2
    multiple_3 = 3
    multiple_5 = 5

    for i in range(1, n):
        dpUgly[i] = min(multiple_2, multiple_3, multiple_5)

        if dpUgly[i] == multiple_2:
            u2 += 1
            multiple_2 = dpUgly[u2] * 2

        if dpUgly[i] == multiple_3:
            u3 += 1
            multiple_3 = dpUgly[u3] * 3

        if dpUgly[i] == multiple_5:
            u5 += 1
            multiple_5 = dpUgly[u5] * 5

    return dpUgly[n - 1]

n = 500
print("50th ugly number is:", nthUgly(n))

# ADVANCED - TRAVELING
# SALESMAN
# PROBLEM

from itertools import permutations

V = 5


def travel_salesman_problem(graph, s):
    # store all vertices
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
            # print(vertex)

    min_path = []
    next_permutation = permutations(vertex)

    for i in next_permutation:
        current_pathweight = 0

        k = s
        for j in i:
            current_pathweight += graph[k][j]
            # print(j, i, current_pathweight, graph[k][j])
            k = j
        current_pathweight += graph[k][s]
        min_path.append(current_pathweight)
        x = sorted(min_path)

    return x[0]


if __name__ == "__main__":
    # matrix representation of graph
    graph = [[0, 10, 15, 20,30],
             [10, 0, 35, 25,5],
             [15, 35, 0, 30,60],
             [20, 25, 30, 0,1],
             [30,5,60,1,0]]
    s = 0
    print(travel_salesman_problem(graph, s))

# MINDBREAKER - PALINDROMIC
# MATRIX

import itertools
a = [['a', 'a', 'a'],
     ['b', 'b', 'a'],
     ['a', 'b', 'a']]
x = list(itertools.product(*a))
#print(x)

p_1 = []
for i in x:
    y = "".join(i)
    p_1.append(y)
# print(p_1)
# print(set(p_1))

def isPalin_2(p_1):
    p_2 = []
    for x in set(p_1):
        if x == x[::-1]:
            p_2.append(x)
    return p_2
print(isPalin_2(p_1))


# palindromic paths from top left to bottom right in a grid.

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

# i and j are row and column indexes of top left corner (these are 0, 0) -- m and n are bottom right corner (4,3)

def palindromic_path(string, a, i, j, m, n):

    # See slides of path traversal - show as lists
    if j < m - 1 or i < n - 1:
        if i < n - 1:
            palindromic_path(string + a[i][j], a, i + 1, j, m, n)
        if j < m - 1:
            palindromic_path(string + a[i][j], a, i, j + 1, m, n)

    # If we reach bottom right corner (or end of the path), we go to is_palindrome function to check it.
    else:
        string = string + a[n - 1][m - 1]
        if is_palindrome(string):
            print(string)

a = [['a', 'a', 'a'],
     ['b', 'b', 'a'],
     ['a', 'b', 'a']]

str = ""
print(palindromic_path(str, a, 0, 0, 3, 3))

You can replace the 'Y' values where 'Y' is 0 with the corresponding 'X' values using Python and pandas, a popular data manipulation library. Here's how you can do it:





import pandas as pd

# Create a DataFrame with your data
data = {'id': [1, 2, 3, 4, 5],
        'X': [10, 20, 35, 45, 55],
        'Y': [1, 0, 3, 0, 5]}
df = pd.DataFrame(data)
df
# Replace 'Y' values where 'Y' is 0 with the corresponding 'X' values
df.loc[df['Y'] == 0, 'Y'] = df.loc[df['Y'] == 0, 'X']

# Replace 'Y' values where 'Y' is 0 with the corresponding 'X' values, except for 'id' 4
df['Y'] = df.apply(lambda row: row['X'] if row['id'] != 4 and row['Y'] == 0 else 12 if row['id'] == 4 else row['Y'], axis=1)

for index, row in df.iterrows():
    if row['Y'] == 0:
        if row['id'] == 4:
            df.at[index, 'Y'] = 12
        else:
            df.at[index, 'Y'] = row['X']

# Print the updated DataFrame
print(df)


