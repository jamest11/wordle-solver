import sys
import os
import re

GUESS_LEN = 5

if len(sys.argv) not in range(2, 4):
    print("Error: Incorrect number of arguments", file=sys.stderr)
    exit(1)

guess = sys.argv[1].lower()
excl = '' if len(sys.argv) == 2 else sys.argv[2].lower()

wrong_loc = {}
pattern = '\[[a-z]+\]'
re_search = re.search(pattern, guess)

while re_search is not None:
    group = re_search.group()
    index = re_search.span()[0]

    wrong_loc[index] = group[1:-1]
    guess = guess.replace(group, '-', 1)

    re_search = re.search(pattern, guess)

if len(guess) != GUESS_LEN or re.search('[^a-z|-]', guess) is not None:
    print("Error: Invalid guess argument", file=sys.stderr)
elif re.search('[^a-z]', excl) is not None:
    print("Error: Invalid exclusions argument", file=sys.stderr)

word_list_name = 'word_list.txt'
word_list_path = f'{os.path.dirname(os.path.abspath(__file__))}/{word_list_name}'

with open(word_list_path, 'r') as file:
    words = file.read().splitlines()

pattern = ''
for s in set(list(''.join(wrong_loc.values()))):
    pattern += f'(?=.*{s})'

for i in range(GUESS_LEN):
    g_c = guess[i]

    if i in wrong_loc.keys():
        wl_s = wrong_loc[i]
        pattern += f'[^{wl_s + excl}]'
    elif g_c == '-':
        pattern += f'[^{excl}]'
    else:
        pattern += g_c

r = re.compile(pattern)
matches = list(filter(r.match, words))

for s in matches:
    print(s)
