import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cdj_dp - corr.csv')

corr = df.corr()
plt.subplots(figsize = (16, 8))

#Plot a heatmap of the correlation matrix we created
#sns.heatmap(corr, annot = True, cmap = 'YlGn')

# features1=['Appearance',	'Intelligence', 'Athleticism', 'Humor',	'Optimism',	'Patience',	'Confidence',	'Kindness']
# features2=['Cat1', 'Cat2','num1','num2']

# corr2 = df[features1].corr()
# df[features2].corr()


sns.heatmap(corr, annot = True, cmap = 'YlGn')
plt.show()
