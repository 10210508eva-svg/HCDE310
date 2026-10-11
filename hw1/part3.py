# HW1 Part 3: Decisions
# Run it:  python3 part3.py
# Your output must match expected/part3.txt exactly.

from artworks import titles, years

cutoff = 1900  # works made before this year are "old"

n=0
for year in years:
    if year>cutoff:
        print(titles[n])
    n=n+1

print()
num=0
for y in years:
    if y> cutoff:
        print(f'{titles[num]}: modern')
    else:
        print(f'{titles[num]}: old')
    num=num+1

print()
old=0
modern=0
for yea in years:
    if yea<1900:
        old= old+1
    else:
        modern=modern+1

print("Old:", old)
print("Modern:", modern)
    