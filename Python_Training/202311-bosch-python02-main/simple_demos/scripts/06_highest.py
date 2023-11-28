

def read_int(prompt='? '):
    return int(input(prompt))

total=read_int('total? ')
count=1
max=read_int('number #1 ? ') # assume first number as the max

while count<total:
    count+=1
    number = read_int(f'number #{count} ? ')
    if number>max:
        max=number

print(f'The Highest number is {max}')

