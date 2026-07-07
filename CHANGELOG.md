# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-07-07

### Added
- New third world, "The Green Frontier", extending the map beyond the pink area
  with fresh terrain, floating platforms and a green backdrop.
- Five new patrolling enemies: `Chicken`, `AngryPig`, `Slime`, `Snail`, `Mushroom`.
- New collectible fruits: Cherries, Oranges and Strawberries.
- `Trampoline` bounce pads that launch the player upward.
- Breakable `Box` crates that reward bonus fruit when smashed from below.
- `Goal` finish flag with a victory screen showing fruit collected and clear time.
- On-screen HUD with a live fruit counter and run timer.
- Headless `smoke_test.py` and `integration_test.py` under `test/`.
- Project scaffolding: `LICENSE`, `pyproject.toml`, `requirements.txt`,
  `CONTRIBUTING.md`, `CHANGELOG.md`, `.editorconfig`, `.env.example`,
  and a GitHub Actions CI workflow.
- Web (WebAssembly) build via pygbag with automatic deployment to GitHub Pages.

### Changed
- The game loop and menus were converted to `async` for browser (pygbag)
  compatibility; the desktop build is unaffected.
- Sound loading now prefers `.ogg` (required by the web build) and falls back
  to `.mp3`/`.wav` for desktop.
- Sound effects are now loaded once at startup instead of every frame.
- Backgrounds only reload when the world actually changes.
- MySQL support is now optional; the game runs and exits cleanly without a database.
- Database credentials are read from environment variables instead of being
  hard-coded in the source.

### Fixed
- Asset loader now ignores non-image files (e.g. `.DS_Store`), which previously
  crashed sprite-sheet loading.

## [1.0.0] - 2023-11

### Added
- Initial release: animated player and NPC, enemies, pets, items, obstacles,
  hearts system, teleportation between two worlds, and optional MySQL stats.
