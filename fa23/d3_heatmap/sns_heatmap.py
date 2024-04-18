import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cdj_dp - corr.csv')

corr = df.corr()
plt.subplots(figsize = (16, 8))

sns.heatmap(corr, annot = True, cmap = 'YlGn')
plt.show()