import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')
sns.lineplot(data=df, x='dia', y='venda')
plt.savefig('gasolina.png')