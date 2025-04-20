# physics/strong.py

import numba
import numpy as np

@numba.njit
def strong_force(dx, dy):
    # Упрощённая модель цветовой силы
    r2 = dx*dx + dy*dy + 1e-12
    magnitude = np.exp(-r2)  # пример
    return magnitude * dx / np.sqrt(r2), magnitude * dy / np.sqrt(r2)
