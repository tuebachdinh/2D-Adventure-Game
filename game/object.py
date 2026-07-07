from os.path import join

import pygame

from game.load_images import get_block_or_brick, get_sprite_sheets

pygame.init()

class Object(pygame.sprite.Sprite):
    ANIMATION_DELAY = 3
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))

class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block_or_brick(size, size, 0, 0)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
class Block2(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = get_block_or_brick(size,size,96,128)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Brick(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        block = get_block_or_brick(width, height, 0, 0)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

class Fire(Object):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.sprites = get_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.sprites["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "on"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

class Saw(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "saw")
        self.sprites = get_sprite_sheets("Traps", "Saw", width, height)
        self.image = self.sprites["on"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "on"
    def loop(self):
        sprites = self.sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

class Spikes(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "spikes")
        self.sprites = get_sprite_sheets("Traps", "Spikes", width, height)
        self.image = self.sprites["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Idle"
    def loop(self):
        sprites = self.sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

class Trampoline(Object):
    """A bouncy pad. When the player lands on it, it launches them upward."""
    ANIMATION_DELAY = 2

    def __init__(self, x, y, width=56, height=56):
        super().__init__(x, y, width, height, "trampoline")
        self.sprites = get_sprite_sheets("Traps", "Trampoline", 28, 28)
        self.animation_name = "Idle"
        self.image = self.sprites[self.animation_name][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.bouncing = 0

    def bounce(self):
        self.animation_name = "Jump (28x28)"
        self.animation_count = 0
        self.bouncing = 1

    def loop(self):
        sprites = self.sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        if self.bouncing and (self.animation_count // self.ANIMATION_DELAY) >= len(sprites):
            self.animation_name = "Idle"
            self.animation_count = 0
            self.bouncing = 0
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)


class Box(Object):
    """A solid crate the player can smash from below to reveal a reward."""
    ANIMATION_DELAY = 3

    def __init__(self, x, y, size=48, kind="Box1"):
        super().__init__(x, y, size, size, "box")
        self.sprites = get_sprite_sheets("Items", join("Boxes", kind), 28, 24)
        self.animation_name = "Idle"
        self.image = self.sprites[self.animation_name][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.broken = False
        self.reward_given = False

    def break_open(self):
        if not self.broken:
            self.broken = True
            self.animation_name = "Break"
            self.animation_count = 0

    def loop(self):
        sprites = self.sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        if self.broken and (self.animation_count // self.ANIMATION_DELAY) >= len(sprites):
            self.rect.x = -300
            self.rect.y = -300
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)


class Goal(Object):
    """The end-of-level flag. Reaching it wins the game."""
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width=64, height=64):
        super().__init__(x, y, width, height, "goal")
        self.sprites = get_sprite_sheets("Items", "Checkpoints", 64, 64)
        self.animation_name = "End (Idle)"
        self.image = self.sprites[self.animation_name][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.reached = False

    def press(self):
        if not self.reached:
            self.reached = True
            self.animation_name = "End (Pressed) (64x64)"
            self.animation_count = 0

    def loop(self):
        sprites = self.sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        if (self.animation_count // self.ANIMATION_DELAY) >= len(sprites):
            self.animation_count = 0
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)


class Item(pygame.sprite.Sprite):
    ANIMATION_DELAY = 2
    def __init__(self, x, y, width, height, name):
        self.name = name
        self.rect = pygame.Rect(x, y, width, height)
        self.animation_count = 0
        self.SPRITES = get_sprite_sheets("Items", "Fruits", width, height, False)
        self.hit = False
        self.hit_animation = 0

    def update_sprite_sheet(self):
        sprites = self.SPRITES[self.name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        if (self.animation_count // self.ANIMATION_DELAY) >  len(sprites):
            self.animation_count = 0
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)
        if self.hit:
            self.name = "Collected"
            self.hit_animation += 1
            if self.hit_animation > 10:
                self.rect.x = - 100
                self.rect.y = - 100


    def loop(self, fps):
        self.update_sprite_sheet()

    def disappear(self):
        self.hit = True

    def draw(self, window, offset_x):
        window.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))

class Checkpoint(Item):
    ANIMATION_DELAY = 2
    def __init__(self, x, y, width, height, name):
        super().__init__(x, y, width, height, name)
        self.SPRITES = get_sprite_sheets("Items", "Checkpoints", 32, 32, False)


