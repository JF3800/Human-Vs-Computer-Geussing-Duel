# Game.py — Source Code Overview

This is the full source for Mind vs Machine: The Guessing Duel. A terminal number guessing game where you race against a computer. Fewest guesses wins.

---

## How the Code Works

### Setup
```python
import random
from rich import print
```
`random` generates the computer's secret number. `rich` handles all the colored terminal output using markup tags like `[bold green]text[/bold green]`.

---

### Round 1 — Human Turn
```python
random_n = random.randint(1, 100)
```
The computer picks a random number between 1 and 100. You don't see it.

A `while True` loop keeps asking for guesses until you get it right. Each guess increments `human_geuss` and checks if it's too high, too low, or correct. On correct, it breaks out of the loop.

---

### Round 2 — Computer Turn
```python
low = 1
high = 100
geuss = (low + high) // 2
```
The computer uses binary search. Every iteration it guesses the midpoint of the remaining range. If the guess is too high, `high` gets updated. Too low, `low` gets updated. It finds any number between 1 and 100 in at most 7 guesses.

---

### Winner Check
```python
if computer_geuss > human_geuss:
    # you won
elif computer_geuss == human_geuss:
    # tie
else:
    # you lost
```
Simple comparison at the end. Fewer guesses wins.

---

## Dependencies

```bash
pip install rich
```

Only one external library. Everything else is standard Python.

---

## Running It

```bash
python Game.py
```

Or download the binary from the releases page no Python needed.
