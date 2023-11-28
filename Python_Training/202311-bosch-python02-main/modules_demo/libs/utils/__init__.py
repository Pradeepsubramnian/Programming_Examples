def check_args(args):
    if type(args) is not tuple:
        return args
    if len(args)==1 and (type(args[0])==tuple or type(args[0])==list or type(args[0])==set):
        return args[0]
    else:
        return args