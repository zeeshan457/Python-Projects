import matplotlib.pyplot as plt
import pandas as pd

# Initialize the lists for X and Y
file = "C:\\Users\\zeeshan\\Desktop\\Solar_Flares_Dataset.xlsx"

df = pd.read_excel(file)
plt.bar(x=df['X-class flares'],
        height=df['largest spot size'])

plt.title("X_CLass Flares & largest spot size")
plt.xlabel("X_CLass Flares")
plt.ylabel("largest spot size")

# Show the plot
plt.show()




