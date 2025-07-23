import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('mtcars.csv')
plt.boxplot(df['mpg'],vert=False)
plt.title('Box Plot of MPG')
plt.ylabel('MPG')
plt.show()