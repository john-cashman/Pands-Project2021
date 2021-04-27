
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set()
from sklearn import datasets


data = datasets.load_iris()

data["feature_names"]

df = pd.DataFrame(data["data"], columns=data["feature_names"])

df["target"] = data["target"]

df["target_name"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

# lmplpots

# Lmplot for sepal length and sepal width.
sns.lmplot(x = 'sepal length (cm)', y = 'sepal width (cm)', data = df, hue = 'target_name', col = 'target')
plt.savefig('ImageFolder/lmppltsepal.png')
plt.show()


# Lmplot for petal length and petal width.
sns.lmplot(x = 'petal length (cm)', y = 'petal width (cm)', data = df, hue = 'target_name', col = 'target')
plt.savefig('ImageFolder/lmppltsepal.png')
plt.show()