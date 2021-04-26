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


sns.violinplot(x= "target", y = "sepal length (cm)", data = df, hue= "target_name")
plt.title("Violinplot for Sepal Length by Species")
plt.savefig('ImageFolder/violinplotforsepallength.png')
plt.show()

sns.violinplot(x= "target", y = "sepal width (cm)", data=df, hue= "target_name")
plt.title("Violinplot for Sepal Width by Species")
plt.savefig('ImageFolder/violinplotforsepalwidth.png')
plt.show()


sns.violinplot(x= "target", y = "petal length (cm)", data=df, hue= "target_name")
plt.title("Violinplot for Petal Length by Species")
plt.savefig('ImageFolder/violinplotforpetallength.png')
plt.show()


sns.violinplot(x= "target", y = "petal width (cm)", data=df, hue= "target_name")
plt.title("Violinplot for Petal Width by Species")
plt.savefig('ImageFolder/violinplotforpetalwidth.png')
plt.show()


