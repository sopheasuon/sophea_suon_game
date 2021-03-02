# IMPORTS
import tkinter as tk


# CONSTANTS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "PNC Data structure to graphism"


# VARIABLES
grid =[
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
[2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
[2,0,0,0,2,0,"b",0,0,0,0,0,0,2,2,2,2,2,0,2], 
[2,0,2,0,2,0,0,2,2,2,2,2,0,0,0,0,0,2,0,2], 
[2,0,2,0,2,2,"b",0,0,0,0,2,0,"b",2,0,0,2,0,2],
[2,0,2,0,0,0,0,2,2,2,2,2,2,0,2,2,0,3,3,2],
[2,0,2,0,"b",0,0,2,2,2,0,0,0,0,0,0,0,3,3,2],
[2,0,2,2,2,2,0,0,0,0,"b",0,0,2,0,2,0,3,3,2],
[2,0,2,0,0,0,0,0,2,2,2,2,0,2,0,2,2,0,0,2],
[2,0,0,"b",2,2,2,2,2,0,0,0,0,2,0,2,0,0,0,2],
[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
]
index = 0

# squareSize = #choose the appropriate size of the squares


# VARIABLES
def arrayToDrawing(grid):
    # global image
    for n in range (len(grid)):
        for i in range (len(grid[n])):
            x0 = i*50
            y0 = (n*50)+200
            x1 = x0+50
            y1 = y0+50
            if grid[n][i] == 1:
                canvas.create_image(x0+20, y0+20,image=imageF)
            elif grid[n][i] == 2:
                canvas.create_image(x0+25, y0+25, image=imageW)
            elif grid[n][i] == 3:
                canvas.create_oval(x0+15, y0+15, x1-15, y1-15, fill="#fd79a8", outline="white")
            elif grid[n][i] == "b":
                canvas.create_image(x0+25, y0+25, image=imageB)
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="white")

def getPlayerPosition(grid):
    for n in range (len(grid)):
        for i in range (len(grid[n])):
            if grid[n][i] == 1:
                col = i
                row = n
    return([row, col])


def left(event):
    global grid
    row = getPlayerPosition(grid)[0]
    col = getPlayerPosition(grid)[1]
    if grid[row][col-1] != 2:
        grid[row][col] = 0
        grid[row][col-1] = 1 
        
    elif grid[row][col-1]== "b":
        grid[row][col] = 0
        grid[row][col-1] = 1
        grid[row][col-2] = "b"
    arrayToDrawing(grid)
    
       

      
def right(event):
    global grid
    row = getPlayerPosition(grid)[0]
    col = getPlayerPosition(grid)[1]
    if grid[row][col+1] != 2:
        grid[row][col] = 0
        grid[row][col+1] = 1 
        
    elif grid[row][col+1] == "b":
        grid[row][col] = 0
        grid[row][col+1] = 1
        grid[row][col+2] = "b" 
    arrayToDrawing(grid)

def up(event):
    global grid
    row = getPlayerPosition(grid)[0]
    col = getPlayerPosition(grid)[1]
    if grid[row-1][col] != 2:       
        grid[row][col] = 0
        grid[row-1][col] = 1 
        
    elif grid[row-1][col] == "b":
        grid[row][col] = 0
        grid[row-1][col] = 1 
        grid[row-2][col] = "b"
    arrayToDrawing(grid)
    
        

def down(event):
    global grid
    row = getPlayerPosition(grid)[0]
    col = getPlayerPosition(grid)[1]
    if grid[row+1][col] != 2:
        grid[row][col] = 0
        grid[row+1][col] = 1 
        
    elif grid[row+1][col] == "b":
        grid[row][col] = 0
        grid[row+1][col] = 1 
        grid[row+2][col] = "b" 
    arrayToDrawing(grid)

        

        
# draw a line with white and black squares using the global array
root = tk.Tk()
imageF = tk.PhotoImage(file="female(1).png")
imageW = tk.PhotoImage(file="wall.png")
imageB = tk.PhotoImage(file="box.png")
# imageB = tk.PhotoImage(file="box.png")
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(root,bg="white")

# root.resizable(False, False)
canvas.pack(expand=True, fill="both")
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)


arrayToDrawing(grid)
root.mainloop()