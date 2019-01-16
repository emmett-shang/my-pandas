import pandas as pd
import matplotlib.pylab as plt
data = pd.read_csv("unmatched_plays.csv")
print(data.head(5))
#print(data['variance_num_of_plays'].value_counts())

print(data['variance_num_of_plays'].describe())

mean_by_date =data.groupby('Date')['variance_num_of_plays'].mean()
count_by_date = data['Date'].value_counts()

stats_by_date = pd.DataFrame({'mean_by_date': mean_by_date, 'count_by_date': count_by_date})
stats_by_date.plot()
plt.show()
data['variance_num_of_plays'].hist(bins=200)
#plt.show()
print("")