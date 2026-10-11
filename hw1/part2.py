# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles
number = 1
for title in titles:
    print(f'{number}. {title}')
    number=number +1

print("Titles:", number-1)

count =0
for tit in titles:
    if 'a' in tit.lower():
        count=count+1
print(f'Titles with an "a": {count}')

length=0
longest= ""
for t in titles:
    if length< len(t):
        length=len(t)
        longest=t

print(f'Longest: {longest}')

