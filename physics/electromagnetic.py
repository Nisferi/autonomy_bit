# physics/electromagnetic.py

import numpy as np

def compute_potential(charges, positions):
    pot = np.zeros(len(positions))
    for i, (qi, ri) in enumerate(zip(charges, positions)):
        for j, (qj, rj) in enumerate(zip(charges, positions)):
            if i == j: continue
            r = np.linalg.norm(ri - rj)
            if r > 0:
                pot[i] += qj / r
    return pot

def compute_force(charges, positions):
    forces = np.zeros_like(positions)
    for i, (qi, ri) in enumerate(zip(charges, positions)):
        for j, (qj, rj) in enumerate(zip(charges, positions)):
            if i == j: continue
            diff = ri - rj
            r = np.linalg.norm(diff)
            if r > 0:
                forces[i] += qi * qj * diff / (r**3)
    return forces
