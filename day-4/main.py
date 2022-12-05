#!/bin/python

def main():
    '''
    Every section has a unique ID number, and each Elf is assigned a range of section IDs.

    However, as some of the Elves compare their section assignments with each other, they've noticed that many of 
    the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and 
    make a big list of the section assignments for each pair (your puzzle input).
    
    In how many assignment pairs does one range fully contain the other?
    
    =====
    
    In how many assignment pairs do the ranges overlap?
    '''
    
    with open('C:\\Users\\colinmac\\Documents\\Git Projects\\advent-of-code-2022\\day-4\\input\\data.txt') as f:
        raw_input = f.read()
        
    raw_elf_data = raw_input.split("\n")
    
    expanded_sets = []
    
    for line in raw_elf_data:
        pair = line.split(',')
        groupA = range( int(pair[0].split('-')[0]), int(pair[0].split('-')[1]) +1 )
        groupB = range( int(pair[1].split('-')[0]), int(pair[1].split('-')[1]) +1 )
        
        expanded_sets.append( (set(groupA),set(groupB)) )
        
    overlaps = 0
    
    for entry in expanded_sets:
        if entry[0].issuperset(entry[1]) or entry[0].issubset(entry[1]):
            overlaps += 1
            
    print("Part 1: Number of fully overlapping sets is: %d" % overlaps)
    
    overlaps = 0
    for entry in expanded_sets:
        if len( entry[0].intersection(entry[1]) ) > 0 :
            overlaps += 1
    print("Part 2: Number of partially overlapping sets is: %d" % overlaps)
    
    return 0


if __name__ == "__main__":
    main()
    