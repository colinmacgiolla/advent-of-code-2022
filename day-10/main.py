#!/bin/python



def render_pixel(cycle, position):
    pos = (cycle % 40)-1
    pos_range = [position-1,position,position+1]
    if pos in pos_range:
        return '#'
    else:
        return ' '


def main():

    with open('C:\\Users\\Colin MacGiollaEain\\Documents\\Projects\\advent-of-code-2022\\day-10\\input\\data.txt') as f:
        raw_input = f.read()

    cycle_clock = 1
    register = 1
    key_cycles = [20,60,100,140,180,220]
    measured_strengths = []

    for line in raw_input.split("\n"):
        if 'noop' in line:
            cycle_clock += 1
            if cycle_clock in key_cycles:
                measured_strengths.append( register * cycle_clock )
        else:
            cycle_clock += 1
            cmd = int(line.split()[1])
 
            if cycle_clock in key_cycles:
                measured_strengths.append( register * cycle_clock )

            register += cmd

            cycle_clock += 1
            if cycle_clock in key_cycles:
                measured_strengths.append( register * cycle_clock )


    print("Part 1: Sum of the 6 measured strengths is: %d" % sum(measured_strengths))

    register = 1
    cycle_clock = 0

    print("\n\n")
    for line in raw_input.split("\n"):
        cycle_clock +=1

        if 'noop' in line:
            if cycle_clock % 40 == 0:
                print("")
            print(render_pixel(cycle_clock, register),end='')
          

        else:
            if cycle_clock % 40 == 0:
                print("")
            print(render_pixel(cycle_clock, register),end='')
            cycle_clock += 1
            cmd = int(line.split()[1])
            if cycle_clock % 40 == 0:
                print("")
            print(render_pixel(cycle_clock, register),end='')
            register += cmd

       
    return 0


if __name__ == "__main__":
    main()
