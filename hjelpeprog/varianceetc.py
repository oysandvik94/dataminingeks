import math
import numpy as np
import statistics

values = [17, 5, 3, 9, 49, 53, 11]

def mean(values):
    return sum(values)/len(values) if len(values) > 0 else 0

def median(values):
    values = sorted(values)
    return statistics.median(values)

def list_range(values):
    values = sorted(values)
    return values[-1] - values[0]

def variance(values):
    sum_v = 0
    m = mean(values)
    for item in values:
        sum_v += math.pow(item - m, 2)
    return sum_v/(len(values)-1)

def aad(values):
    sum_aad = 0
    m = mean(values)
    for item in values:
        sum_aad += abs(item - m)
    return sum_aad/len(values)

def mad(values):
    mad_list = []
    m = mean(values)
    for item in values:
        mad_list.append(abs(item - m))
    return median(mad_list)

def iqr(values):
    return np.percentile(values, 75) - np.percentile(values, 25)

def percentilema(values, perc):
    values = sorted(values)
    valuesnump = np.array(values)
    val = np.percentile(valuesnump, perc)
    for item in values:
        if item > val:
            return item

print("Percentile: ")
print(percentilema(values, 70))
print("\nRange")
print(list_range(values))
print("\nMedian:")
print(median(values))
print("\nMean")
print(mean(values))
print("\nVariance")
print(variance(values))
print("\nAAD")
print(aad(values))

print(help(np.percentile))
