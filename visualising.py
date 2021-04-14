
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set()
from sklearn import datasets


data = datasets.load_iris()
df = pd.DataFrame(data["data"])
df["target"] = data["target"]

plt.title('difference between sepal width and length')
sns.scatterplot(df['sepal_length'], df['sepal_width']);
plt.show()