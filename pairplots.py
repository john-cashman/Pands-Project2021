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


sns.pairplot(df, hue = "target_name")
plt.savefig("snsoverview.png")
plt.savefig('ImageFolder/pairplot.png')
# plt.show()