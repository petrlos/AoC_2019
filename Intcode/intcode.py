opcodes = {
    1: lambda a, b: a + b,
    2: lambda a, b: a * b}

def intcode_computer(numbers):

    for i in range(0,len(numbers), 4):
        if numbers[i] == 99:
            return numbers
        num1 = numbers[numbers[i+1]]
        num2 = numbers[numbers[i+2]]
        numbers[numbers[i+3]] = opcodes[numbers[i]](num1, num2)