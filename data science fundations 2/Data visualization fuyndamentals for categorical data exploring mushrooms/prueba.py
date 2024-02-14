import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# load in the data
df = pd.read_csv("mushroom_data.csv")
#print(df.head())
#print(df.info())#solo bruises es null, el resto son strings. Si bien no hay nulos hay que revisar los strings
#todo categórico, se puede hacer uno más gráficos de barras de cualquier variable

# list of all column headers
columns = df.columns.tolist()

for column in columns:
    df[column] = pd.factorize(df[column])[0]
    sns.countplot(df[column])
    plt.show()
    plt.clf()