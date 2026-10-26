# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
data["data"][0]["title"] The first data means the whole json. We use data to call it because in the total number of results, we also use data to call the whole json. The second data we use is the data list (artwork list) inside this json. The 0 means the first artwork in the list, and title will get the title from this artwork. The first title is "Lion (One of a Pair, South Pedestal)."

## 2. Find 3 more fields you'd want to show a user, and their paths
Find location: data["data"][0]["place_of_origin"] will show Chicago.
Find department: data["data"][0]["department_title"] will show Arts of the Americas.
Find artwork_type_title: data["data"][0]["artwork_type_title"] will show Sculpture.


## 3. Which fields are `null` for some works?
I found that artist_title is null for the third artwork, "Baroque Pearl Mounted as a Cat Holding a Mouse." I think we can display "Unknown artist" instead of None when the artist information is missing.

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*
I think it will probably get an error because the URL is empty right now. It might ask me to enter something for "Search the Art Institute for: " and then it will get an error because the rest of the code is not ready yet.

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*

The program asked me to enter something for "Search the Art Institute for:" and I entered "cat". After that, I got an error called MissingSchema because invalid URL. The error happened on response = requests.get(url, params=params), because there is no valid URL for the program to request data from.