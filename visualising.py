import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import datasets

data = datasets.load_iris()

iris_df = data


plt.title('Comparison between sepal width and length')
sns.scatterplot(iris_df['sepal length (cm)'], iris_df['sepal width (cm)']);

print('nope')