# MyPokeAPIScraper-Project
Command-line tool that looks up Pokémon height, weight, and ability using the PokeAPI.
# Pokémon Lookup

A command-line tool that fetches Pokémon data from the [PokeAPI](https://pokeapi.co/) and displays each Pokémon's name, height, weight, and first ability.

## Features

- Look up any Pokémon by name
- Displays height and weight in meters and kilograms
- Handles invalid names and server errors with clear messages

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/souravdey0311/pokemon-lookup.git
   cd pokemon-lookup
   ```
2. Install the required library:
   ```bash
   pip install requests
   ```

## Usage

Run the program:

```bash
python MyPokeAPIScraper-Project.py
```

Enter a Pokémon name when prompted. Multi-word names use hyphens instead of spaces (for example, `mr-mime`). Type `quit` to exit.

Example:

```
Enter a Pokemon name or type quit to exit: pikachu
Name: Pikachu
Height: 0.4 Meters
Weight: 6.0 Kilograms
Ability: static
```

## What I Learned

- Making HTTP requests and handling status codes with `requests`
- Parsing JSON responses into Python dictionaries
- Building a input loop with a clean exit condition
