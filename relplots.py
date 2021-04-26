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

col = "sepal length (cm)"
sns.relplot(x=col, y ="target", hue="target_name", data=df)
plt.title(col)
plt.savefig('ImageFolder/relplotsepallengthplt.png')
#plt.show()

col = "sepal width (cm)"
sns.relplot(x=col, y ="target", hue="target_name", data=df)
plt.title(col)
plt.savefig('ImageFolder/relplotsepalwidthplt.png')
#plt.show()

col = "petal length (cm)"
sns.relplot(x=col, y ="target", hue="target_name", data=df)
plt.title(col)
plt.savefig('ImageFolder/relplotpetallengthplt.png')
#plt.show()

col = "petal width (cm)"
sns.relplot(x=col, y ="target", hue="target_name", data=df)
plt.title(col)
# plt.savefig('ImageFolder/relplotpetalwidthplt.png')
plt.show()