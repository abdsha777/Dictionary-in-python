import json
import time
from difflib import get_close_matches

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

def search(word):
    word = word.lower()
    ans = data.get(word)
    ans = str(ans)
    if(ans=='None'):
        s = get_close_matches(word, data.keys())
        print(f"Did you mean {s}?")
    else:
        print(ans)


    for i in range(5):
        print('..',end="")
        time.sleep(0.1)
    print('\n')

data = json.load(open("dictonary/data.json"))
i=2

while(i!='0'):
    i = input("-------Dictonary-------\nPress 1 for searching a meaning of a word\npress 0 to exit\nEnter your choice: ")
    if(i == '1'):
        word = input("Enter you Word: ")
        search(word)
    elif(i=='0'):
        break

    else:
        print(f"{bcolors.WARNING}\n.....Invalid Input.....\n{bcolors.ENDC}")
        print("")

