
def read_int(prompt='? '):
    return int(input(prompt))

def read_float(prompt='? '):
    return float(input(prompt))

def read_bool(prompt='? ',default_response=True):
    answer=input(prompt).lower()
    if answer=='yes' or answer=='y' or answer=='true' or answer=="ok":
        return True
    elif answer=='no' or answer=='n' or answer=='false' or answer=='cancel':
        return False
    else:
        return default_response