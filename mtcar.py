import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('mtcars.csv')
print(df.head(5))


plt.hist(df['mpg'], bins=10, edgecolor='black')
plt.title('Histogram of MPG')
plt.xlabel('MPG')
plt.ylabel('Frequency')
plt.show() 


plt.scatter(df['wt'], df['mpg'])
plt.title('Weight vs MPG')
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show() 


print("Min MPG:", df['mpg'].min())
print("Max MPG:", df['mpg'].max())
