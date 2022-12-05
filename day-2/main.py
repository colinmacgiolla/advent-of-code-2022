#!/bin/python



def result(opp,me):
    
    if opp == 'A':
        if me == 'X':
            return 3
        elif me == 'Y':
            return 6
        else:
            return 0 
        
    elif opp == 'B':
        if me == 'X':
            return 0
        elif me == 'Y':
            return 3
        else:
            return 6
        
    else:
        if me == 'X':
            return 6
        elif me == 'Y':
            return 0
        else:
            return 3

def get_point(item):
    
    if item == 'X':
        return 1
    elif item == 'Y':
        return 2
    else: 
        return 3


def part_two( opp, result):
    if opp == 'A':
        if result == 'X':
            return 0 + get_point('Z')
        elif result == 'Y':
            return 3 + get_point('X')
        else:
            return 6 + get_point('Y') 
        
    elif opp == 'B':
        if result == 'X':
            return 0 + get_point('X')
        elif result == 'Y':
            return 3 + get_point('Y')
        else:
            return 6 + get_point('Z')
        
    else:
        if result == 'X':
            return 0 + get_point('Y')
        elif result == 'Y':
            return 3 + get_point('Z')
        else:
            return 6 + get_point('X')


def main():
    '''
    The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. 
    The second column--" Suddenly, the Elf is called away to help with someone's tent.

    The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. 
    Winning every time would be suspicious, so the responses must have been carefully chosen.
    
    The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each 
    round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
    plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    
    
    ### Part 2
    
    The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: 
    X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

    The total score is still calculated in the same way, but now you need to figure out what shape to choose so the 
    round ends as indicated. The example above now goes like this:

    * In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), 
    so you also choose Rock. This gives you a score of 1 + 3 = 4.
    * In the second round, your opponent will choose Paper (B), and you choose Rock so 
    you lose (X) with a score of 1 + 0 = 1.
    * In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

    
    '''
    with open('C:\\Users\\colinmac\\Documents\\Git Projects\\advent-of-code-2022\\day-2\\input\\data.txt') as f:
        raw_input = f.read()
        
    raw_elf_data = raw_input.split("\n")
    
    strategy = []
    for line in raw_elf_data:
        strategy.append( line.split() )
        
    
    score = 0
    for item in strategy:
        score += result(item[0],item[1]) + get_point(item[1])
    
    print("Part 1 score is: %d" % score)
    
    score = 0
    for item in strategy:
        score += part_two(item[0],item[1])
        
    print("Part 2 score is: %d" % score)

        
    print("End of Line")
    
    
    
    return 0


if __name__ == "__main__":
    main()
