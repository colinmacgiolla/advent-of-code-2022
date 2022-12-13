#!/bin/python


from ast import literal_eval

def compare_packet(entryA, entryB):
    try:
        #print("Examining %s vs. %s" % (entryA, entryB))
        for i in range(len(entryA)):
            x = entryA[i]
            y = entryB[i]

            if isinstance(x, int) and isinstance(y, int):
                # Handle int comparison
                if x < y:
                    return True
                elif x > y:
                    return False
                else:
                    continue
                
            elif isinstance(x, list) and isinstance(y, int):
                # x is list and y is int
                result = compare_packet(x,[y])
                if result is None:
                    continue
                else:
                    return result
                
            elif isinstance(x, int) and isinstance(y, list):
                # x is int and y is list
                result = compare_packet([x], y)
                if result is None:
                    continue
                else:
                    return result
            else:
                # Both are lists
                result =  compare_packet(x,y)
                if result is None:
                    continue
                else:
                    return result
                

        
        # X should be shorter then Y and we haven't hit an exit yet
        if len(entryA) < len(entryB):
            return True
        # If we get this far, more iterations are required
        return None
    except IndexError:
        return False
            
    


def main():

    with open('C:\\Users\\colinmac\\Documents\\Git Projects\\advent-of-code-2022\\day-13\\input\\data.txt') as f:
        raw_input = f.read()
    
    entries = []
    for record in raw_input.split('\n\n'):
        entryA, entryB = record.split('\n')
        entries.append((entryA, entryB))
        
    parsed_pairs = []
    for entry in entries:
        entryA = literal_eval(entry[0])
        entryB = literal_eval(entry[1])
        parsed_pairs.append((entryA, entryB))
    
    correct_packets = []
    for index, pair in enumerate(parsed_pairs):
        if compare_packet(pair[0],pair[1]):
            correct_packets.append(index+1)
    
    print("Part 1: The sum of the indices of the currect packets: %d" % sum(correct_packets))
            
    print("End of Line")
    return 0
    


if __name__ == "__main__":
    main()
