
import pandas as pd

data = pd.read_csv("iris_csv.csv") 




sum = data["sepallength"].sum()
mean = data["sepallength"].mean()
median = data["sepallength"].median()


print(sum,mean,median)





# print(data)
# print(data["sepallength"].sum())
# print(sum)
# print(data["sepallength"].sum())
# print(data["sepallength"].mean())
# print(data["sepallength"].median())





# print("Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data)
# print(data.head(11))
# print(data.sample(20))
# print(data.columns)
# print(data.shape)