#!/bin/python


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def location(self):
        return (self.x, self.y)


def move_tail(head: Point, tail: Point):

    #print_grid(head,tail)

    x_delta = head.x - tail.x
    y_delta = head.y - tail.y

    if x_delta == y_delta == 0:
        pass

    # Handle movement horizontally
    elif abs(x_delta) == 2 and y_delta == 0:
        if x_delta > 0:
            tail.x += 1
        else:
            tail.x -= 1


    elif abs(y_delta) == 2 and x_delta == 0:
        if y_delta > 0:
            tail.y += 1
        else:
            tail.y -= 1

    # diagonal move :(
    elif (abs(x_delta) + abs(y_delta) > 2 ):
        if x_delta > 0:
            tail.x += 1
        else:
            tail.x -= 1

        if y_delta > 0:
            tail.y += 1
        else:
            tail.y -= 1

def print_grid(head,tail):

    state = [list("." * 26) for i in range(21)]
    state[head.x][head.y] = 'H'

    for index, entry in enumerate(tail):
        state[entry.x][entry.y] = str(index)

    for row in reversed(state):
        print("".join(row))


def move_knots(head: Point, kts: list ):
    move_tail(head, kts[0])

    for i in range(1,len(kts)):
        move_tail(kts[i-1],kts[i])


def main():

    with open('C:\\Users\\colinmac\\Documents\\Git Projects\\advent-of-code-2022\\day-9\\input\\data.txt') as f:
        raw_input = f.read()

    input = raw_input.split('\n')


    head = Point(0,0)
    tail = Point(0,0)

    move = { "U":Point(1,0), "D":Point(-1,0), "L":Point(0,-1), "R":Point(0,1) }
    tail_log = set()
    tail_log.add(tail.location())

    for line in input:
        cmd,steps = line.split()

        for i in range(int(steps)):
            # move the head
            head = head + move[cmd]
            move_tail(head, tail)
            tail_log.add(tail.location())

    print("Part 1: Number of positions the tail has visited: %d" % len(tail_log))

    head = Point(0,0)
    # Part 2 is basically handling multiple tails(knots)
    tail_log = set()
    knots = [ Point(0,0) for i in range(9)]
    tail_log.update( [ entry.location() for entry in knots ] )

    for line in input:
        cmd, steps = line.split()
        for i in range(int(steps)):
            head = head + move[cmd]
            move_knots(head, knots)
            tail_log.add( knots[-1].location() )
        #print_grid(head, knots)
        #print("\n\n")

    print("Part 2: Number of positions the tail has hit: %d" % len(tail_log))

    return 0

if __name__ == "__main__":
    main()