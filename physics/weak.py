# physics/weak.py

import random

def try_beta_decay(particle):
    # Упрощённое β-распад: шанс на распад ~ e^{-t/lifetime}
    import math
    if random.random() < 0.01:  # примерный шанс
        # вернуть две дочерние частицы
        return True, 'neutrino', 'electron'
    return False, None, None

def flavor_change(quark):
    # Смена "вкуса" кварка
    flavors = ['up', 'down', 'strange', 'charm', 'bottom', 'top']
    return random.choice(flavors)
