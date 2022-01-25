import pandas as pd

df = pd.read_csv("file_name")

print(df.dtypes)

#.describe() for summary

print(df["numberOfDays"]) #to print a column

fdf = df[df["numberOfDays"] < 25] #filters it to onlt rows less than 25

fdff = df[(df["numberOfDays"] < 25) & (df["usage"] == 1)]
