# Wordle Solver

A Python script for finding solutions to a Wordle puzzle. Only tested with Python 3.9.

 ## Usage

The script takes two arguments from the command line: **guess** and **exclusions**, then prints the possible solutions to the puzzle.

Run the script as follows: `python wordle_solver.py [guess] [exclusions]`

### Guess String

The guess string has three options for each of the five letters in the puzzle:

* Unknown: `-`
* Wrong position: `[x]`
  * Multiple letters can be provided for a single position: `[xy]`
* Correct: `x`

### Exclusions String

List the letters that are not part of the solution as a string with no spaces: `abcde`

## Example

`python wordle.py [w]-[n]-y ertiadc`

**Output**: SNOWY

