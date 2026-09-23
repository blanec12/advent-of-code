# Advent of Code 2015

My solutions to Advent of Code 2015, written in Python.

## Requirements
- Python 3.13+
- uv

## Setup

From the `2015` directory run this command:

```bash
uv sync
```

Create a `.env` file in the `2015` directory, and add your Advent of Code session cookie:

```bash
AOC_SESSION_COOKIE=<your-session-cookie>
```

Find your session cookie in your browser's dev tools while logged into Advent of Code.

## Input

Run `save_input.py` from the `2015` directory:

```bash
uv run python save_input.py --day 1
```

This downloads your puzzle input for the specified day and saves it to the corresponding directory.

For example, `--day 1` saves the input to:

```bash
day01/input.txt
```

## Run

Run solutions from the `2015` directory:

```bash
uv run python -m day01.solution
```

Replace `day01` with the day you want to run.

