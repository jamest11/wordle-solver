from os import path
import sys
import re

if len(sys.argv) != 3:
    print("Error: Incorrect number of arguments", file=sys.stderr)
    exit(1)

GUESS_LEN = 5

guess = sys.argv[1].upper()
excl = sys.argv[2].upper()

wrong_pos = {}
pattern = '\[[A-Z]+\]'
wp_search = re.search(pattern, guess)

while wp_search is not None:
    group = wp_search.group()
    index = wp_search.span()[0]

    wrong_pos[index] = group[1:-1]
    guess = guess.replace(group, '-', 1)

    wp_search = re.search(pattern, guess)

if len(guess) != GUESS_LEN or re.search('[^A-Z|-]', guess) is not None:
    print("Error: Invalid guess argument", file=sys.stderr)
    exit(1)
elif re.search('[^A-Z]', excl) is not None:
    print("Error: Invalid exclusions argument", file=sys.stderr)
    exit(1)

pattern = ''
for c in set(list(''.join(wrong_pos.values()))):
    pattern += f'(?=.*{c})'

for i in range(GUESS_LEN): 
    if i in wrong_pos.keys():
        pattern += f'[^{wrong_pos[i] + excl}]'
    elif guess[i] == '-':
        pattern += f'[^{excl}]'
    else:
        pattern += guess[i]

word_list_path = path.join(path.dirname(path.abspath(__file__)), 'word_list.txt')

with open(word_list_path, 'r') as file:
    words = file.read().splitlines()

r = re.compile(pattern)
matches = filter(r.match, words)

for word in matches:
    print(word)
