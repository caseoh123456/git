import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('IRIS.csv')

plt.plot( df['sepal_length'], 'o-r', label='Sepal Length')
plt.plot( df['sepal_width'], 'o-b', label='Sepal Width')

plt.title('Sepal Measurements')
plt.xlabel('Sample ID')
plt.ylabel('Length (cm)')
plt.legend()
plt.show()
