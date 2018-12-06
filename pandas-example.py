import pandas as pd
import Dataset
import Country


def header(msg):
    print(f'\n*** {msg.upper()} ***')

countries = []
countries_code = {}

countries_code = pd.read_csv("datasets/meta.csv")
print(countries_code.keys())
countries_code = countries_code[['Country Code', 'TableName']]
header("countries code")
print(countries_code)
hid = pd.read_csv("datasets/hid.csv")
"""
header("dtypes")
print(countries_code.dtypes)
header("index")
print(countries_code.index)
header("columns")
print(countries_code.columns)
header("values")
# print(countries_code.values)
header("describe()")
print(countries_code.describe())
"""

header("hid")
# print(hid.describe())
header("HID table")
print(hid)
# header("sorted")
# print(hid.sort_values('2017', ascending=False))
# header("HID table 2")
# print(hid)
header("2017 column")
print(hid['2017'].head())
header("a few countries")
print(hid[3:10])
header("multiple columns")
print(hid[['1997', '2007', '2017']].head())

header("creating new data frames")
new_hid = hid[['HDI Rank (2017)', 'Country', '2007']]
print(new_hid.head())
print(new_hid.tail())

header("assignment")
new_hid.loc[2, ['Country']] = "Fake Country"
print(new_hid.loc[2, ['Country']])
