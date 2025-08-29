# Requirements



## Functional

- CLI compatibility 
- GUI
- Make a board with a set size dependent on the difficulty.
    - **beginner** 9*9 Board and 10 mines
    - **Intermediate** 16*16 Board and 40 mines
    - **Advanced** 24 * 24 Board and 99 Mines
- place the mines in a random arrangement.
- Have user input actions
    - mark spot as a mine with a flag
    - Step on a spot aka mark a spot as not a mine
- showcase the numbers around spots that have been steeped with the number of mines around the stepped square. 
Showcase example: 
x is mine l is steeped on square

| 1 | 1 | 0 |
|---|---|---|
| x | l | 0 |
| x | 2 | 0 |

- making an appimage
 
## Non-Functional

- Modularity such that it should be easy to change from CLI to a GUI or other such examples
- Easy to read code
- work in a test mindset
- Learn as much as possible
- start with simple code. 