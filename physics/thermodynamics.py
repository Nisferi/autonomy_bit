# physics/thermodynamics.py

import numpy as np

def shannon_entropy(distribution):
    p = np.array(distribution)
    p = p[p > 0]
    return -np.sum(p * np.log2(p))
