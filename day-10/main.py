#!/bin/python






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




       
    return 0


if __name__ == "__main__":
    main()
