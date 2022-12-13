#!/bin/python

from collections import deque

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def location(self):
        return (self.x, self.y)


class Grid:
    def __init__(self, x_size, y_size):
        
        self._grid = []
        self._xsize = x_size
        self._ysize = y_size
        for i in range(y_size):
            self._grid.append([])
            for j in range(x_size):
                self._grid[i].append(None)

        
    def add_point(self, x: int, y: int, value: int):
        self._grid[y][x] = value
        
        
    def get_value(self, point: Point):
        return self._grid[point[1]][point[0]]
        
    def set_anchors(self, start, end):
        self.start = start
        self.end = end
        
    def get_neighbors(self, point):
        neighbors = []
        locations = [ Point(0,1), Point(0,-1), Point(1,0), Point(-1,0) ]
        for spot in locations:
            temp = Point(point[0],point[1]) + spot
            if temp.x < 0 or temp.y < 0 or temp.x >= self._xsize or temp.y >= self._ysize:
                pass
            else:
                neighbors.append( ((temp.x,temp.y), self._grid[temp.y][temp.x]) )
        return neighbors
            

def bfs_search(graph: Grid):
    visited = set()

    queue = deque([ (0,graph.start) ])
    
    visited.add(graph.start)
    
    while queue:
        distance,node = queue.popleft()
        if node == graph.end:
            return distance
        
        height = graph.get_value(node)
        
        
        neighbors = graph.get_neighbors(node)
        for neighbor, n_height in neighbors:
            
            if n_height <= height + 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append((distance+1,neighbor))
            else:
                pass
            

def reversed_bfs_search(graph: Grid):
    visited = set()

    queue = deque([ (0,graph.end) ])
    
    visited.add(graph.end)
    
    while queue:
        distance,node = queue.popleft()
        if graph.get_value(node) == 0:
            return distance
        
        height = graph.get_value(node)
        
        
        neighbors = graph.get_neighbors(node)
        for neighbor, n_height in neighbors:
            
            if n_height >= height -1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append((distance+1,neighbor))
            else:
                pass


def main():

    with open('C:\\Users\\colinmac\\Documents\\Git Projects\\advent-of-code-2022\\day-12\\input\\data.txt') as f:
        raw_input = f.read()
    
    
    y_size = len(raw_input.split('\n'))
    x_size = len( raw_input.split('\n')[0] )
    map = Grid(x_size, y_size)
    start = None
    end = None
    
    for y,line in enumerate(raw_input.split('\n')):
        for x, symbol in enumerate(line):
            if symbol == 'S':
                map.add_point(x,y, ord('a') - ord('a'))
                start = (x,y)
            elif symbol == 'E':
                map.add_point(x,y, ord('z') - ord('a'))
                end = (x,y)
            else:
                map.add_point(x,y, ord(symbol) - ord('a'))
                
    assert start is not None and end is not None
    map.set_anchors(start,end)
    

    print("Part 1: minimum distance between S and E is: %d" % bfs_search(map))
    print("Part 2: minimum distance between E and any 'a' is: %d" % reversed_bfs_search(map))
            
    print("End of Line")
    return 0
    

 


if __name__ == "__main__":
    main()
