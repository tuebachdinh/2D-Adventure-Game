# BlueVenture - 2D Adventure Game Engine Simulation

[![CI](https://github.com/tuebachdinh/2D-Adventure-Game/actions/workflows/ci.yml/badge.svg)](https://github.com/tuebachdinh/2D-Adventure-Game/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Made with pygame](https://img.shields.io/badge/made%20with-pygame-1f425f.svg)](https://www.pygame.org/)

**Overview**

Welcome to "BlueVenture" ! This Python game, powered by the Pygame library, takes you on an animated adventure featuring different characters based on your choice. Brace yourself for a thrilling journey filled with enemies, pets, obstacles, and finding your lover - PinkAce. 

Your mission: guide the player to the your lover's destination while avoiding enemies and obstacles 🪨, all while preserving your three hearts. Meet PinkAce, teleport to a new state, and face fresh challenges!🚀🤖

**Demo video**

[![Gameplay Video](https://img.youtube.com/vi/gqSG5FgoR6Q/maxresdefault.jpg)](https://www.youtube.com/watch?v=gqSG5FgoR6Q)

**Features**
 
- Animated Player: Lively animations of the player character, courtesy of PixelFrog Assets. Enjoy fluid movements, jumps, and double jumps that bring the game to life.🔹
- Diverse Characters: Encounter animated enemies, items, pets, and an NPC. Each character is crafted with different functions to enhance your gaming experience.🐸🦇🦏
- Objective: Navigate through obstacles and enemies, collecting items along the way. Your goal is to reach the your lover's destination without losing all three hearts.🍥
- Hearts System: Be strategic to preserve your three hearts. Losing them all leads to a game over. Plan your moves, overcome challenges, and find PinkAce with at least one heart intact.💙
- Pet System: Collect enough items, and you'll receive a pet! Pets can eliminate enemies, providing an advantage in overcoming obstacles. Your pet becomes your trusty companion on this exciting journey.🐦🐟
- Teleportation: Successfully reaching the NPC triggers a teleportation to a new game state. Brace yourself for new environments and challenges in each level.🕦

**What's new in this expansion** ✨

- New world - "The Green Frontier": A brand-new third area extends the map far beyond the pink world, with fresh terrain, floating platforms and a lush green backdrop.🌿
- New enemies: Patrolling **Chicken**, **AngryPig**, **Slime**, **Snail** and **Mushroom** foes that pace back and forth and can be defeated by your pets.🐔🐌
- New collectibles: **Cherries**, **Oranges** and **Strawberries** join the fruit basket.🍒🍓🍊
- Trampolines: Bounce pads that launch you high into the air to reach hidden fruit platforms.🤸
- Breakable crates: Smash boxes from below to reveal a bonus of +3 fruit.📦
- Finish flag: Reach the end flag to rescue PinkAce and trigger a victory screen showing your fruit count and clear time.🏁
- HUD: A live fruit counter and run timer are shown at the top of the screen.⏱️
- Quality of life: MySQL is now optional (the game no longer crashes without a database), sound effects load once instead of every frame, and hidden files (like `.DS_Store`) no longer break asset loading.🛠️

**Controls**

- Arrow keys: Move the player character left or right. ←→
- Spacebar / Up: Make the player character jump.⬆️
- Double Jump: Press jump twice for a double jump.⬆️⬆️
- Trampolines: Simply land on a bounce pad to be launched upward.🤸

**Play in your browser**

The game is also built to WebAssembly with [pygbag](https://github.com/pygame-web/pygbag)
and published to GitHub Pages on every push to `main` — no install required:

➡️ https://tuebachdinh.github.io/2D-Adventure-Game/

**Setup & Run (desktop)**

```bash
# Install dependencies (pygame-ce is a drop-in replacement for pygame)
pip install -r requirements.txt

# Start the game
python main.py
```

**Build the web version locally**

```bash
pip install pygbag
python -m pygbag main.py      # serves at http://localhost:8000
```

**Tests**

Headless smoke and integration tests can be run without a display:

```bash
python test/smoke_test.py        # builds every entity and runs their loops
python test/integration_test.py  # drives the real game loop for 400 frames
```

**Project structure**

```
2D-Adventure-Game/
├── main.py            # Entry point, game loop, level layout, menus
├── game/              # Core engine package
│   ├── player.py      # Player + NPC classes
│   ├── enemy.py       # Enemies and pets
│   ├── object.py      # Blocks, traps, items, trampolines, boxes, goal
│   └── load_images.py # Sprite-sheet / background loading helpers
├── assets/            # Art & fonts (Pixel Adventure by Pixel Frog)
├── sound/             # Music & sound effects
├── state/             # UI images (menus, hearts, game over)
├── test/              # Headless smoke & integration tests
├── requirements.txt   # Runtime dependencies
├── pyproject.toml     # Project metadata & tooling config
└── .github/workflows/ # Continuous integration
```

**Optional: persisting stats to MySQL**

Stats are only saved if [`mysql-connector-python`](https://pypi.org/project/mysql-connector-python/)
is installed and a database is reachable. Copy `.env.example` to `.env` and set
the `BLUEVENTURE_DB_*` variables — no credentials are hard-coded in the source.

**Contribution**

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for the
development setup, test commands, and pull-request guidelines.

**Credits**

- Pygame: The game is built using the Pygame library.
- Player, Enemy, and Pet Artwork from the "Pixel Adventure" pack by Pixel Frog.
- Game Developed by Tue Dinh (Toby).

**License**

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file
for details. Enjoy the game!

Happy gaming! 🎮
