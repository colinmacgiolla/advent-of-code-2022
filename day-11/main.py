#!/bin/python

from copy import deepcopy
import math
class Monkey:
    '''
    Arguments:
        items: Initial list of items
        test: divisible by X (the test)
        trueTest: target monkey if true
        falseTest: target monkey if false
        operation: the string describing the operation performed by the monkey
        relief_factor=3: part 1 parameter to limit the size of the dividend
    '''

    def __init__(self, items: list[int] , test: int, trueTest: int, falseTest: int, operation: str, relief_factor=3):
        self._relief_factor = relief_factor
        self.items = items
        self.test_divisor = test
        self._true_target = trueTest
        self._false_target = falseTest
        self._inspect_ctr = 0
        # Added for part 2
        self.lcm = None
        self._operandA, self._operator, self._operandB = operation.split()

    def test(self, item: int):
        if item % self.test_divisor == 0:
            return True
        else:
            return False

    def work_round(self):
        throw = []
        for item in self.items:
            self._inspect_ctr += 1
            result = self.inspect(item)
            action = self.action(result)
            throw.append(action)
        self.items.clear()
        return throw

    def catch(self, item: int):
        self.items.append(item)

    def inspect(self, item: int):
        if self._operandA == 'old':
            operandA = item
        else:
            operandA = self._operandA
        if self._operandB == 'old':
            operandB = item
        else:
            operandB = self._operandB

        if self._operator == '+':
            return int(operandA) + int(operandB)
        elif self._operator == '-':
            return int(operandA) - int(operandB)
        elif self._operator == '*':
            return int(operandA) * int(operandB)
        elif self._operator == '/':
            return int(operandA) / int(operandB)

    def action(self, item: int):

        if self.lcm is not None:
            # Part 2 special. the updated_item is now the modulo of the lowest common divisor, of the multiple
            # of the divisors, on the dividend
            updated_item = item % self.lcm
        else:
            updated_item = item // self._relief_factor

        if self.test(updated_item):
            return( (updated_item,self._true_target) )
        else:
            return( (updated_item, self._false_target) )



def main():

    with open('C:\\Users\\Colin MacGiollaEain\\Documents\\Projects\\advent-of-code-2022\\day-11\\input\\data.txt') as f:
        raw_input = f.read()

    monkeys = []
    for monkey in raw_input.split('\n\n'):
        for line in monkey.split('\n'):
            if 'Starting' in line:
                raw_start = line.split(':')[1].split(',')
                start_items = [int(x) for x in raw_start]
            elif 'Operation' in line:
                oper = line.split(':')[1].split('=')[1].strip()
            elif 'Test' in line:
                test = int(line.split()[-1])
            elif 'If true' in line:
                trueTest = int(line.split()[-1])
            elif 'If false' in line:
                falseTest = int(line.split()[-1])

        monkeys.append( Monkey(start_items, test, trueTest, falseTest, oper))

    round_two_monkeys = deepcopy(monkeys)

    for i in range(20):
        for monkey in monkeys:
            steps = monkey.work_round()
            for task in steps:
                monkeys[task[1]].catch(task[0])#

    activity_level = []
    for monkey in monkeys:
        activity_level.append(monkey._inspect_ctr)
    activity_level.sort()
    print("Part 1: level of monkey business is: %d" % (activity_level[-1] * activity_level[-2]))

    # The part one solution runs into trouble after about 300 iterations
    #
    # however we can do "maths". The idea is that modulo (%) of the dividend (the "stress factor" of the item),
    # of the lowest common divisor (lcm) of the multiple of all the divisors, can be used to get the same results. 
    # This keeps the dividend size within the realms of normal computation
    lcm = math.lcm(*[monkey.test_divisor for monkey in  round_two_monkeys])

    activity_level.clear()
    for monkey in round_two_monkeys:
        # Not actually needed to do, but want to keep the internal state correct
        monkey._relief_factor = 1
        # Insert the Lowest Common Multiple to each monkey
        monkey.lcm = lcm

    for i in range(10000):
        if i % 1000 == 0:
            print("Processing iteration: %d" % i)

        for monkey in round_two_monkeys:
            steps = monkey.work_round()
            for task in steps:
                round_two_monkeys[task[1]].catch(task[0])

    for monkey in round_two_monkeys:
        activity_level.append(monkey._inspect_ctr)
    activity_level.sort()
    print("Part 2: level of monkey business is: %d" % (activity_level[-1] * activity_level[-2]))


    print("End of Line")
    return 0


if __name__ == "__main__":
    main()
