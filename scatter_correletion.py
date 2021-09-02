import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import seaborn as sns

# # Import dataset
midwest = pd.read_csv("datasets/midwest_filter.csv")

# Prepare Data
# Create as many colors as there are unique midwest['category']
categories = np.unique(midwest['category'])
colors = [plt.cm.tab10(i / float(len(categories) - 1)) for i in range(len(categories))]

# Draw Plot for Each Category
fig = plt.figure(figsize=(16, 9), dpi=80, facecolor='w', edgecolor='k')

for i, category in enumerate(categories):
    plt.scatter('area', 'poptotal',
                data=midwest.loc[midwest.category == category, :],
                s=20, c=colors[i], label=str(category))

# Decorations
plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
              xlabel='Area', ylabel='Population')

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title("Scatterplot of Midwest Area vs Population", fontsize=22)
plt.legend(fontsize=12)
plt.show()
fig.savefig('Presentation/Files/Scatter/Scatter.pdf')

# Prepare Data
df = pd.read_csv("datasets/mtcars.csv")
x = df.loc[:, ['mpg']]
df['mpg_z'] = (x - x.mean()) / x.std()
df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
df.sort_values('mpg_z', inplace=True)
df.reset_index(inplace=True)

# Draw plot
fig = plt.figure(figsize=(16, 9), dpi=80)
plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z, color=df.colors, alpha=0.4, linewidth=5)

# Decorations
plt.gca().set(ylabel='$Model$', xlabel='$Mileage$')
plt.yticks(df.index, df.cars, fontsize=12)
plt.title('Diverging Bars of Car Mileage', fontdict={'size': 20})
plt.grid(linestyle='--', alpha=0.5)
fig.savefig('Presentation/Files/Scatter/Divergent_columns.pdf')
plt.show()

# Read data
df = pd.read_csv("datasets/email_campaign_funnel.csv")

# Draw Plot
fig = plt.figure(figsize=(16, 9), dpi=80)
group_col = 'Gender'
order_of_bars = df.Stage.unique()[::-1]
colors = [plt.cm.Spectral(i / float(len(df[group_col].unique()) - 1)) for i in range(len(df[group_col].unique()))]

for c, group in zip(colors, df[group_col].unique()):
    sns.barplot(x='Users', y='Stage', data=df.loc[df[group_col] == group, :], order=order_of_bars, color=c, label=group)

# Decorations
plt.xlabel("$Users$")
plt.ylabel("Stage of Purchase")
plt.yticks(fontsize=12)
plt.title("Population Pyramid of the Marketing Funnel", fontsize=22)
plt.legend()
fig.savefig('Presentation/Files/Scatter/Population_pyramid.pdf')
plt.show()

# Import
df_raw = pd.read_csv("datasets/mpg_ggplot2.csv")

# Prepare Data
df = df_raw.groupby('class').size()

# Make the plot with pandas
fig = plt.figure(figsize=(9, 9), dpi=80)
df.plot(kind='pie', subplots=True, figsize=(8, 8))
plt.title("Pie Chart of Vehicle Class - Bad")
plt.ylabel("")
fig.savefig('Presentation/Files/Scatter/Diagram.pdf')
plt.show()

import calmap

# Import Data
df = pd.read_csv("datasets/yahoo.csv", parse_dates=['date'])
df.set_index('date', inplace=True)

# Plot
plt.figure(figsize=(16, 9), dpi=80)
calmap.calendarplot(df['2014']['VIX.Close'], fig_kws={'figsize': (16, 10)},
                    yearlabel_kws={'color': 'black', 'fontsize': 14}, subplot_kws={'title': 'Yahoo Stock Prices'})
plt.show()
