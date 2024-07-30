import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

### Colors
color1 = 'blue' # Light Blue
color2 = '#41210A' # Dark Brown
color3 = '#8A55A2' # Pink
color4 = '#5854A3' # Purple
color5 = '#2D5653' # Dark Green
colorbg ='#EBCFA7' # BG Light Brown

# Define the background style and colors of the chart elements.
sns.set(rc={"axes.facecolor": colorbg, "figure.facecolor": colorbg, "axes.labelcolor": color2, "xtick.color": color2, "ytick.color": color2, "text.color": color2})
color_palette_num = [color1, color2, color3, color4, color5]
color_palette_cluster = [color1, color3, color5, color2, color4]

# Set global parameters for all bar charts
plt.rcParams['patch.edgecolor'] = 'none'  # Removes edges from all patches (including bars)