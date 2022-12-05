#!/bin/python

import string

def intersect(lst1, lst2):
    return list( set(lst1) & set(lst2) )


def main():
    '''
    The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of 
    items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the 
    second half of the characters represent items in the second compartment.
    
    To help prioritize item rearrangement, every item type can be converted to a priority:

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.

    Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
    
    ====
    
    For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. 
    That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and 
    at most two of the Elves will be carrying any other item type.

    Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type.

    Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?    
    '''
    
    with open('C:\\Users\\colinmac\\Documents\\Git Projects\\advent-of-code-2022\\day-3\\input\\data.txt') as f:
        raw_input = f.read()
        
    raw_elf_data = raw_input.split("\n")
    
    
    bag_list = []
    letter_lst = []
    
    letter_lst = list(string.ascii_lowercase)
    letter_lst.extend(list(string.ascii_uppercase))
    
    score_dict = {}
    i = 1
    for letter in letter_lst:
        score_dict[letter] = i
        i += 1
    
    
    for sack in raw_elf_data:
        bag_list.append( ( list(sack[0:len(sack)//2]), list(sack[len(sack)//2:]) ) )


    score = 0
    for item in bag_list:
        target = intersect(item[0],item[1])
        score += score_dict[target[0]]

    
    i = 0
    part_two_score = 0
    while i < len(raw_elf_data):
        target = list( set(raw_elf_data[i]) & set(raw_elf_data[i+1]) & set(raw_elf_data[i+2]))
        part_two_score += score_dict[target[0]]
        i+=3
        
        
        
    print("Part 1: Sum of priorities: %d" % score )
    print("Part 2: Sum of group priorities: %d" % part_two_score )

if __name__ == "__main__":
    main()
