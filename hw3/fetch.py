# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display,place_of_origin,department_title, artwork_type_title"

# Functions go here (above the code that runs)


term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"      # TODO: the search URL from step 2
params = {
    "q": term,
    "fields": FIELDS
    }   # TODO: q (the search term) and fields (FIELDS)
response = requests.get(
    url,
    params=params,
    headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})

# TODO step 3: check response.status_code before you use the data
# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results
def count_by_artist(artworks):
    """Takes a list of artwork dictionaries and returns artist counts."""
    counts = {}
    for artwork in artworks:
        artist = artwork.get("artist_title", "Unknown")
        if artist is None:
            artist = "Unknown"
        if artist in counts:
            counts[artist] += 1
        else:
            counts[artist] = 1
    return counts

def save_results(artworks, filename): 

    with open(filename, "w") as file:
        for art in artworks:
            title = art.get("title") or "Unknown title"
            artist = art.get("artist_title") or "Unknown artist"
            date = art.get("date_display") or "Unknown date"
            department = art.get("department_title") or "Unknown department"
            file.write(f"{title} - {artist} ({date}, {department})\n")


print(response.status_code)

if response.status_code != 200:
    print(f'Your request failed with status code {response.status_code}: {response.reason}')
else:
    data = response.json()
    artworks = data["data"]
    if not artworks:
        print("No results found. Please try some other term.")
    else:
        for art in artworks:
            title = art.get("title") or "Unknown title"
            artist = art.get("artist_title") or "Unknown artist"
            year = art.get("date_display") or "Unknown date"
            location = art.get("place_of_origin") or "Unknown location"
            department = art.get("department_title") or "Unknown department"
            type = art.get("artwork_type_title") or "Unknown type"

            print(f'{title} - {artist} ({year})')
            print(f"Location: {location}")
            print(f"Department: {department}")
            print(f"type: {type}")
            print()
            print(count_by_artist(artworks))
    save_results(artworks, "results.txt")




