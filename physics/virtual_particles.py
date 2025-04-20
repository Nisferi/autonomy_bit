# physics/virtual_particles.py

from collections import deque

class VirtualExchange:
    """
    Менеджер виртуальных частиц для обменных взаимодействий.
    """
    def __init__(self):
        self.pool = deque()

    def create(self, type_, momentum):
        vp = {'type': type_, 'momentum': momentum}
        self.pool.append(vp)
        return vp

    def consume(self):
        return self.pool.popleft() if self.pool else None
