import tkinter as tk
from random import *

class Board:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.grid = self.blank_grid()
        self.randomise()
        

    def blank_grid(self):
        grid = [ [] for x in range(self.width)]
        for i in range(len(grid)):
            for j in range(self.height):
                grid[i].append(False)

        return grid



    def isAlive(self,x,y):
        if x >= 0 and x<len(self.grid):
            if y >= 0 and y<len(self.grid[0]):
                return self.grid[x][y]
        return False #get here =out of bounds!


    def get_cell_status(self,x,y):
        neigh = self.get_live_neighbours(x,y)
        if self.isAlive(x,y):
            return (neigh == 2 or neigh ==3)
        else:
            return neigh == 3
                                

    def get_live_neighbours(self,x,y):
        live = 0
        neighbors = [ (x-1,y), (x-1,y-1),
                  (x,y-1), (x+1,y-1),
                  (x+1,y), (x+1,y+1),
                  (x,y+1), (x-1,y+1) ]
        for neighbor in neighbors:
            if self.isAlive(neighbor[0],neighbor[1]):
                live+=1
        return live


    def update_grid(self):
        new_grid = self.blank_grid()
        for row in range(self.width):
            for col in range(self.height):
                new_grid[row][col] = self.get_cell_status(row,col)
        self.grid = new_grid


    def randomise(self):
        for row in range(self.width):
            for col in range(self.height):
                tf = [True,False,False,False]                
                self.grid[row][col] = choice(tf)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=500, height=500, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 100
        self.columns = 100
        self.cellwidth = 25
        self.cellheight = 25

        self.rect = {}
        for column in range(20):
            for row in range(20):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="red", tags="rect")

        self.redraw(1000)

    def redraw(self, delay):
        b.update_grid()
        self.canvas.itemconfig("rect", fill="red")
        for col in range(20):
            for row in range(20):
            
                item2_id = self.rect[row,col]
                if b.isAlive(row,col):
                    self.canvas.itemconfig(item2_id, fill="green")
        self.after(delay, lambda: self.redraw(delay))
    
if  __name__ =='__main__':
    b = Board(20,20)
    app = App()
    app.mainloop()
