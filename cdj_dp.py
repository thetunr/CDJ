import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Data simulation
np.random.seed(1)
data = np.random.rand(10, 10)

mydata2 = pd.read_csv("data.csv", header = None, names = ['ID', 'first_name', 'salary'])

sns.heatmap(data)
plt.show()
