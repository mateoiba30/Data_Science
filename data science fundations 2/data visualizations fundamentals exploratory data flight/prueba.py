import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math


## Read in Data
flight = pd.read_csv("flights.csv")
#flight = flight.head(1000)
#print(flight.head())
#print(flight.info())
#print(flight.inflight_meal.unique())
int_meal = flight.apply(lambda row: 1 if row['inflight_meal']=='Yes' else 0, axis=1)
print(int_meal)

plt.boxplot([int_meal, flight.coach_price])
plt.show()
plt.xlabel("with meal or not")
plt.ylabel("Price")
plt.clf()

#print(flight[flight.inflight_meal == 'No'])