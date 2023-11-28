import pandas as pd
import random

lst = ['robot'] * 10

lst += ['human'] * 10

random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})

categories = data['whoAmI'].unique()
one_hot_df = pd.DataFrame(0, columns=categories, index=range(len(data)))
for i, category in enumerate(categories):
    one_hot_df[category] = data['whoAmI'].eq(category).astype(int)
data = pd.concat([data, one_hot_df], axis=1)
data.drop('whoAmI', axis=1, inplace=True)
data.head()
