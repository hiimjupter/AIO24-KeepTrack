import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(
    "/Users/jupternguyen/Projects/EXT10004_AIO24/Homework/AIO24-KeepTrack/M02_Week4/advertising.csv")

# Question 7
x = data['TV']
y = data['Radio']

print(np.corrcoef(x, y))


# Question 8
print(data.corr())

# Question 9
plt.figure(figsize=(10, 8))
data_corr = data.corr()
sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=.5)
plt.show()
