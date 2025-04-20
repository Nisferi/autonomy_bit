# physics/quantum_effects.py

import random
import math
from physics.quantum import collapse

def tunnel(particle, barrier_height, width):
    m = particle['mass']
    E = particle.get('energy', 0)
    if E >= barrier_height:
        return True
    kappa = math.sqrt(2*m*(barrier_height - E)) / 1.054e-34
    prob = math.exp(-2 * kappa * width)
    return random.random() < prob

def superposition(states):
    idx = collapse(states)
    return idx
