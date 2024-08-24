import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

DATA_PATH = 'M03_Week1/opsd_germany_daily.csv'
# df = pd.read_csv(DATA_PATH, index_col='Date')

# print(df.info())  # quite many NaN values
# print(df.dtypes)
# print(df.shape)  # 4383 row, 4 column
# df = pd.read_csv(DATA_PATH, index_col=0)
# print(df.sample(5, random_state=0))

df = pd.read_csv(DATA_PATH, index_col=0, parse_dates=True)

df['Year'] = df.index.year
df['Month'] = df.index.month
df['Date'] = df.index.day
df['Weekday'] = df.index.day_name()
# print(df.sample(5, random_state=0))

# Time-based indexing
# print(df.loc['2008-10-01':'2008-11-30'].head())

# Visualizing
# sns.set(rc={'figure.figsize': (11, 4)})
# df['Consumption'].plot(linewidth=0.5)

# cols_plot = ['Consumption', 'Wind+Solar']
# axes = df[cols_plot].plot(marker='.', alpha=0.5,
#                           linestyle='None', figsize=(11, 9), subplots=True)

# for ax in axes:
#     ax.set_ylabel('Daily Totals (GWh)')
# plt.show()
# Conclusion: Solar and Wind are put into production from 2010 and 2012 respectively. Both contributes to approximately 20% energy supply


# Seasonality
# fig, axes = plt.subplots(3, 1, figsize=(11, 10), sharex=True)
# for name, ax in zip(['Consumption', 'Solar', 'Wind'], axes):
#     sns.boxplot(data=df, x='Month', y=name, ax=ax)
#     ax.set_ylabel('GWh')
#     ax.set_title(name)
#     # Remove the automatic x-axis label from all but the bottom subplot
#     if ax != axes[-1]:
#         ax.set_xlabel('')
# Conclusion: Consumption reaches its peak during winter and spring (cold weather) while reducing during summer.
# Summer is the month with the largest production of Solar energy while the other seasons are better for producing Wind energy
# plt.show()

# Frequencies:
# print(pd.date_range('2008-10-10', '2008-11-01', freq='D'))
# times_sample = pd.to_datetime(['2013-02-03', '2013-02-06', '2013-02-08'])
# consum_sample = df.loc[times_sample, ['Consumption']].copy()

# consum_freq = consum_sample.asfreq('D')
# consum_freq['Consumption - FFill'] = consum_sample.asfreq('D', method='ffill')
# print(consum_freq)


# Resampling --> Generalize and group data into bigger time duration (downsampling)
data_columns = ['Consumption', 'Wind', 'Solar', 'Wind+Solar']
# df_mean = df[data_columns].resample('W').mean()
# df_month = df_mean[data_columns].resample('M').mean()

# Visualize daily vs weekly data
# start, end = '2017-01', '2017-07'
# fig, ax = plt.subplots()
# ax.plot(df.loc[start:end, 'Solar'], marker='.',
#         linestyle='-', linewidth=0.5, label='Daily')
# ax.plot(df_mean.loc[start:end, 'Solar'], marker='o',
#         markersize=8, label='Weekly Mean')
# ax.plot(df_month.loc[start:end, 'Solar'], marker='x',
#         markersize=8, label='Monthly Mean')
# ax.set_ylabel('Solar Production (GWh)')
# ax.legend()
# plt.show()

# Calculate fraction
# df_annual = df[data_columns].resample('Y').sum(min_count=360)
# df_annual = df_annual.set_index(df_annual.index.year)
# df_annual.index.name = 'Year'

# df_annual['Wind+Solar/Consumption'] = df_annual['Wind+Solar'] / \
#     df_annual['Consumption']
# print(df_annual.tail(3))

# Visualizing Wind+Solar/Consumption from 2012 when both are put into production
# ax = df_annual.loc[2012:, 'Wind+Solar/Consumption'].plot.bar()
# ax.set_ylabel('Renewable Production/Consumption')
# ax.set_ylim(0, 0.3)
# ax.set_title('Wind + Solar Share of Annual Electricity Consumption')
# plt.xticks(rotation=0)
# plt.show()


# Rolling windows
df_7d = df[data_columns].rolling(7, center=True).mean()
print(df_7d.head(14))

df_365d = df[data_columns].rolling(
    window=365, center=True, min_periods=360).mean()

# fig, ax = plt.subplots()
# ax.plot(df['Consumption'], marker='.', markersize=2,
#         color='0.6', linestyle=None, label='Daily')
# ax.plot(df_7d['Consumption'], linewidth=2, label='7-d Rolling Mean')
# ax.plot(df_365d['Consumption'], color='0.2',
#         linewidth=3, label='Trend (365-d Rolling Mean)')

fig, ax = plt.subplots()
for nm in ['Wind', 'Solar', 'Wind+Solar']:
    ax.plot(df_365d[nm], label=nm)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.set_ylim(0, 400)
    ax.legend()
    # ax.set_xlabel('Year')
    ax.set_ylabel('Production (GWh)')
    ax.set_title('Trends in Electricity Production (365-d Rolling Means)')
plt.show()
