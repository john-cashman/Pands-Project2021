import matplotlib.pyplot as plt
import numpy as np

minSalary = 20000
maxSalary = 80000
numberEntries = 100

np.random.seed(1) # seed makes sure that the randomly generated numbers are the same each time this allows for easier debugging
salaries = np.random.randint(minSalary,maxSalary,numberEntries)
ages = np.random.randint( low = 21, high = 65, size = numberEntries)
plt.scatter(ages, salaries, label = "Salaries")

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints,ypoints, color= 'r', label = "x squared")

plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()
plt.show()
plt.savefig('prettier-plt.png')