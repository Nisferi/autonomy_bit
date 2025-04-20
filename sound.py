# sound.py

import pygame
import os

def init_sound():
    pygame.mixer.init()
    base = os.path.dirname(__file__)
    sounds = {
        'decay': pygame.mixer.Sound(os.path.join(base, 'decay.wav')),
        'binding': pygame.mixer.Sound(os.path.join(base, 'binding.wav')),
        'collision': pygame.mixer.Sound(os.path.join(base, 'collision.wav')),
    }
    return sounds
