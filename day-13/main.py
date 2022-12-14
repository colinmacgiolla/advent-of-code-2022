#!/bin/python


from ast import literal_eval
from functools import cmp_to_key
from pprint import pprint
from copy import deepcopy

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
                result = compare_packet(x,y)
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


def compare_wrapper(entryA, entryB):
    response = compare_packet(entryA, entryB)
    if response is None:
        return 0
    elif response:
        return 1
    else:
        return -1


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

    all_packets = [ x for y in parsed_pairs for x in y ]
    # Add our marker packets
    all_packets.append([[2]])
    all_packets.append([[6]])

    # Sort based on whether or not they are correct I *think*!
 
    sorted_packets = sorted(all_packets, key=cmp_to_key(compare_wrapper), reverse=True)
    #pprint(sorted_packets)
    mark_1 = sorted_packets.index([[2]]) + 1
    mark_2 = sorted_packets.index([[6]]) + 1
    print("Part 2: The product of the indices of the marker packets in the sorted list is: %d" % (mark_1 * mark_2))


    print("End of Line")
    return 0



if __name__ == "__main__":
    main()
