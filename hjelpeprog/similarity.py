import math

matrix = {
    1: [1, 2, 0, 0, 0, 0],
    2: [1, 0, 1, 1, 1, 0],
    3: [3, 0, 0, 0, 0, 3],
    4: [2, 4, 0, 0, 0, 0]
}

def sim_smc(x, y):
    matches = 0
    for idx, val in enumerate(x):
        if x[idx] == y[idx]:
            matches += 1
    return matches / len(x)

def sim_jaccard(x, y):
    matches = 0
    nonzeros = 0
    for idx, val in enumerate(x):
        if x[idx] + y[idx] > 0:
            nonzeros += 1
            if x[idx] and y[idx] > 0:
                matches += 1
    return matches / nonzeros

def sim_cosine(x,y):
    sim = 0
    top = 0
    botx = 0
    boty = 0
    for idx, val in enumerate(x):
        top += x[idx] * y[idx]
        botx += math.pow(x[idx], 2)
        boty += math.pow(y[idx], 2)
    botx = math.sqrt(botx)
    boty = math.sqrt(boty)
    sim = top / (botx * boty)
    return sim


print("1vs2")
print("Jaccard")
print(sim_jaccard(matrix[1], matrix[2]))
print("cosine")
print(round(sim_cosine(matrix[1], matrix[2]), 3))
print("1vs3")
print("Jaccard")
print(sim_jaccard(matrix[1], matrix[3]))
print("cosine")
print(round(sim_cosine(matrix[1], matrix[3]), 3))
print("1vs4")
print("Jaccard")
print(sim_jaccard(matrix[1], matrix[4]))
print("cosine")
print(round(sim_cosine(matrix[1], matrix[4]),3))

