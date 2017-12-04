import math
from collections import Counter

TOTAL_RECORDS = 14

def entropy(C1, C2):
    """Entropy of a list of records associated with a node."""
    n = C1 + C2
    PC1 = C1/n
    PC2 = C2/n
    if PC1 == 0:
        ent = 0 - PC2 * math.log(PC2, 2)
    elif PC2 == 0:
        ent = - PC1 * math.log(PC1, 2) - 0
    else:
        ent = - PC1 * math.log(PC1, 2) - PC2 * math.log(PC2, 2)
    return ent

def infogain(m, C1, C2):
    childEntropy = entropy(C1, C2)
    n = C1 + C2

    return ((n/m) * childEntropy)


print(entropy(1001,1001))
print(entropy(1,5))
print(entropy(2, 4))

infogainVal = 0
infogainVal += infogain(5, 1, 2)
infogainVal += infogain(5, 2, 0)


infogainVal = 0.97 - infogainVal
print(infogainVal)
