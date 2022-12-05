#!/bin/python

from queue import LifoQueue
import time


def main():
    '''
        [H]         [H]         [V]    
        [V]         [V] [J]     [F] [F]
        [S] [L]     [M] [B]     [L] [J]
        [C] [N] [B] [W] [D]     [D] [M]
    [G] [L] [M] [S] [S] [C]     [T] [V]
    [P] [B] [B] [P] [Q] [S] [L] [H] [B]
    [N] [J] [D] [V] [C] [Q] [Q] [M] [P]
    [R] [T] [T] [R] [G] [W] [F] [W] [L]
     1   2   3   4   5   6   7   8   9 
    
    '''
    with open('C:\\Users\\colinmac\\Documents\\Git Projects\\advent-of-code-2022\\day-5\\input\\aoc_2022_day05_large_input-2.txt') as f:
        raw_input = f.read()
        
    
    q_list = []
    # used for part 2
    data_copy = []
    starting_state, actions = raw_input.split('\n\n')
    
    
    startTime = time.time()
    
    
    num_queues = len(starting_state.split('\n')[-1].split())
    i = 0
    while i < num_queues:
        q_list.append(LifoQueue())
        data_copy.append(LifoQueue())
        i+=1
    
    start_data = starting_state.split('\n')[:-1] 
    
        
    for line in start_data[::-1]:
        position = 1
        index = 0
        while  index < num_queues:
            if line[position] == " ":
                pass
            else:
                q_list[index].put(line[position])
                data_copy[index].put(line[position])
            position += 4
            index += 1
    

    
    for action in actions.split('\n'):
        temp = action.split()
        num = int(temp[1])
        src = int(temp[3])
        dst = int(temp[5])
        
        i = 0
        while i < num:
            item = q_list[src-1].get()
            q_list[dst-1].put(item)
            i += 1
    
    print("Results for part one: ")
    for stack in q_list:
        print(stack.get(),end='')

    print("\n")

    for action in actions.split('\n'):
        temp = action.split()
        num = int(temp[1])
        src = int(temp[3])
        dst = int(temp[5])
    
        i = 0
        items = []
        # To preserve the order we pop off the queue into a list
        # and put it to the new queue in reverse order, since it is a LIFO queue
        while i < num:
            items.append(data_copy[src-1].get())
            i += 1
        for item in reversed(items):
            data_copy[dst-1].put(item)

    print("Results for part two: ")
    for stack in data_copy:
        print(stack.get(),end='')            
    
    print("\n")
    print('Execution time in seconds: ' + str(time.time()-startTime))
    
    print("End of Line")
    
    
    
    return 0


if __name__ == "__main__":
    main()
