import pandas as pd
import math
import copy

def hasNan(alist):
    firstLoop = True
    for item in alist:
        if firstLoop is True:
            firstLoop = False
            continue

        x = float(item)
        if math.isnan(x):
            return True

dataframe = pd.DataFrame()

codes = pd.read_csv("datasets/codes.csv")
hdi = pd.read_csv("datasets/hdi.csv")
freedom = pd.read_csv('datasets/economics-freedom.csv')

data = []

codes_dict = dict(zip(codes['Name'], codes['Code']))

new_hdi = hdi.set_index('Country')
for index, row in new_hdi.iterrows():
    if index in codes_dict:
        score = round(row['2017'], 3)

        target = 0
        if score >= 0.8:
            target = 1
        else:
            target = 0

        data.append([codes_dict[index], score, target])

new_freedom = freedom.set_index('Country Name')
for index, row in new_freedom.iterrows():
    if index in codes_dict:
        code = codes_dict[index]
        score = round(row['2018 Score'], 3)
        population = row['Population (Millions)']
        gdp_capita = row['GDP per Capita (PPP)']
        trade_freedom = row['Trade Freedom']
        business_freedom = row['Business Freedom']
        tax_gdp = row['Tax Burden % of GDP']
        gov_spends_gdp = row['Gov Expenditure % of GDP']

        gdp_capita = str(gdp_capita)
        gdp_capita = str(gdp_capita.strip('$').replace(',', ''))

        if math.isnan(score) is False:
            count = 0
            for v in data:
                if v[0] == code:
                    data[count].append(score)
                    data[count].append(population)
                    data[count].append(gdp_capita)
                    data[count].append(trade_freedom)
                    data[count].append(business_freedom)
                    data[count].append(tax_gdp)
                    data[count].append(gov_spends_gdp)

                    break
                else:
                    count += 1


labels = ['Code', 'HDI', 'HDI Target', 'Freedom', 'Population',
          'GDP per Capita', 'Trade Freedom', 'Business Freedom',
          'Tax Burden % of GDP', 'Gov Expenditure % of GDP']

count = 0
for row in data:
    if len(row) < len(labels) or row[0] == 'LIE':  # TODO: nao esta reconhecendo LIE
        data.pop(count)

    count += 1

data2 = copy.deepcopy(data)

for i in range(len(data2)):
    score = data2[i][1]

    if score >= 0.8:
        data2[i][2] = 2
    elif score >= 0.7:
        data2[i][2] = 1
    else:
        data2[i][2] = 0

# print(data)


# labels = ['Code', 'HDI', 'Freedom', 'Population', 'GDP per Capita']
df = pd.DataFrame(data, columns=labels)
df2 = pd.DataFrame(data2, columns=labels)

print(df.head())
print(df2.head())

df.to_csv("datasets/dataset.csv", index=False)
df2.to_csv("datasets/dataset2.csv", index=False)

df3 = df[['Freedom', 'GDP per Capita', 'Trade Freedom', 'HDI Target']]
df3.to_csv("datasets/dataset3.csv", index=False)
