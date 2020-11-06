from collections import defaultdict
import re


def letter_count(words):
    """Count the letters in the room name"""
    count = defaultdict(int)
    for word in words:
        letters = list(word)
        for letter in letters:
            count[letter] += 1
    return sorted(sorted(count.items(), key=lambda x: x[0]),
                  key=lambda x: x[1], reverse=True)


def real_room(count, checksum):
    """Decipher if the room is real or not"""
    for idx, letter in enumerate(checksum):
        if letter == count[idx][0]:
            continue
        if peek(count, idx):
            continue
        return False
    return True


def peek(count, idx):
    """Recursively peek into the list of characters"""
    if count[idx][1] == count[idx+1][1]:
        if count[idx][0] == count[idx+1][0]:
            return True
        else:
            return peek(count, idx+1)
    return False


with open('./day4/input.txt', 'r') as f:
    input = f.readlines()
id_count = 0
for line in input:
    splitted_string = line.strip('\n').split('-')
    count = letter_count(splitted_string[:-1])
    id = re.search('[0-9]*', splitted_string[-1]).group(0)
    checksum = list(splitted_string[-1].removeprefix(id)[1:-1])
    if real_room(count, checksum):
        id_count += int(id)

print(id_count)
