# %% import necessary module
import matplotlib.pyplot as plt
import stemgraphic
import pandas as pd

# %% Read csv and define coloumn name
df = pd.read_csv('cars.csv')
print(df)

df.columns = ['car', 'mpg', 'cly', 'disp', 'hp',
              'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

# %% Question 1
'''
	Quantitative data are data about numeric variables.
Here “mpg, disp, hp, drat, wt, qsec“ those columns have Quantitative data.
	Qualitative data are measures of 'types' and may be represented by a name, symbol, or a number code. Qualitative data are data about categorical variables.
Here “car, cly, vs, am, gear, carb” those columns have Qualitative data.
'''

# %% Question 2
'''Here i use pie chart for that'''

df['Car'].value_counts().plot(kind='pie')
# %%
df['cly'].value_counts().plot(kind='pie')
# %%
df['vs'].value_counts().plot(kind='pie')
# %%
df['am'].value_counts().plot(kind='pie')
# %%
df['gear'].value_counts().plot(kind='pie')
# %%
df['carb'].value_counts().plot(kind='pie')
# %%
'''Here i use pie chart for that'''
df['car'].value_counts().plot(kind='bar')
# %%
df['cly'].value_counts().plot(kind='bar')
# %%
df['vs'].value_counts().plot(kind='bar')
# %%
df['am'].value_counts().plot(kind='bar')
# %%
df['gear'].value_counts().plot(kind='bar')
# %%
df['carb'].value_counts().plot(kind='bar')

# %% Question 3
df.hist(column=['mpg'], bins=5)

# %% Question 4
df1 = df['carb']
print(type(df1))
stemgraphic.stem_graphic(df1, scale=10)

# Convert the series to a list then ploat
# l = df1.tolist()
# stemgraphic.stem_graphic(l, scale=10)

# data = [6, 5, 7, 6, 3, 5, 9, 5, 4, 7, 0]
# p = pd.Series(data)
# p = p//10
# plt.ylabel('Data')
# plt.xlabel('stems')
# plt.stem(p, data)

# %% Question 5
df.boxplot(column=['wt'])
# There is lot of outlayers...

# %% Question 6
df2 = df['mpg']

q1 = df2.quantile(.25)
q3 = df2.quantile(.75)

l = df2.tolist()

print([i for i in l if i < q1])
print([i for i in l if i > q3])
