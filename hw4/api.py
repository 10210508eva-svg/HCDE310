## api.py: my HW3 fetch.py code, moved into functions so the web app can use it.
# Instead of input() I get the term from the form, and instead of print() I return the data.

import requests

URL = "https://api.artic.edu/api/v1/artworks/search"

# Same FIELDS as my HW3, I want to use these fields inthe api and these will all be shown on result page.
FIELDS = "id,title,artist_title,artist_display,date_display,place_of_origin,department_title,artwork_type_title"


# I ask ai to help me write the fake artworks data so I can use it in the skeleton version of search_art() without calling the real API.
# Fake data for testing without calling the real API.
FAKE_ARTWORKS = [
    {"title": "Lion (One of a Pair, South Pedestal)",
     "artist_title": "Edward Kemeys",
     "date_display": "1893",
     "place_of_origin": "Chicago",
     "department_title": "Arts of the Americas",
     "artwork_type_title": "Sculpture"},

    {"title": "Baroque Pearl Mounted as a Cat Holding a Mouse",
     "artist_title": None,
     "date_display": "17th century",
     "department_title": "Applied Arts of Europe"},
]

#this is the fake version of search function, it will return artworks from the fake artworks.
def search_art_fake(term):
    # Skeleton version: no internet, always the same 2 artworks
    return clean_artworks(FAKE_ARTWORKS)


# the request + status check are my HW3 code, I think most of the code here are from HW3
def search_art(term):
    """Searches for artworks and returns a list, or None if the API fails."""

    params = {
        "q": term,
        "fields": FIELDS,
        "limit": 10,
    }

    try:
        response = requests.get(
            URL,
            params=params,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/json"
            },
            timeout=10
        )

        # Same status check as HW3
        if response.status_code != 200:
            print(f"API error: {response.status_code}")
            return None
        data = response.json()
        artworks = data["data"]

        return clean_artworks(artworks)

    except (requests.RequestException, ValueError, KeyError, TypeError):
        print("Your request failed.")
        return None

# This code is also from my HW3, but I changed it to use the cleaned-up artwork dictionaries instead of the raw API data.
def clean_artworks(artworks):
    """Returns artwork information with defaults for missing fields."""

    results = []

    for art in artworks:
        # Same defaults as HW3
        title = art.get("title") or "Unknown title"
        artist = art.get("artist_title") or "Unknown artist"
        year = art.get("date_display") or "Unknown date"
        location = art.get("place_of_origin") or "Unknown location"
        department = art.get("department_title") or "Unknown department"
        type = art.get("artwork_type_title") or "Unknown type"

        results.append({
            "title": title,
            "artist": artist,
            "year": year,
            "location": location,
            "department": department,
            "type": type
        })

    return results


# From my HW3 (Part 3), hand-written.
# The AI changed one line because clean_artworks uses "artist".
def count_by_artist(artworks):
    """Takes a list of artwork dictionaries and returns artist counts."""

    counts = {}

    for artwork in artworks:
        artist = artwork["artist"]

        if artist in counts:
            counts[artist] += 1
        else:
            counts[artist] = 1

    return counts