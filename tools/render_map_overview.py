"""Render a full-map overview image of the BlueVenture level layout."""
import os
import sys

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, ROOT)

import pygame

WIDTH, HEIGHT = 1152, 768
block_size = 96
PINK_X = 2500
GREEN_X = block_size * 90


def rects_block(x, y, size=96):
    return pygame.Rect(x, y, size, size)


def build_level():
    """Return (objects, enemies, items, landmarks) as lists of (rect, kind)."""
    objects = []
    enemies = []
    items = []
    landmarks = []

    def add_object(rect, kind="block"):
        objects.append((rect, kind))

    def add_enemy(rect):
        enemies.append(rect)

    def add_item(rect):
        items.append(rect)

    # Walls & floor
    for i in range(0, HEIGHT // block_size):
        add_object(rects_block(0, i * block_size), "block")
    for i in range(-WIDTH // block_size, 44):
        add_object(rects_block(i * block_size, HEIGHT - block_size), "block")
    for i in range(0, HEIGHT // block_size):
        add_object(rects_block(25 * block_size, i * block_size), "block")
    for i in range(-WIDTH // block_size, 44):
        add_object(rects_block(i * block_size, 0), "block")

    for i in range(0, 6):
        add_object(pygame.Rect(block_size * 4 + i * 96, HEIGHT - block_size * 5 - 30, 96, 18), "brick")

    # Round 1
    for i in range(1, 4):
        add_object(rects_block(block_size * i, HEIGHT - block_size * (i + 1)))
    for dx in (-1, -2, -3):
        add_object(rects_block(dx * block_size, HEIGHT - 4 * block_size))
    add_object(rects_block(-3 * block_size, HEIGHT - 3 * block_size))
    add_object(rects_block(-3 * block_size, HEIGHT - 2 * block_size))
    for i in range(10, 13):
        add_object(rects_block(block_size * i, HEIGHT - (14 - i) * block_size))
    add_object(rects_block(block_size * 15, block_size))
    add_object(rects_block(15 * block_size, 2 * block_size))
    for i in range(3, 5):
        add_object(rects_block(15 * block_size, i * block_size))
    for i in range(16, 23):
        add_object(rects_block(i * block_size, 4 * block_size))
    add_object(rects_block(24 * block_size, HEIGHT - 2 * block_size))
    add_object(rects_block(6 * block_size, HEIGHT - 3 * block_size))
    add_object(rects_block(7 * block_size, HEIGHT - 3 * block_size))
    for bx in (13, 16):
        add_object(rects_block(block_size * bx, block_size if bx == 13 else block_size * 3))
    add_object(rects_block(block_size * 13, block_size * 2))
    add_object(rects_block(block_size * 14, block_size * 2))

    # Round 2
    for i in range(2, 6):
        add_object(rects_block(block_size * (28 + i), HEIGHT - block_size * i))
    for i in range(0, 10):
        add_object(rects_block(block_size * (34 + i), HEIGHT - block_size * 5))
    for i in range(0, 16):
        add_object(rects_block(block_size * (60 + i), HEIGHT - block_size), "block2")
    add_object(rects_block(block_size * 47, HEIGHT - block_size * 4))
    add_object(rects_block(block_size * 51, HEIGHT - block_size * 5))
    add_object(rects_block(block_size * 55, HEIGHT - block_size * 3))
    add_object(rects_block(block_size * 65, HEIGHT - block_size * 2), "block2")
    add_object(rects_block(block_size * 67, HEIGHT - block_size * 4), "block2")
    add_object(rects_block(block_size * 58, HEIGHT - block_size * 5))
    for i in range(0, 16):
        add_object(rects_block(block_size * (60 + i), 0), "block2")
    add_object(rects_block(block_size * 68, HEIGHT - block_size * 4), "block2")
    add_object(rects_block(block_size * 69, HEIGHT - block_size * 4), "block2")
    add_object(rects_block(block_size * 75, HEIGHT - block_size * 2), "block2")
    for i in range(0, 3):
        add_object(rects_block(block_size * (76 + i), HEIGHT - block_size * (3 + i)), "block2")
    for i in range(2, 10):
        add_object(rects_block(block_size * (80 + i), HEIGHT - block_size))

    # Round 3 — Green Frontier
    for i in range(90, 120):
        add_object(rects_block(block_size * i, HEIGHT - block_size))
    for i in range(0, HEIGHT // block_size):
        add_object(rects_block(block_size * 120, i * block_size))
    for i in range(0, 3):
        add_object(rects_block(block_size * (93 + i), HEIGHT - block_size * 4))
    add_object(rects_block(block_size * 104, HEIGHT - block_size * 3))
    add_object(rects_block(block_size * 108, HEIGHT - block_size * 4))
    add_object(rects_block(block_size * 116, HEIGHT - block_size * 3))

    # Obstacles
    for x, y, w, h, kind in [
        (-160, HEIGHT - block_size - 64, 16, 32, "fire"),
        (6 * block_size + 80, HEIGHT - 3 * block_size - 64, 16, 32, "fire"),
        (block_size * 67, HEIGHT - block_size * 2 + 64, 16, 16, "spikes"),
        (-80, HEIGHT - block_size - 64, 16, 32, "fire"),
        (block_size * 68, 320, 38, 38, "saw"),
        (block_size * 114, HEIGHT - block_size - 64, 16, 32, "fire"),
    ]:
        add_object(pygame.Rect(x, y, w, h), kind)
    for i in range(0, 8):
        add_object(pygame.Rect(400 + 80 * i, HEIGHT - block_size - 72, 38, 38), "saw")
    for i in range(0, 4):
        add_object(pygame.Rect(1600 + i * 150, HEIGHT - block_size - 64, 16, 32), "fire")
    for i in range(3, 17):
        add_object(pygame.Rect(block_size * 67 + 16 * i, HEIGHT - block_size * 2 + 64, 16, 16), "spikes")
    for i in range(0, 8):
        add_object(pygame.Rect(block_size * 106 + 16 * i, HEIGHT - block_size - 32, 16, 16), "spikes")
    for x in (block_size * 100, block_size * 112):
        add_object(pygame.Rect(x, HEIGHT - block_size - 56, 56, 56), "trampoline")
    for x in (block_size * 95, block_size * 97, block_size * 118):
        add_object(pygame.Rect(x, HEIGHT - block_size * 2 - 48, 48, 48), "box")
    add_object(pygame.Rect(block_size * 119, HEIGHT - block_size - 128, 64, 64), "goal")

    # Enemies
    enemy_positions = [
        (600, block_size, 50, 50),
        (block_size * 19, HEIGHT - block_size * 4 - 68, 50, 50),
        (block_size * 23 + 24, HEIGHT - block_size * 3 + 20, 50, 50),
        (block_size * 35, HEIGHT - block_size * 5 - 68, 50, 50),
        (block_size * 65, 100, 40, 48),
        (block_size * 74, HEIGHT - block_size - 56, 50, 50),
        (block_size * 92, HEIGHT - block_size - 68, 50, 50),
        (block_size * 102, HEIGHT - block_size - 60, 50, 50),
        (block_size * 110, HEIGHT - block_size - 60, 50, 50),
        (block_size * 115, HEIGHT - block_size - 48, 50, 50),
        (block_size * 117, HEIGHT - block_size - 64, 50, 50),
    ]
    for x, y, w, h in enemy_positions:
        add_enemy(pygame.Rect(x, y, w, h))

    # Items
    for i in range(8, 15):
        add_item(pygame.Rect(100 + i * 50, 200, 32, 32))
    for i in range(7, 14):
        add_item(pygame.Rect(150 + i * 50, HEIGHT - block_size * 5, 32, 32))
    for i in range(0, 3):
        add_item(pygame.Rect(1665 + i * 150, HEIGHT - block_size - 64, 32, 32))
    add_item(pygame.Rect(block_size * 14 + 20, block_size * 3, 32, 32))
    add_item(pygame.Rect(block_size * 24 + 16, HEIGHT - block_size * 4 + 56, 32, 32))
    add_item(pygame.Rect(block_size * 30, HEIGHT - block_size * 3, 32, 32))
    for i in range(-3, 10):
        add_item(pygame.Rect(block_size * 39 + 32 + 100 * i, HEIGHT - block_size * 5 - 64, 32, 32))
    for i in range(0, 5):
        add_item(pygame.Rect(block_size * 67 + 50 * i, HEIGHT - block_size * 2 - 64, 32, 32))
    add_item(pygame.Rect(block_size * 78, HEIGHT - block_size * 6 - 32, 64, 64))
    for i in range(0, 4):
        add_item(pygame.Rect(block_size * 91 + 44 * i, HEIGHT - block_size - 90, 32, 32))
    for i in range(0, 3):
        add_item(pygame.Rect(block_size * (93 + i), HEIGHT - block_size * 4 - 44, 32, 32))
    for x in (block_size * 108, block_size * 104, block_size * 116):
        add_item(pygame.Rect(x, HEIGHT - block_size * 4 - 44 if x != block_size * 104 else HEIGHT - block_size * 3 - 44, 32, 32))

    landmarks = [
        ("START", 100, 100, (80, 200, 255)),
        ("PinkAce", block_size * 16 + 24, HEIGHT - block_size * 5, (255, 120, 200)),
        ("Teleport", 2600, HEIGHT // 2, (200, 100, 255)),
        ("GOAL", block_size * 119, HEIGHT - block_size - 128, (255, 215, 0)),
    ]
    return objects, enemies, items, landmarks


KIND_COLORS = {
    "block": (95, 75, 55),
    "block2": (110, 95, 80),
    "brick": (140, 90, 55),
    "fire": (255, 90, 30),
    "saw": (200, 200, 210),
    "spikes": (180, 50, 50),
    "trampoline": (0, 220, 220),
    "box": (210, 140, 40),
    "goal": (255, 215, 0),
}


def world_bg(x):
    if x >= GREEN_X:
        return (34, 90, 50)
    if x >= PINK_X:
        return (90, 45, 75)
    return (35, 70, 120)


objects, enemies, items, landmarks = build_level()

all_rects = [r for r, _ in objects] + enemies + items
min_x = min(r.left for r in all_rects) - 80
max_x = max(r.right for r in all_rects) + 80
map_w = max_x - min_x

scale = min(1.0, 4800 / map_w)
out_w = int(map_w * scale)
out_h = int(HEIGHT * scale) + 90

pygame.init()
font = pygame.font.Font(None, 22)
title_font = pygame.font.Font(None, 28)

surface = pygame.Surface((out_w, out_h))
surface.fill((18, 18, 24))

for band_x in range(0, out_w, 4):
    world_x = min_x + band_x / scale
    pygame.draw.rect(surface, world_bg(world_x), (band_x, 0, 4, int(HEIGHT * scale)))

for label, x_pos, color in [
    ("BLUE WORLD", min_x + 400, (120, 180, 255)),
    ("PINK WORLD", PINK_X + 300, (255, 150, 200)),
    ("GREEN FRONTIER", GREEN_X + 200, (120, 255, 150)),
]:
    surface.blit(font.render(label, True, color), (int((x_pos - min_x) * scale), 8))


def to_screen(rect):
    return pygame.Rect(
        int((rect.x - min_x) * scale),
        int(rect.y * scale),
        max(1, int(rect.width * scale)),
        max(1, int(rect.height * scale)),
    )


for rect, kind in objects:
    pygame.draw.rect(surface, KIND_COLORS.get(kind, (95, 75, 55)), to_screen(rect))

for rect in enemies:
    pygame.draw.rect(surface, (180, 60, 220), to_screen(rect))

for rect in items:
    r = to_screen(rect)
    pygame.draw.circle(surface, (255, 230, 60), r.center, max(2, r.width // 2))

for label, x, y, color in landmarks:
    r = to_screen(pygame.Rect(x, y, 40, 40))
    pygame.draw.circle(surface, color, r.center, max(4, 6))
    surface.blit(font.render(label, True, color), (r.centerx - 30, r.centery - 18))

legend_y = int(HEIGHT * scale) + 12
surface.blit(title_font.render("BlueVenture — Full Map Overview", True, (240, 240, 240)), (12, legend_y))
lx = 12
for text, col in [
    ("Terrain", (95, 75, 55)),
    ("Alt terrain", (110, 95, 80)),
    ("Traps", (255, 90, 30)),
    ("Trampoline", (0, 220, 220)),
    ("Box / Goal", (255, 215, 0)),
    ("Enemies", (180, 60, 220)),
    ("Fruit", (255, 230, 60)),
]:
    pygame.draw.rect(surface, col, (lx, legend_y + 28, 14, 14))
    surface.blit(font.render(text, True, (200, 200, 200)), (lx + 20, legend_y + 26))
    lx += 155

out_path = os.path.join(ROOT, "map_overview.png")
pygame.image.save(surface, out_path)
print(f"Saved: {out_path} ({out_w}x{out_h})")
pygame.quit()
