
import matplotlib.pyplot as plt 
import seaborn as sns

df = sns.load_dataset('iris') 
df.head
sns.boxplot( y=df["sepal_length"] );
plt.show()





#references: https://seaborn.pydata.org/generated/seaborn.boxplot.html