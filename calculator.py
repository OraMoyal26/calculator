import math

def plus(args):
    return sum(args)

def minus(args):
    return args[0]-args[1]

def multiply(args):
    return math.prod(args)

def divide(args):
    if args[1]==0:
        raise ValueError("Division by zero is not allowed")
    return args[0]/args[1]