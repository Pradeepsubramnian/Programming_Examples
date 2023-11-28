

def read_int(prompt='? '):
    return int(input(prompt))

total=read_int('total? ')
count=0
max=None
max2=None

while count<total:
    count+=1
    number = read_int(f'number #{count} ? ')
    if  max == None or number>max:
        if max !=None:
            max2=max
        max=number
    elif max2==None or number>max2:
        max2=number

if max==max2:
    max2=None
    
print(f'The Second Highest number is {max2}')

