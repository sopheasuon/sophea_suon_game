# Import module
from tkinter import *


# Create object
root = Tk()

# Adjust size
root.geometry("1000x1000")
# root.resizable(0,0)
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
circlePink = 6
index = 0
# Create Canvas


canvas1 =Canvas(root, bg="white")
imageF =PhotoImage(file="female1.png")
imageW =PhotoImage(file="Wall.png")
imageB =PhotoImage(file="Box.png")


# # #Function

def remove(event):
    canvas1.delete("remove")
    canvas1.delete("delete")
    canvas1.move("welcome", 0, 100)


def startNew(event):
    global grid
    # canvas1.create_rectangle(0, 0, 1000, 600, fill="white", tags="remove")
    canvas1.delete("all")
    arrayToDrawing(grid)



def quitNew(event):
    canvas1.move("welcome", 0, -100)
    canvas1.create_rectangle(300, 100, 700, 500, fill="white", tags="delete")
    canvas1.create_text(680, 120, text = "X", fill="black", font="Times 25 italic bold", tags="remove")
    canvas1.create_text(350, 130, anchor=W, font="Purisa",text="Most relationships seem so transitory")



# Add image file
bg = PhotoImage(file = "sky-background-clipart-2.png")


# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")


# Add Text
canvas1.create_text(500, 150, text = "Start game!!!", fill="white", font="Times 35 italic bold", tags="welcome")

#Button START
canvas1.create_rectangle(430, 220, 610, 280, fill="white", tags="start")
canvas1.create_text(515, 250, text = "Start", fill="black", font="Times 35 italic bold", tags="start")
canvas1.tag_bind("start", "<Button-1>", startNew)
#Button QUIT

canvas1.create_rectangle(430, 420, 610, 480, fill="white", tags="quit")
canvas1.create_text(515, 450, text = "Quit", fill="black", font="Times 35 italic bold", tags="quit")




canvas1.tag_bind("quit", "<Button-1>", quitNew)
canvas1.tag_bind("remove", "<Button-1>", remove)




def arrayToDrawing(grid):
    for n in range (len(grid)):
        for i in range (len(grid[n])):
            x0 = i*50
            y0 = (n*50)+200
            x1 = x0+50
            y1 = y0+50
            if grid[n][i] == 1:
                canvas1.create_image(x0+25, y0+20,image=imageF)
            elif grid[n][i] == 2:
                canvas1.create_image(x0+25, y0+25, image=imageW)
            elif grid[n][i] == 3:
                canvas1.create_oval(x0+15, y0+15, x1-15, y1-15, fill="#fd79a8", outline="white")
            elif grid[n][i] == "b":
                canvas1.create_image(x0+25, y0+25, image=imageB)
            else:
                canvas1.create_rectangle(x0, y0, x1, y1, fill="white", outline="white")

def getPlayerPosition(grid):
    global imageS
    # canvas.create_image(0, 0, image=imageS)
    canvas1.delete("all")
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
        elif grid[row][col-1] == "b":
            if grid[row][col-2] == 0:
                grid[row][col-2] = "b"
                grid[row][col] = 0
                grid[row][col-1] = 1 
            elif grid[row][col-2] == 3:
                grid[row][col-2] = "b"
                grid[row][col] = 3
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
        elif grid[row][col+1] == "b":
            if grid[row][col+2] == 0:
                grid[row][col+2] = "b"
                grid[row][col] = 0
                grid[row][col+1] = 1
            elif grid[row][col+2] == 3:
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
        elif grid[row-1][col] == "b":
            if grid[row-2][col] == 0:
                grid[row-2][col] = "b"
                grid[row][col] = 0
                grid[row-1][col] = 1  
            elif grid[row-2][col] == 3:
                grid[row+2][col] = "b"
                grid[row][col] = 0
                grid[row+1][col] = 1  
        arrayToDrawing(grid)


def down(event):
    global grid
    row = getPlayerPosition(grid)[0]
    col = getPlayerPosition(grid)[1]
    if row > 0:
        if grid[row+1][col] == 0:
            grid[row][col] = 0
            grid[row+1][col] = 1
        elif grid[row+1][col] == "b":
            if grid[row+2][col] == 0:
                grid[row+2][col] = "b"
                grid[row][col] = 0
                grid[row+1][col] = 1  
            elif grid[row+2][col] == 3:
                grid[row+2][col] = "b"
                grid[row][col] = 0
                grid[row+1][col] = 1 
        arrayToDrawing(grid)

canvas1.pack(fill = "both", expand = True)


root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)


# Display root
root.mainloop()