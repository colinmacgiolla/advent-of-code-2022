#!/bin/python



def msg_parser(input, window=4):
    index = 0

    while (index + window) < len(input):

        block = input[index:window+index]
        if len( set(block)) != window:
            index += 1
        else:
            break    

    return int(window + index)


def main():

    with open('C:\\Users\\Colin MacGiollaEain\\Documents\\Projects\\advent-of-code-2022\\day-6\\input\\data.txt') as f:
        raw_input = f.read()

    print("Part 1: Marker located at: %d" % msg_parser(raw_input))
    print("Part 2: Marker located at: %d" % msg_parser(raw_input, window=14))

       
    return 0


if __name__ == "__main__":
    main()
