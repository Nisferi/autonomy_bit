# physics/quantum.py

import numpy as np

def collapse(state_amplitudes):
    probs = np.abs(state_amplitudes) ** 2
    probs /= probs.sum()
    return np.random.choice(len(state_amplitudes), p=probs)
