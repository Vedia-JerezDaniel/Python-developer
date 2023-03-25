# %% Different ways to take a sum of a column

import pandas as pd

# %% Read demo data

websites = pd.read_csv("popular_websites.csv", index_col=0)
websites.head()
print(websites.shape)

# %% Best way: use the dedicated pandas .sum() method

websites["total_views"].sum()

# %% List comprehension with .itertuples()

sum(website.total_views for website in websites.itertuples())

# %% Manual loop with .itertuples()

total = 0
for website in websites.itertuples():
    total += website.total_views

total
