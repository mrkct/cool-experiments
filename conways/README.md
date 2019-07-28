# Conways Game of Life
## What is this
This is a simple implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) in C.

## How to run it
Nothing fancy is needed, just run:

    gcc conways.c -o conways
    ./conways

To change the initial state of the board edit the `board_init` function. To change how many evolutions to calculate change the STEPS constant. To change the size of the board change the SIZE constant