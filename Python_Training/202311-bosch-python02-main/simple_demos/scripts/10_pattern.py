from console import read_int

def main():
    n=read_int('n? ')
    row=0
    while row<n:
        row+=1
        item=0
        while item<row:
            print('*', end='\t')
            item+=1
        print()

    

main()