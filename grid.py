# grid.py

import threading
import numpy as np
from particles import PARTICLE_DATA
from physics.electromagnetic import compute_force as em_force
from physics.gravitational import compute_gravity
from physics.strong import strong_force
from physics.weak import try_beta_decay
from physics.virtual_particles import VirtualExchange
from physics.quantum_effects import tunnel

class SparseGrid:
    def __init__(self, size=100):
        self.size = size
        self.cells = {}
        self.paused = True
        self.lock = threading.Lock()
        self.vp_manager = VirtualExchange()

    def randomize(self, density=0.1):
        import random
        for x in range(self.size):
            for y in range(self.size):
                if random.random() < density:
                    ptype = random.choice(list(PARTICLE_DATA.keys()))
                    self.cells[(x,y)] = {
                        'type': ptype,
                        **PARTICLE_DATA[ptype],
                        'pos': np.array([x, y], float),
                        'vel': np.zeros(2),
                        'energy': 0
                    }

    def step_physics(self):
        with self.lock:
            positions = np.array([p['pos'] for p in self.cells.values()])
            charges = np.array([p['charge'] for p in self.cells.values()])
            masses = np.array([p['mass'] for p in self.cells.values()])

            f_em = em_force(charges, positions)
            f_gr = compute_gravity(masses, positions)

            for idx, p in enumerate(list(self.cells.values())):
                total_force = f_em[idx] + f_gr[idx]
                decayed, child1, child2 = try_beta_decay(p)
                if decayed:
                    del self.cells[tuple(p['pos'])]
                    self.cells[tuple(p['pos'])] = {**PARTICLE_DATA[child1], 'pos': p['pos'], 'vel': p['vel']}
                    continue

                if tunnel(p, barrier_height=1e-20, width=1.0):
                    p['pos'] += p['vel']

                accel = total_force / p['mass']
                p['vel'] += accel
                p['pos'] += p['vel']

    def step(self):
        if not hasattr(self, '_thread') or not self._thread.is_alive():
            self._thread = threading.Thread(target=self.step_physics)
            self._thread.start()
