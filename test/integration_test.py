"""Drive the real main() game loop headless for a fixed number of frames.

We hold the RIGHT arrow so the player actually moves, collides, collects
fruit and jumps, then stop via a sentinel exception raised from a patched
display.update(). This catches runtime regressions in the live loop
(handle_move, collisions, trampoline/box handling, HUD drawing, background
switching) that the pure construction smoke test cannot.
"""
import asyncio
import os
import sys

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, ROOT)

import pygame

import main

FRAMES = 400


class _Stop(Exception):
    pass


class _Keys:
    """Pretend RIGHT and SPACE are held so the player runs and jumps."""
    def __getitem__(self, key):
        return key in (pygame.K_RIGHT, pygame.K_SPACE)


_count = {"n": 0}
_real_update = pygame.display.update


def _fake_update(*args, **kwargs):
    _real_update(*args, **kwargs)
    _count["n"] += 1
    if _count["n"] >= FRAMES:
        raise _Stop()


pygame.display.update = _fake_update
main.pygame.key.get_pressed = lambda: _Keys()

window = pygame.display.set_mode((main.WIDTH, main.HEIGHT))

try:
    asyncio.run(main.main(window))
except _Stop:
    print(f"OK: main() ran {_count['n']} live frames without crashing.")
except SystemExit:
    print(f"OK: main() exited cleanly after {_count['n']} frames.")
finally:
    pygame.quit()
