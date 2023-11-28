from libs.utils import check_args
    
def sum(*args):
    numbers=check_args(args)
    total=0
    for number in numbers:
        total+=number

    return total

def average(*args):
    numbers=check_args(args)
    return sum(numbers)/len(numbers)