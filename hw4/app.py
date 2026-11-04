# app.py: the routes for my art search app.
#
# Pseudocode:
#
#  (home page)
#  I want to show home.html, which has the big "Find Artworks" title and the search bar from my sketch.
#
#  (results page)
#   1. First I get the word the user typed in the search bar. This is like input() in my HW3,
#      but now it comes from the form.
#   2. If the user didn't type anything (or only spaces), I send them back to the home page
#      with a message telling them to type something. I check this first so I don't call the API for nothing.
#   3. Then I call search_art(term) from api.py, which is my HW3 code inside a function.
#   4. If search_art gives me None, I think that means the API didn't work, so I go back to
#      the home page and show an error message instead of crashing.
#   5. If I get an empty list, there are no results, so I show "No results found" like I did in HW3.
#   6. If there are results, I use my count_by_artist function from HW3 to count the artists.
#   7. Last, I show results.html with the artworks and the counts. This replaces print() from HW3.

from flask import Flask, render_template, request   # request (Flask) reads the form, not requests!
from api import search_art, count_by_artist

app = Flask(__name__)


#the routes are my code, but the AI wrote the docstrings and comments
@app.route("/")
def home():
    """Shows the search page (home.html) with the search bar."""
    return render_template("home.html")


@app.route("/results")
def results():
    """Reads what the user searched, calls the API, and shows the results or a helpful message."""
    # 1. the term from the form; "term" has to match name="term" in home.html
    #    .strip() so only spaces counts as empty too
    term = request.args.get("term", "").strip()

    # 2. empty input -> check this BEFORE calling the API
    if not term:
        return render_template("home.html", message="Please type something to search for, like cat or monet.")

    # 3. call my HW3 code (switch to search_art_fake to test the skeleton)
    artworks = search_art(term)

    # 4. API error -> search_art gave back None
    if artworks is None:
        return render_template("home.html", message="Sorry, something went wrong while searching the museum. Please try again in a minute.")

    # 5. no results -> same idea as my HW3 message
    if not artworks:
        return render_template("home.html", message=f'No results found for "{term}". Please try some other term.')

    # 6 + 7. it worked: count the artists (HW3 Part 3) and show the results page
    counts = count_by_artist(artworks)
    return render_template("results.html", term=term, artworks=artworks, counts=counts)