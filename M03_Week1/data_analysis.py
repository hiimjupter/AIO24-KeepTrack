import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


DATAPATH = "M03_Week1/IMDB-Movie-Data.csv"
df = pd.read_csv(DATAPATH)

# df.info()  # Lack of data in Revenue (Millions): 1000-872 and Metascore: 1000-936
# "Title" or "Rank" column could be seen as the indexed column <-> they don't contain duplicate values
# print(df.head(5))

# new_df = pd.read_csv(DATAPATH, index_col="Rank")
# print(new_df.head(5))

# print(df.describe())


# Check missing values:
# print(df.isnull().sum())

# Fill in missing values
df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].mean(), inplace=True)
df['Metascore'].fillna(df['Metascore'].mean(), inplace=True)

# print(df.isnull().sum()) # --> no more n/a values
print(df.describe())


def apply_rating(rating):
    if rating >= 7.5:
        return "Good"
    elif rating >= 5.0 and rating < 7.5:
        return "Average"
    else:
        return "Bad"


def apply_revenue(revenue):
    if revenue >= 100:
        return "Profitable project"
    elif revenue >= 50 and revenue < 100:
        return "Breakeven project"
    else:
        return "Loss project"


df["Rate"] = df["Rating"].apply(apply_rating)
df["ROI"] = df["Revenue (Millions)"].apply(apply_revenue)
print(df.tail())
