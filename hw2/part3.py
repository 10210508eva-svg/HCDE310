# HW2 Part 3 – Counting with a dictionary
#
# In `part3.py`:
#
# 1. Build a dictionary counting works per artist, and print it: `{'Vincent van Gogh': 1, ...}`. A
#    work with no artist counts under `'Unknown'`.
# 2. Print the artist with the most works: `Most works: Claude Monet (2)`
#
# (This is the letter-counting pattern from Class 3, applied to art.)

from artworks import artworks

counts = {}
for artwork in artworks: 
    artist = artwork.get("artist", "Unknown")
    if artist in counts:
        counts[artist] +=1
    else:
        counts[artist] = 1

print(counts)

max=0
max_artist=0
for artist in counts:
    if counts[artist]>max:
        max=counts[artist]
        max_artist=artist

print(f'Most works: {max_artist} ({max})')



