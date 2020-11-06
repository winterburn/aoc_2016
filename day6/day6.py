from collections import defaultdict
letters_per_pos = defaultdict(lambda: defaultdict(int))
word = ''
with open('./day6/input.txt') as f:
    messages = f.readlines()
for message in messages:
    for idx, letter in enumerate(message.strip('\n')):
        letters_per_pos[idx][letter] += 1
for pos in letters_per_pos:
    word += sorted(letters_per_pos[pos].items(),
                   key=lambda x: x[1], reverse=True)[0][0]
print(word)
