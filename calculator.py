import math

def plus(args):
    args = [int(char) for char in args]
    return sum(args)

def minus(args):
    args = [int(char) for char in args]
    return args[0]-args[1]

def multiply(args):
    args = [int(char) for char in args]
    return math.prod(args)

def divide(args):
    args = [int(char) for char in args]
    if args[1]==0:
        raise ValueError("Division by zero is not allowed")
    return args[0]/args[1]