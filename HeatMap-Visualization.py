import pandas as pd
import seaborn as sns

df = pd.read_csv("gapminder-FiveYearData.csv")
#reading the csv file present in the folder
df2 = df[['country', 'year', 'lifeExp']]
##taking the columns into an array
df3 = pd.pivot_table(df2, index='country', columns='year', values='lifeExp')
## creating a pivot table from the taken data
print(df3)
kss = sns.heatmap(df3, annot=True, fmt="f").get_figure().savefig('HeatMap1')
##drawing the heatmap and fmt refers to formatting value  and annot means annotation and savefig is used to save the
##image in the folder


## the image can be seen by using plt.show()
