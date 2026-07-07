"""Headless smoke test for BlueVenture.

Runs with dummy SDL drivers so it can execute in CI / without a display.
It constructs every game entity (including the new round-3 content) and runs
their update/draw loops for a number of frames to catch asset-key or logic
regressions without needing a human at the keyboard.
"""
import os
import sys

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

# Run from the project root so relative asset paths resolve.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, ROOT)

import pygame

pygame.init()
WIDTH, HEIGHT = 1152, 768
window = pygame.display.set_mode((WIDTH, HEIGHT))

from game.enemy import (
    AngryPig,
    Bat,
    BlueBird,
    Bunny,
    Chameleon,
    Chicken,
    FatBird,
    Ghost,
    Mushroom,
    Radish,
    Rino,
    Slime,
    Snail,
    Turtle,
)
from game.object import Block, Box, Brick, Fire, Goal, Item, Saw, Spikes, Trampoline
from game.player import NPC, Player

FPS = 60
block_size = 96

player = Player(100, 100, 50, 50, "VirtualGuy")
npc = NPC(3000, HEIGHT - block_size * 5, 50, 50, "PinkMan")

enemies = [
    Bat(600, block_size, 50, 50, "Bat"),
    Rino(1800, 400, 50, 50, "Rino"),
    Chameleon(2200, 400, 50, 50, "Chameleon"),
    FatBird(6000, 100, 40, 48, "FatBird"),
    Ghost(7000, 400, 50, 50, "Ghost"),
    Chicken(8800, 600, 50, 50, "Chicken"),
    AngryPig(9800, 600, 50, 50, "AngryPig"),
    Slime(10500, 600, 50, 50, "Slime"),
    Snail(11000, 620, 50, 50, "Snail"),
    Mushroom(11200, 600, 50, 50, "Mushroom"),
]

pets = [
    BlueBird(-135, 530, 50, 50, "BlueBird"),
    Turtle(1300, 140, 50, 50, "Turtle"),
    Bunny(-115, 300, 50, 50, "Bunny"),
    Radish(-180, 310, 50, 50, "Radish"),
]

fruit_names = ["Apple", "Bananas", "Kiwi", "Melon", "Pineapple", "Cherries", "Orange", "Strawberry"]
items = [Item(200 + i * 60, 300, 32, 32, name) for i, name in enumerate(fruit_names)]

trampolines = [Trampoline(block_size * 100, HEIGHT - block_size - 56)]
boxes = [Box(block_size * 95, HEIGHT - block_size * 2 - 48, 48, kind) for kind in ("Box1", "Box2", "Box3")]
goal = Goal(block_size * 119, HEIGHT - block_size - 128, 64, 64)

obstacles = [Fire(400, 600, 16, 32), Saw(500, 600, 38, 38), Spikes(700, 600, 16, 16)] + trampolines + boxes + [goal]
objects = [Block(0, 600, block_size), Brick(200, 400, 96, 18)] + obstacles

# Exercise the special interactions.
trampolines[0].bounce()
boxes[0].break_open()
goal.press()

frames = 150
for frame in range(frames):
    player.loop(FPS)
    npc.loop(FPS)
    for pet in pets:
        pet.loop(FPS)
    for enemy in enemies:
        enemy.loop(FPS)
    for obs in obstacles:
        obs.loop()
    for item in items:
        item.loop(FPS)

    window.fill((0, 0, 0))
    for obj in objects:
        obj.draw(window, 0)
    for enemy in enemies:
        enemy.draw(window, 0)
    for item in items:
        item.draw(window, 0)
    for pet in pets:
        pet.draw(window, 0)
    player.draw(window, 0)
    npc.draw(window, 0)

print(f"OK: ran {frames} frames with {len(enemies)} enemies, "
      f"{len(items)} items, {len(objects)} objects without errors.")
pygame.quit()
