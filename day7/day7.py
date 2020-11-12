"""https://adventofcode.com/2016/day/7"""
import re


def abba_finder(string):
    """Find occurances of 4 letter palindromes"""
    for idx in range(len(string)-3):
        if string[idx:idx+4] == string[idx:idx+4][::-1]:
            if string[idx] != string[idx+1]:
                return True
    return False


def supports_ssl(supernets, hypernets):
    """Find out of IP supports SSL"""
    abas = []
    for sequence in supernets:
        for idx in range(len(sequence)-2):
            if sequence[idx] == sequence[idx+2]:
                if sequence[idx] != sequence[idx+1]:
                    abas.append(sequence[idx:idx+3])
    if not abas:
        return False
    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        for hyper in hypernets:
            if bab in hyper:
                return True
    return False


count = 0
ssl_count = 0
with open('./day7/input.txt') as f:
    data = f.readlines()
for ip in data:
    strings = re.split(r'[\[\]]', ip.strip('\n'))
    # every odd string is inside brackets
    supernets = strings[::2]
    hypernets = strings[1::2]
    ssl_count += supports_ssl(supernets, hypernets)
    results = []
    for idx, string in enumerate(strings):
        if not idx % 2:
            results.append(abba_finder(string))
        else:
            if abba_finder(string):
                break
    else:
        count += any(results)

print(f'Supports TLS: {count}')
print(f'Supports SSL: {ssl_count}')
