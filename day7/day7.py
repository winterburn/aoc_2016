
import re


def abba_finder(string):
    """Find occurances of 4 letter palindromes"""
    for idx in range(len(string)-3):
        if string[idx:idx+4] == string[idx:idx+4][::-1]:
            if string[idx] != string[idx+1]:
                return True
    return False


count = 0
with open('./day7/input.txt') as f:
    data = f.readlines()
for ip in data:
    strings = re.split(r'[\[\]]', ip.strip('\n'))
    # every odd string is inside brackets
    results = []
    for idx, string in enumerate(strings):
        if not idx % 2:
            results.append(abba_finder(string))
        else:
            if abba_finder(string):
                break
    else:
        count += any(results)

print(count)
