# Source: https://medium.com/mlearning-ai/wordclouds-with-python-c287887acc8b
# Github: https://github.com/m3redithw/data-science-visualizations/blob/main/WordClouds/wordclouds.ipynb
import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import font_manager
import random

# reading csv for dating preferences
dp_text = pd.read_csv('cdj_dp - wordcloud.csv')
dp_text = list(map(lambda x: x.lower(), dp_text))

def convert(lst):
    stripped_list = map(str.strip, lst)
    return ' '.join(stripped_list)
dp_text = convert(dp_text)

# importing mask
heart_mask = np.array(Image.open('./redheart.png'))

# font
my_font_path = 'fonts/jai.ttf'
font_manager.fontManager.addfont(my_font_path)

# color map
cmp = ListedColormap(['#c49ed9', '#ffb3d0', '#ff96bd', '#9ed2ff', '#73bbff'])

# creating and displaying word cloud
wc = WordCloud(font_path= my_font_path, background_color='#ffffff', 
               mask = heart_mask, contour_width = 0, contour_color='#FFFFFF', colormap = cmp, random_state= random.randint(1, 500)).generate(dp_text)
plt.figure(figsize=[10,10])
plt.tight_layout()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
