
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set()
from sklearn import datasets


data = datasets.load_iris()
df = pd.DataFrame(data["data"])
df["target"] = data["target"]



#making sure there isn't any missing values.
print(df.isnull().sum(axis=0))
'''

#Check for Duplicates.
print(df.duplicated().sum()) #This tells the number of duplicates.

print(df[df.duplicated()]) #This tells me where the duplicate occurs.

# Print Target Count
print(df['target'].value_counts())


#Species Count: There should be 50 each. 0 is Setosa, 1 is Veriscolor and 2 is Virginica.
plt.title('species count')
sns.countplot(df['target']);
plt.savefig('ImageFolder/speciescount.png')
plt.show()
'''



#references: https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d