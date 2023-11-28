from utils import check_args

def create_freqency_table(*args):
    values= check_args(args)
    table={}
    for value in values:
        table[value]=table.get(value,0)+1
    return table
