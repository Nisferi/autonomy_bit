# simulation.py

from grid import SparseGrid
from ui import UI
from sound import init_sound

def main():
    grid = SparseGrid(size=100)
    grid.randomize(density=0.05)

    ui = UI(grid)
    sounds = init_sound()

    while ui.running:
        cmd = ui.poll()
        if cmd == 'start':
            grid.paused = False
        elif cmd == 'pause':
            grid.paused = True
        elif cmd == 'faster':
            pass
        elif cmd == 'slower':
            pass
        elif cmd == 'save':
            pass
        elif cmd == 'load':
            pass

        if not grid.paused:
            grid.step()

        ui.render()

    ui.cleanup()

if __name__ == "__main__":
    main()
