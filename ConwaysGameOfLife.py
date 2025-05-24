print("Name:Lata.S.B","USN:1AY24AI060","Section:'O'")
import time
import os

# Define grid size
WIDTH = 10
HEIGHT = 10

# Create an initial grid (0 = dead, 1 = alive)
grid = [[0]*WIDTH for _ in range(HEIGHT)]

# Add a simple pattern (a "blinker")
grid[4][4] = 1
grid[4][5] = 1
grid[4][6] = 1

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        for cell in row:
            print('■' if cell else ' ', end='')
        print()
    print()
