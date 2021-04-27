

'''
Exploring the Iris Dataset:
Importing the libraries and loading the dataset.
'''



# import the libraries. 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns




# I'm loading the dataset directly from sklearn. I installed sklearn onto my machine already and found doing it this way easier than downloading the dataset as a csv file.
from sklearn import datasets
data = datasets.load_iris()
print("done")


# Getting a bried introduction to the dataset:
# Tells a little bit about the dataset.
print(data["DESCR"])


#Check for Duplicates.
print(df.duplicated().sum()) #This tells the number of duplicates.

print(df[df.duplicated()]) #This tells me where the duplicate occurs.


# The dataset is built on comparing 3 different species of iris flower based on 4 distinct features. The names of the 4 features are: sepal length, sepal width, petal length and petal width.import
data["feature_names"]



# Adding target from dataset.
df = pd.DataFrame(data["data"], columns=data["feature_names"])
df["target"] = data["target"]
df.head()



# The dataset has 150 data-points and 4 features. It then also has 1 class label for the target which was added above. If I ran the df.shape command before adding the target it would say that there are 4 features.
df.shape


# Species count checks the to see how this 150 data-points is distributed accross the 3 species.
plt.title('species count')
sns.countplot(df['target']);
plt.savefig('ImageFolder/Speciescount.png')   


# The below 'describe' command gives an easy to read overview of the whole dataset. Below is a basic description of the data. It shows some basic statistics of the 4 features. Although it is a basic description it still gives some interesting information. For example that there is a big difference between the smallest petal length and the largest. There isn't as large a range in petal width.
df.describe()

# Get the target names
data["target_names"]

# Put names to the targets
# gives the targets names for the plot. 0 = setosa, 1 = versicolor and 2 = virginica
df["target_name"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})



#  Scatter Plots:
sns.set_style("whitegrid"); 
sns.FacetGrid(data, hue="target", size=8)\
    .map(plt.scatter, "sepal length (cm)", "sepal width (cm)")\
    .add_legend()    
plt.show();


sns.set_style("whitegrid");
sns.FacetGrid(df, hue="target", size=8)\
    .map(plt.scatter, "petal length (cm)", "petal width (cm)")\
    .add_legend()
plt.show();



# Histograms
col = "sepal length (cm)"
df[col].hist()
plt.suptitle(col)
plt.savefig('sepallengthhist.png')
plt.show()

col = "sepal width (cm)"
df[col].hist()
plt.suptitle(col)
plt.savefig('sepalwidththhist.png')
plt.show()


col = "petal length (cm)"
df[col].hist()
plt.suptitle(col)
plt.savefig('petallengthhist.png')
plt.show()

col = "petal width (cm)"
df[col].hist()
plt.suptitle(col)
plt.savefig('petalwidthhist.png')
plt.show()


# Rel Plots:
# sepal length and the target
col = "sepal length (cm)"
sns.relplot(x=col, y ="target", hue="target_name", data=df)
plt.title(col)
plt.savefig('sepallengthplt.png')
plt.show()


# Showing the relationship of sepal width with the target. 
col = "sepal width (cm)"
sns.relplot(x=col, y ="target", hue="target_name", data=df)
plt.title(col)
plt.savefig('sepalwidthplt.png')
plt.show()


# Showing the relationship of petal length with the target.
col = "petal length (cm)"
sns.relplot(x=col, y ="target", hue="target_name", data=df)
plt.title(col)
plt.savefig('petallengthplt.png')
plt.show()


# Showing the relationship of petal width with the target.
col = "petal width (cm)"
sns.relplot(x=col, y ="target", hue="target_name", data=df)
plt.title(col)
plt.savefig('petalwidthplt.png')
plt.show()

# Pair Plots
sns.pairplot(df, hue = "target_name")
plt.savefig("snsoverview.png")
plt.show()


# Box Plot
sns.boxplot(data=df, orient="h", palette="Set2")
plt.savefig('ImageFolder/violinplot.png')
plt.show()


# Violin Plot for each variable
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


# lmplpots

# Lmplot for sepal length and sepal width.
sns.lmplot(x = 'sepal length (cm)', y = 'sepal width (cm)', data = df, hue = 'target_name', col = 'target')
plt.savefig('ImageFolder/lmppltsepal.png')
plt.show()


# Lmplot for petal length and petal width.
sns.lmplot(x = 'petal length (cm)', y = 'petal width (cm)', data = df, hue = 'target_name', col = 'target')
plt.savefig('ImageFolder/lmppltsepal.png')
plt.show()