# physics/gravitational.py

import numpy as np

G = 6.67430e-11

def compute_gravity(masses, positions):
    forces = np.zeros_like(positions)
    for i, (mi, ri) in enumerate(zip(masses, positions)):
        for j, (mj, rj) in enumerate(zip(masses, positions)):
            if i == j: continue
            diff = ri - rj
            r = np.linalg.norm(diff)
            if r > 0:
                forces[i] += -G * mi * mj * diff / (r**3)
    return forces
