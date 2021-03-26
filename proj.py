# import the tools needed to analyse and plot the data. 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn import datasets
print('done')

# This updates the plotting styles within the program to follow the seaborn style. Not needed,just the seaborn style looks better.
sns.set()

# loads the Iris dataset from sklearns datasets. Important to include the "()" afterwards. 
data = datasets.load_iris()


df = pd.DataFrame(data["data"], columns=data["feature_names"])
df["target"] = data["target"]

# describes the data
# print(data["DESCR"])

# print(data)
print(data["feature_names"])
print('still works')
