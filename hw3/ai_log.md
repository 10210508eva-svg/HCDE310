# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*
def save_results(artworks, filename):  
    for art in artworks:
        title = art.get("title") or "Unknown title"
        artist = art.get("artist_title") or "Unknown artist"
        date = art.get("date_display") or "Unknown date"
        return f"{title} - {artist} ({date})\n"

## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*
Q. I attatched a screenshot and sent the part 4 prompt to it.
A. Your attempt is a good start! You're already using .get() and or to handle missing artwork information.

Here's a completed version of your function, keeping it beginner-friendl
# AI-written
def save_results(artworks, filename):
    """Takes artworks and a filename, then saves artwork details to a text file."""
    with open(filename, "w") as file:
        for art in artworks:
            title = art.get("title") or "Unknown title"
            artist = art.get("artist_title") or "Unknown artist"
            date = art.get("date_display") or "Unknown date"
            file.write(f"{title} | {artist} | {date}\n")

One new concept: with open(filename, "w") opens a file for writing and automatically closes it when finished.
Step 2: Predict (don't run it yet!)
Imagine we have this artwork data:

artworks = [
    {"title": "Starry Night", "artist_title": "Vincent van Gogh", "date_display": "1889"},
    {"title": "The Great Wave", "artist_title": "Hokusai"}
]
My question: If we call save_results(artworks, "results.txt"), what do you think will appear inside results.txt?

Pay special attention to the second artwork, which doesn't have a date.

Tell me your prediction first, and then we'll run it and compare!

Q I think title artist and date will all be record ?
A Yes! Your prediction is correct for the first artwork. The function should record the title, artist, and date on one line for each artwork.

But notice that the second artwork doesn't have a date_display value.

Before running it: What do you think the function will write for that missing date?

After you've made your prediction, run the function and tell me what appears in results.txt.

Q WIll get to repolace none to unknow?
A Yes! Exactly! 👍

There's one small difference:
- .get("date_display") retrieves the date, or returns None if the key doesn't exist.
- or "Unknown date" replaces a missing or other falsy value with "Unknown date".
So your prediction is correct! The second artwork should show Unknown date.

Now it's time for the Run step!

Run your function and check results.txt.

Tell me what appears in the file. Then I'll ask you to explain each line of the function in your own words!


## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*

I think it will contain the title, artist, and date because we put these three variables in the f-string. There will be one artwork on each line, and missing values will show "Unknown title," "Unknown artist," or "Unknown date."

## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*
I think the open() function is super cool. I didn't know we could automatically create a txt file using code. This is something new to me.

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*

I added a new line for department. I changed the code so it will print the department after the date because I want users to know which department the artwork belongs to.