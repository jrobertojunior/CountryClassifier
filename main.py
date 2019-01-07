import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns


def header(msg):
    print(f'\n*** {msg} ***')


def plot(x, y):
    sns.lmplot(x=x, y=y, data=dataset, hue='HDI Target',
               palette='Set1', fit_reg=False, scatter_kws={"s": 70})


def evaluate(predict, target):
    sucess = 0
    offset = len(predict)
    count = 0
    for value in predict:
        #print(count)
        if (value == target.iloc[offset + count - 1]):
            sucess += 1
        count += 1

    return sucess / len(predict)

dataset = pd.read_csv("datasets/dataset2.csv")

# creating dataset
data = dataset[['Freedom', 'GDP per Capita', 'Trade Freedom',
                'Business Freedom', 'Tax Burden % of GDP',
                'Gov Expenditure % of GDP']]
target = dataset['HDI Target']

# country codes
codes = dataset['Code']

indicators = dataset.keys()
indicators = indicators[3:]

# plot graphs
for indicator in indicators:
    if indicator == 'Population' or indicator == 'GDP per Capita':
        continue
    #plot(indicator, 'HDI')

half = len(data) >> 1
# create scaler
scaler = StandardScaler()
scaler.fit(data)
scaler.transform(data)

print(data['GDP per Capita'].max())
# print(data2[0:10])



# crate svm
'''
C = [10**x for x in range(4)]
count = False
for c in C:
    if (count is False):
        #print(data2[:half])
        count = True

    clf = svm.SVC(C=c, gamma='scale')
    clf.fit(data2[:half], target[:half])
    predict = clf.predict(data2[half:])
    print(predict)
    print(evaluate(predict, target))
'''
c = 10000
clf = svm.SVC(C=c, gamma='scale')
clf.fit(data[:half], target[:half])
predict = clf.predict(data[half:])
print(predict)
print(evaluate(predict, target))


plt.show()
