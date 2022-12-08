#!/bin/python



def is_visible(row, col, data):
    
    # Edges are always visible
    if row == 0 or row == len(data) - 1:
        return True
    if col == 0 or col == len(data[row]) -1:
        return True
    
    current_tree_height = data[row][col]
    
    # we only care about one row, and one column - those that our tree is inline with
    i_row = data[row]
    i_col = [data[x][col] for x in range(len(data))]
    
    # evaluate to true if all the trees in each direction are below the current tree
    left = all( x < current_tree_height for x in i_row[:col])
    right = all(x < current_tree_height for x in i_row[col+1:])
    up = all(x < current_tree_height for x in i_col[:row])
    down = all(x < current_tree_height for x in i_col[row+1:])
    
    return left or right or up or down
    
    
def viewing_score(x,y, data):
    score = 0
    
    current_tree_height = data[x][y]
    
    
    
    
    
    return score
    



def main():

    with open('C:\\Users\\colinmac\\Documents\\Git Projects\\advent-of-code-2022\\day-8\\input\\data.txt') as f:
        raw_input = f.read()
        
    input = raw_input.split('\n')
    data = [[int(i) for i in line] for line in input]
    
    ctr = 0
    
    for row in range(len(data)):
        for col in range(len(data[row])):
            
            if is_visible(row, col, data):
                ctr += 1
            
            
    print("Part 1: Number of trees visible from outside the grid: %d" % ctr)
 
            

    return 0

if __name__ == "__main__":
    main()