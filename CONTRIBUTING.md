# Contributing to BlueVenture

Thanks for your interest in improving BlueVenture! Contributions of all kinds
are welcome — bug reports, new levels, enemies, art, or documentation.

## Getting started

1. Fork and clone the repository.
2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the game:

   ```bash
   python main.py
   ```

## Project layout

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
└── test/              # Headless smoke & integration tests
```

## Running the tests

The tests run headless (no window required) using dummy SDL drivers:

```bash
python test/smoke_test.py        # constructs every entity and runs their loops
python test/integration_test.py  # drives the real game loop for 400 frames
```

Please make sure both pass before opening a pull request.

## Coding style

- Target Python 3.9+.
- Follow PEP 8; the repo ships a [`ruff`](https://docs.astral.sh/ruff/) config.
  Run `ruff check .` and `ruff format .` if you have it installed.
- Keep comments focused on *why*, not *what*.
- Do not commit secrets. Database credentials are read from environment
  variables (see `.env.example`).

## Pull requests

1. Create a descriptive branch (`feature/ice-world`, `fix/trampoline-bounce`).
2. Keep changes focused and add a short note to `CHANGELOG.md`.
3. Ensure the tests pass and describe your change clearly in the PR.

## Assets & licensing

Game code is MIT licensed (see `LICENSE`). The pixel art is from the free
"Pixel Adventure" pack by **Pixel Frog**. Please respect the original asset
license when redistributing.
