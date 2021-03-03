# IMPORTS
import tkinter as tk


# CONSTANTS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
root = tk.Tk()  
# frame = tk.Frame()
# frame.master.title("Sophea")
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(root, bg="white")
# imageS = tk.PhotoImage(file="Sky.png")
imageF = tk.PhotoImage(file="female1.png")
imageW = tk.PhotoImage(file="Wall.png")
imageB = tk.PhotoImage(file="Box.png")


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


def arrayToDrawing(grid):
    for n in range (len(grid)):
        for i in range (len(grid[n])):
            x0 = i*50
            y0 = (n*50)+200
            x1 = x0+50
            y1 = y0+50
            if grid[n][i] == 1:
                canvas.create_image(x0+25, y0+20,image=imageF)
            elif grid[n][i] == 2:
                canvas.create_image(x0+25, y0+25, image=imageW)
            elif grid[n][i] == 3:
                canvas.create_oval(x0+15, y0+15, x1-15, y1-15, fill="#fd79a8", outline="white")
            elif grid[n][i] == "b":
                canvas.create_image(x0+25, y0+25, image=imageB)
            else:
                # canvas.create_image(x0+25, y0+25, image=imageS)
                canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="white")

def getPlayerPosition(grid):
    global imageS
    # canvas.create_image(0, 0, image=imageS)
    canvas.delete("all")
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
    if col > 0:
        if grid[row][col-1] == 0:
            grid[row][col] = 0
            grid[row][col-1] = 1
        elif grid[row][col-1] == "b" and col > 0:
            if grid[row][col-2] == 0:
                grid[row][col-2] = "b"
                grid[row][col] = 0
                grid[row][col-1] = 1        
        arrayToDrawing(grid)

     
def right(event):
    global grid
    row = getPlayerPosition(grid)[0]
    col = getPlayerPosition(grid)[1]
    if col > 0:
        if grid[row][col+1] == 0:
            grid[row][col] = 0
            grid[row][col+1] = 1
        elif grid[row][col+1] == "b" and col >0:
            if grid[row][col+2] == 0:
                grid[row][col+2] = "b"
                grid[row][col] = 0
                grid[row][col+1] = 1         
        arrayToDrawing(grid)

def up(event):
    global grid
    row = getPlayerPosition(grid)[0]
    col = getPlayerPosition(grid)[1]
    if row > 0:
        if grid[row-1][col] == 0:
            grid[row][col] = 0
            grid[row-1][col] = 1
        elif grid[row-1][col] == "b" and row > 0:
            if grid[row-2][col] == 0:
                grid[row-2][col] = "b"
                grid[row][col] = 0
                grid[row-1][col] = 1    
        arrayToDrawing(grid)


def down(event):
    global grid
    row = getPlayerPosition(grid)[0]
    col = getPlayerPosition(grid)[1]
    if row > 0:
        if grid[row+1][col] == 0:
            grid[row][col] = 0
            grid[row+1][col] = 1
        elif grid[row+1][col] == "b" and row > 0:
            if grid[row+2][col] == 0:
                grid[row+2][col] = "b"
                grid[row][col] = 0
                grid[row+1][col] = 1   
        arrayToDrawing(grid)

     
root.resizable(False, False)
canvas.pack(expand=True, fill="both")
# frame.pack(expand=True, fill="both")


root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)


arrayToDrawing(grid)
root.mainloop()
