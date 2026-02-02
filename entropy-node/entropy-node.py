import numpy as np

def entropy_node(y):
    if len(y) == 0:
        return 0.0

    hs = 0.0
    psa = {}

    for i in y:
        psa[i] = psa.get(i, 0) + 1

    n = float(len(y))

    for j in psa.values():
        p = j / n         
        hs -= p * np.log2(p)

    return max(hs, 0.0)    