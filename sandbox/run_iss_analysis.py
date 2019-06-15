import pandas.util.testing as tm

from dateutil.relativedelta import relativedelta, FR
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

# load data 
file_name = 'ISS-Full-Results.xlsx'
df = pd.read_excel(
        file_name,
        index_col='time',
        parse_dates={'time':['Time']},
        date_parser=lambda x: pd.datetime.strptime(x, '%H:%M:%S')
        )

print(df)

# plot data
f, axes = plt.subplots(3,1)

ax = sns.lineplot(x=df.index, y='humidity', marker='o', markersize=10, color='lightblue', legend=False, data=df, ax = axes[0])
# ax.set_xticklabels([x.strftime('%H:%M:%S') for x in df.index])
ax.legend(handles=ax.lines[::len(df)+1], labels = ['humidity'], loc = 'upper-left')
ax.set_title('ISS Results')
ax = sns.lineplot(x=df.index, y='temperature', marker='d', markersize=10, data=df, color='purple', ax = axes[1])
# ax.set_xticklabels([x.strftime('%H:%M:%S') for x in df.index])
ax.legend(handles=ax.lines[::len(df)+1], labels = ['temperature'], loc = 1)
ax = sns.lineplot(x=df.index, y='pressure',marker='^', markersize=10, data=df, color='pink', ax = axes[2])
# ax.set_xticklabels([x.strftime('%H:%M:%S') for x in df.index])
ax.legend(handles=ax.lines[::len(df)+1], labels = ['pressure'], loc = 1)
plt.show()

