
# GROUP LUKE, BEN, KEEGAN
import matplotlib.pyplot as plt
import matplotlib.animation
import time
# USER INPUT MENU


state = input("Enter a state from the list above: ")
gridsize = input("Enter Gridsize ex.(10): ")
steps = input("Enter steps to run similation: ")
gridsize = int(gridsize)
steps = int(steps)

# CREATION OF GRID

start = time.time()

cols = gridsize
rows = gridsize
grid = [[False] * cols for r in range(rows)]

# COUNTING NEIGHBORS IN EACH CELL
def countNeighbors(grid, x, y):
    check = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(x-i < len(grid) and y-j < len(grid) and grid[x-i][y-j] ):
                
                check += 1
    if(grid[x][y]):
        check -= 1

    return check

# UPDATING CURRENT GRID WITH GAME RULES


def Update(grid, n):
    updated_grid = [[False] * cols for r in range(rows)]
    for i in range(gridsize-1):
        for j in range(gridsize-1):
           # print(i,j)
            curr = grid[i][j]
            if(i == 0 or i == cols - 1 or j == 0 or j == rows - 1):
                updated_grid[i][j] = grid[i][j]
            neighbors = countNeighbors(grid, i, j)
            curr = grid[i][j]
            if curr == False and neighbors == 3:
                updated_grid[i][j] = True
            elif curr == True and (neighbors < 2 or neighbors > 3):
                updated_grid[i][j] = False
            else:
                updated_grid[i][j] = curr

    grid = [[False] * cols for r in range(rows)]
    #boardplot(updated_grid, gridsize)
    return updated_grid

# RANDOM STATE


def random(grid, n):
    import random
    choice = [True, False]
    for x in range(n):
        for y in range(n):
            grid[x][y] = random.choice(choice)

    return grid

# BLINKER STATE

def blinker(grid, n):
    mid = int(gridsize / 2)
    left = int((gridsize/2) - 1)
    right = int((gridsize/2) + 1)
    grid[mid][mid] = True
    grid[left][mid] = True
    grid[right][mid] = True
    return grid

# GLIDER GUN STATE
def glidergun(grid, n):
    mid = int(gridsize / 2)

    grid[mid][mid] = True
    grid[mid+1][mid+2] = True
    grid[mid+2][mid+1] = True
    grid[mid+2][mid] = True
    grid[mid+3][mid] = True
    grid[mid+2][mid-1] = True
    grid[mid+1][mid-2] = True
    grid[mid-1][mid-3] = True
    grid[mid-2][mid-3] = True
    grid[mid-3][mid-2] = True
    grid[mid-4][mid-1] = True
    grid[mid-4][mid] = True
    grid[mid-4][mid+1] = True
    grid[mid-3][mid+2] = True
    grid[mid-2][mid+3] = True
    grid[mid-1][mid+3] = True

    grid[mid-13][mid] = True
    grid[mid-14][mid] = True
    grid[mid-14][mid+1] = True
    grid[mid-13][mid+1] = True

    grid[mid+6][mid+1] = True
    grid[mid+6][mid+2] = True
    grid[mid+6][mid+3] = True
    grid[mid+7][mid+1] = True
    grid[mid+7][mid+2] = True
    grid[mid+7][mid+3] = True
    grid[mid+8][mid] = True
    grid[mid+8][mid+4] = True
    grid[mid+10][mid] = True
    grid[mid+10][mid-1] = True
    grid[mid+10][mid+4] = True
    grid[mid+10][mid+5] = True

    grid[mid+20][mid+2] = True
    grid[mid+20][mid+3] = True
    grid[mid+21][mid+2] = True
    grid[mid+21][mid+3] = True

    return grid
# PERSON STATE


def person(grid, n):
    mid = int(gridsize / 2)
    grid[mid][mid] = True
    grid[mid][mid+1] = True
    grid[mid+1][mid+2] = True
    grid[mid+1][mid+3] = True
    grid[mid+1][mid+4] = True
    grid[mid][mid+4] = True
    grid[mid-1][mid+4] = True
    grid[mid-1][mid+3] = True
    grid[mid-1][mid+2] = True
    grid[mid-1][mid] = True
    grid[mid-1][mid-3] = True
    grid[mid-1][mid-4] = True
    grid[mid-3][mid] = True
    grid[mid-2][mid-1] = True
    grid[mid+1][mid] = True
    grid[mid+1][mid-3] = True
    grid[mid+1][mid-4] = True
    grid[mid+3][mid-2] = True
    grid[mid+2][mid-1] = True
    grid[mid][mid-1] = True
    grid[mid][mid-2] = True
    return grid
# PLOTTING BOARD
fig, ax = plt.subplots()
life = [(x, y) for x in range(gridsize) for y in range(gridsize) if grid[x][y]]
xs = [x for (x, _) in life]
ys = [y for (_, y) in life]
if state == 'random':
    grid = random(grid, gridsize)
elif state == 'glider gun':
    grid = glidergun(grid, gridsize)
elif state == 'blinker':
    grid = blinker(grid, gridsize)
elif state == 'person':
    grid = person(grid, gridsize)
sc = ax.scatter(xs, ys, marker = 'x')
plt.xlim([0,gridsize])
plt.ylim([0,gridsize])
 

def boardplot(grid, n):
    # Find all the x and y cells that are true
    life = [(x, y) for x in range(n) for y in range(n) if grid[x][y]]
    xs = [x for (x, _) in life]
    ys = [y for (_, y) in life]
    plt.xlim([0, n])
    plt.ylim([0, n])
    plt.scatter(xs, ys, marker='x')
    

def animate(steps):
    global grid
    
   
    newgrid = Update(grid,gridsize)        
    grid = newgrid
    life = [(x, y) for x in range(gridsize) for y in range(gridsize) if grid[x][y]]
    xs = [x for (x, _) in life]
    ys = [y for (_, y) in life]
    news = [[xs[i],ys[i]] for i in range (len(xs))]
    sc.set_offsets(news)

def dyngraph(grid, n, steps):

    
    ani = matplotlib.animation.FuncAnimation(fig, animate, 
                frames=steps, interval=1, repeat= False) 
    plt.show()
    return ani


ani = dyngraph(grid, gridsize, steps)

end = time.time()

print ('Time taken: ' , (end - start))
# CONSOLE

