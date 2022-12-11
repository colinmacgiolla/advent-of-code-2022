#!/bin/python


class Monkey:
    '''
    Arguments:
        items: Initial list of items
        test: divisible by X (the test)
        trueTest: target monkey if true
        falseTest: target monkey if false
        operation: the string describing the operation performed by the monkey

    
    '''

    def __init__(self, items: list[int] , test: int, trueTest: int, falseTest: int, operation: str):
        self._relief_factor = 3

        self.items = items
        
        self.test_divisor = test
        self._true_target = trueTest
        self._false_target = falseTest
        self._inspect_ctr = 0

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

    print("%d monkeys created" % len(monkeys))
    for i in range(20):
        for monkey in monkeys:
            steps = monkey.work_round()
            for task in steps:
                monkeys[task[1]].catch(task[0])

    activity_level = []
    for monkey in monkeys:
        activity_level.append(monkey._inspect_ctr)
    activity_level.sort()
    print("Part 1: level of monkey business is: %d" % (activity_level[-1] * activity_level[-2]))


    


    print("End of Line")




       
    return 0


if __name__ == "__main__":
    main()
