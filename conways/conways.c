#include <stdio.h>
#include <stdlib.h>
#define SIZE 20
#define STEPS 20
#define ALIVE 'o'
#define EMPTY ' '


char
step_cell(char **board, int x, int y, size_t size) {
    int i, j;
    int neighbours = 0;
    for (i = -1; i <= 1; i++) {
        for (j = -1; j <= 1; j++) {
            if (i == 0 && j == 0)
                continue;
            if (x+i >= 0 && x+i < size && y+j >= 0 && y+j < size)
                if (board[x+i][y+j] == ALIVE)
                    neighbours++;
        }
    }

    if (board[x][y] == EMPTY && neighbours == 3)
        return ALIVE;
    if (board[x][y] == ALIVE) {
        if (neighbours < 2 || neighbours > 3)
            return EMPTY;
        
        return ALIVE;
    }
}

char **
create_board(size_t size, char fill) {
    int i, j;
    char **board = malloc(sizeof(char*) * size);
    for (i = 0; i < size; i++) {
        board[i] = malloc(sizeof(char) * size);
        for (j = 0; j < size; j++) {
            board[i][j] = fill;
        }
    }

    return board;
}

void
free_board(char **board, size_t size) {
    int i;
    for (i = 0; i < size; i++) {
        free(board[i]);
    }
    free(board);
}

char **
step_board(char **board, size_t size) {
    char **next = create_board(size, EMPTY);
    int i, j;
    for (i = 0; i < size; i++) {
        for (j = 0; j < size; j++) {
            next[i][j] = step_cell(board, i, j, size);
        }
    }

    return next;
}

void
print_board(char **board, size_t size) {
    int i, j;
    for (j = 0; j < size; j++) {
        for (i = 0; i < size; i++) {
            printf("%c", board[i][j]);
        }
        printf("\n");
    }
}

/*
    Insert the initial state of the board here
*/
void
board_init(char **board, size_t size) {
    board[10][10] = EMPTY;
    board[11][10] = ALIVE;
    board[12][10] = EMPTY;
    board[10][11] = EMPTY;
    board[11][11] = EMPTY;
    board[12][11] = ALIVE;
    board[10][12] = ALIVE;
    board[11][12] = ALIVE;
    board[12][12] = ALIVE;
}

int 
main(int argc, char **argv) {
    char **board = create_board(SIZE, EMPTY);
    board_init(board, SIZE);

    char **t;
    int i;
    for (i = 0; i < STEPS; i++) {
        print_board(board, SIZE);
        t = step_board(board, SIZE);
        free_board(board, SIZE);
        board = t;
    }

    return 0;
}