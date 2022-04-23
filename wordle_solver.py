from os import path
import sys
import re

if len(sys.argv) != 3:
    print("Error: Incorrect number of arguments", file=sys.stderr)
    exit(1)

GUESS_LEN = 5

guess = sys.argv[1].lower()
excl = sys.argv[2].lower()

wrong_pos = {}
pattern = '\[[a-z]+\]'
wp_search = re.search(pattern, guess)

while wp_search is not None:
    group = wp_search.group()
    index = wp_search.span()[0]

    wrong_pos[index] = group[1:-1]
    guess = guess.replace(group, '-', 1)

    wp_search = re.search(pattern, guess)

if len(guess) != GUESS_LEN or re.search('[^a-z|-]', guess) is not None:
    print("Error: Invalid guess argument", file=sys.stderr)
    exit(1)
elif re.search('[^a-z]', excl) is not None:
    print("Error: Invalid exclusions argument", file=sys.stderr)
    exit(1)

word_list_name = 'word_list.txt'
word_list_path = f'{path.dirname(path.abspath(__file__))}/{word_list_name}'

with open(word_list_path, 'r') as file:
    words = file.read().splitlines()

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

r = re.compile(pattern)
matches = list(filter(r.match, words))

for word in matches:
    print(word)
