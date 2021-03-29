import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

sns.set()

print('done')


from sklearn import datasets  # I pip installed sklearn and imported the dataset from here.
data = datasets.load_iris()


df = pd.DataFrame(data["data"], columns=data["feature_names"])




# first I set a variable named col and equal it to the column I want to use for the histogram. Then  I pass it into the histogram and finaly use it to make a title for the histogram. The final part I am saving the histogram as an image so it saves elsewhere in my directory.
col = "sepal length (cm)"
df[col].hist( color = "green")  # I could have also used Matplotlib here with plt.hist
plt.suptitle('Sepal Length in CM')
plt.xlabel("sepal Length in cm")
plt.ylabel("count")
plt.savefig('ImageFolder/SepalLengthHist.png')   #This saves the image to my image folder. 
# plt.show()



# Sepal Width
col = "sepal width (cm)"
df[col].hist( color = "Red")  
plt.suptitle('Sepal Width in CM')
plt.xlabel("sepal Width in cm")
plt.ylabel("count")
plt.savefig('ImageFolder/SepalWidthHist.png')   
# plt.show()





# Petal Length
col = "petal length (cm)"
df[col].hist( color = "Yellow")  
plt.suptitle('Petal Length in CM')
plt.xlabel("Petal Length in cm")
plt.ylabel("count")
plt.savefig('ImageFolder/PetalLengthHist.png')   
# plt.show()



# Petal Width
col = "petal width (cm)"
df[col].hist( color = "Blue")  
plt.suptitle('Petal Length in CM')
plt.xlabel("Petal Width in cm")
plt.ylabel("count")
plt.savefig('ImageFolder/PetalWidthHist.png')   
# plt.show()
