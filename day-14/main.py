#!/bin/python

from pprint import pprint

    
def render_grid(grid: dict):
    min_X = min(grid.keys(), key=lambda x: x[0])[0]
    min_Y = min(grid.keys(), key=lambda x: x[1])[1]
    max_X = max(grid.keys(), key=lambda x: x[0])[0]
    max_Y = max(grid.keys(), key=lambda x: x[1])[1]
    
    for y in range(min_Y,max_Y+1):
        print("")
        for x in range(min_X,max_X+1):
            print("%s" % grid.get((x,y),".") , end="")
    print("\n")
    
    return None


class Grid():
    def __init__(self, start_point):
        self.data = {}
        self.min_X = None
        self.min_Y = None
        self.max_X = None
        self.max_Y = None
        self._startX, self._startY = start_point
        self.data[start_point] = "+"
        
    def add_stone( self, point ):
        self.data[ point ] = "#"
        
    def add_sand(self, point):
        self.data[point] = "o"
        
    def set_boundaries(self):
        
        self.min_X = min(self.data.keys(), key=lambda x: x[0])[0]
        self.min_Y = min(self.data.keys(), key=lambda x: x[1])[1]
        self.max_X = max(self.data.keys(), key=lambda x: x[0])[0]
        self.max_Y = max(self.data.keys(), key=lambda x: x[1])[1]
        
    def get( self, point, default="."):
        if point in self.data:
            return self.data[point]
        else:
            return default
        
    def render(self):
        for y in range(self.min_Y,self.max_Y+1):
            print("")
            for x in range(self.min_X, self.max_X+1):
                print("%s" % self.get((x,y)),end="" )
        print("\n")


def falling_sand(grid: Grid):
    
    sandX, sandY = grid._startX,grid._startY
    

    while True:
       
        # current space is empty, so fall by one
        if (sandX, sandY+1) not in grid.data:
            sandY += 1
        
        # there is something in the way, so try and move down
        # and to the left
        elif (sandX-1, sandY+1) not in grid.data:
            sandX -= 1
            sandY +=1
        
        # otherwise try to move down and to the right
        elif (sandX+1, sandY+1) not in grid.data:
            sandX += 1
            sandY += 1
        
        # can't move
        else:
            grid.add_sand( (sandX, sandY) )
            break
            
            
    
    
    return None



def main():

    with open('C:\\Users\\colinmac\\Documents\\Git Projects\\advent-of-code-2022\\day-14\\input\\data.txt') as f:
        raw_input = f.read()


    grid = Grid( (500,0))

    for line in raw_input.split('\n'):
        points = line.split(' -> ')
        coords = [ tuple(map(int,point.split(","))) for point in points ]


        for (X_cur, Y_cur),(X_nxt, Y_nxt) in zip(coords,coords[1:]):
            for x in range( min(X_cur,X_nxt), max(X_cur,X_nxt)+1 ):
                for y in range( min(Y_cur,Y_nxt), max(Y_cur,Y_nxt)+1 ):
                    grid.add_stone( (x,y) )
    
    # Import completed
    grid.set_boundaries()
                    

    for _ in range(22):
        falling_sand(grid)

    grid.render()
                
         
        
    

    print("End of Line")
    return 0



if __name__ == "__main__":
    main()
