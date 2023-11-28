import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

colors=[bcolors.OKBLUE,  bcolors.OKCYAN, bcolors.OKGREEN, bcolors.WARNING, bcolors.FAIL, bcolors.HEADER, bcolors.BOLD]

for x in range(100):
    time.sleep(1)
    color=colors[x%len(colors)]
    print(f"{color}{str(x).rjust(3)}{bcolors.ENDC }",end="\r") 