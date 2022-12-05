#!/bin/python


def main():
    
    '''
    1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000

    This list represents the Calories of the food carried by five Elves:

        The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
        The second Elf is carrying one food item with 4000 Calories.
        The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
        The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
        The fifth Elf is carrying one food item with 10000 Calories.

    In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know 
    how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).
        
    Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    
    Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
    
    '''
    
    with open('C:\\Users\\colinmac\\Documents\\Git Projects\\advent-of-code-2022\\day-1\\input\\data.txt') as f:
        raw_input = f.read()
        
    raw_elf_data = raw_input.split("\n\n")
    
    # Get rid of enpty blank line at the end of the last list
    raw_elf_data[-1] = '\n'.join(raw_elf_data[-1].split('\n')[:-1])
    
    calorie_count = []
    for index,entry in enumerate(raw_elf_data):
        #print(index)
        if len(entry) > 0:
            calorie_count.append(  sum( [int(x) for x in entry.split('\n')] ) )
    
    print("Highest calorie count is: %d" % max(calorie_count) )
    
    
    print("Total calories for top 3 is: %d" %   sum( sorted(calorie_count, key=int, reverse=True)[:3] )  )
        
    print("End of Line")
    
    
    
    return 0


if __name__ == "__main__":
    main()
