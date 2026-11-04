1. What surprise me: I think my ai did a lot of things for me in this homewhok, I'm surprise that it is this smart. I think they actully mmade something really good and i'm glad to see that.

2. What I change, I think i ask my ai to help me cthink of how to write Spec each piece. I keep getting confuse when i reading it, I fix some part myself because I think no one can understand it.

3. 
Questions: I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I follow a routine: Try → Predict → Run → Explain → Log.

My attempt so far: [paste your code or plan, even if it doesn't work] Where I'm stuck: [one sentence] The function I need: [name]([inputs]) takes [what] and returns [what].

Rules: - Write only this one function, about 10 lines or fewer. No other code, and don't change mine. - Put # AI-written on the line above the function. - Start the function with a one-line docstring that says what it takes and returns. - Use only what a beginner would know: loops, if, lists, dictionaries, and the libraries I'm already using. If you need something new, tell me its name and what it does in one line. - Don't explain the code yet. Ask me to predict what it returns for [one real input]. Wait for my prediction. - After I've run it and told you the result, ask me to explain each line in my own words. Correct anything I got wrong, then ask me about one line I skipped. - Then suggest one small change I could make myself (don't write it). Wait until I tell you what I changed. - Then ask me: what's one thing that surprised you? Don't answer it for me. - For anything other than this one function, act as my tutor: hints and questions, no code.

Answer: I can help you with your entire Python assignment, but I'll follow the rules in your prompt so that you're still learning and writing your own code.

Here's exactly how I'll help:
1. Planning: Help you understand the assignment, break it into smaller steps, and develop pseudocode. I'll give hints and ask guiding questions instead of writing code.
2. Writing code: I can write one function at a time, around 10 lines or fewer, with # AI-written above it and a one-line docstring. I won't change your existing code.
3. Predicting: Before explaining the function, I'll ask you to predict its output using a real input.
4. Testing: You'll run the code and tell me what happened. I'll help you investigate errors through questions and hints.
5. Explaining: You'll explain the code line by line. I'll correct misunderstandings and ask about anything you skipped.
6. Improving: I'll suggest one small change for you to implement yourself.
7. Reflecting: I'll ask what surprised you, without writing your reflection for you.
What I won't do
- Write your entire assignment or multiple functions at once.
- Write your routes, HTML, or other code outside the one requested function.
- Give you complete solutions when you're supposed to work through them yourself.
- Skip the prediction, explanation, testing, or reflection steps.
One important thing
You can still ask me conceptual questions! For example, if you're confused about Flask routes, API responses, dictionaries, or how your files connect, I can explain the concepts in beginner-friendly language without giving you the code.

And if you're stuck, I can give increasingly specific hints until you figure it out.

Send me your assignment instructions, what you've tried, and where you're stuck. I'll help you from there while following your learning routine: Try → Predict → Run → Explain → Log.

questions: Due: Tue Nov 3, 10am AI: Stage 3 – Little helper (at most one function per prompt) Individual

Build on your HW3 script to make a small web app: a user searches for art and sees useful results. Reuse your HW3 API code, and replace input() and print() with a form and a results page.

This time you plan before you build. The plan is what you'd hand in even without AI, and it's what you give the AI (Stage 3) when you ask it for a piece.

Steps
Sketch the screens. Sketch a search page and a results page, with the bare minimum the page needs. Paper is fine; take a photo.
Write down the data. Which fields from the API response do you actually need on the results page (for example: title, artist, image)? Your HW3 sample response helps.
Spec each piece. For each function or route: what goes in, what comes out, and 2–3 checks: things you'll try in the browser to know it works (for example: search "monet" and see results; submit an empty form and see a message).
Pseudocode. Write the steps as # comments in app.py before you write any code.
Skeleton. Get the whole path working with fake data first: form → /results → a template showing a hard-coded list (see class 9).
One piece at a time. Replace the fake parts with real ones. Commit each time something works.
Steps 1–3 go in plan.md; the pseudocode goes in app.py. Write them before the code they describe.

Where things go (recommended, like the books example in Class 9): - api.py: your HW3 API code, inside a function (for example search_art(term)) that returns the list of artworks - app.py: the routes. Each one reads the input, calls your api.py function, and renders a template - templates/: the HTML pages (home.html, results.html) 

What you need to build:
Your assignment checklist:

Questions: What is Spec each piece suppost to be?

Answer: “Spec each piece” means writing a short plan for what each function or route is supposed to do before you start coding.

For your HCDE 310 HW4, your professor wants you to describe three things for each piece:

1. Input: What information does it receive?
2. Output: What should it return or display?
3. Checks: 2–3 things you can test to make sure it works.

### Example for your Art Search App

You can put something like this in your `plan.md`:

| Piece                       | Input                      | Output                                  |
| --------------------------- | -------------------------- | --------------------------------------- |
| `home()` route              | User visits `/`            | Displays the search page                |
| `results()` route           | Search term from the form  | Displays artwork results                |
| `search_art(term)` function | Search term like `"monet"` | Returns a list of artworks from the API |

### What are checks?

Checks are specific tests you will perform to verify that each piece works.

For example, for your `results()` route:

- Check 1: Search for `"monet"` → The results page displays artworks.
- Check 2: Submit an empty search → The page displays a message instead of crashing.
- Check 3: Search for something that doesn't exist → The page displays a "No results found" message.

### How to write it in `plan.md`

### Piece: results() route

**Input:** A search term entered by the user.

**Output:** A results page showing artworks related to the search term.

**Checks:**

1. Search for "monet" and check if artworks appear.
2. Submit an empty search and check if a message appears.
3. Search for something with no matching artworks and check if "No results found" appears.

Important: You don't need to explain every line of code here. You're describing what each piece should accomplish, not how to program it.

One question for you: Do you think your `search_art(term)` function should return an HTML page or a list of artwork dictionaries? Think about the difference between what `api.py` and `app.py` are responsible for.

Questions: should I use the code our in class 10 use in herea? I think they ar esuper similar (I have attathed what i have)

Answer: Yes!! You should definitely use your Class 10 code as a reference for HW4! They're very similar because both involve building a Flask web app that searches an API and displays results.

However, you shouldn't copy everything directly. Your HW4 has some specific requirements about what you need to write yourself.

### What you can reuse

| Class 10 (Books App) | Your HW4 (Art App)           | What to do                        |
| -------------------- | ---------------------------- | --------------------------------- |
| `app.py`             | `app.py`                     | Reuse the overall Flask structure |
| `/` route            | `/` route                    | Write this yourself               |
| `/results` route     | `/results` route             | Adapt the logic for artwork       |
| `home.html`          | `home.html`                  | Write this yourself               |
| `results.html`       | `results.html`               | Adapt for artwork results         |
| Books API            | Art Institute of Chicago API | Reuse your HW3 API code           |
| Empty/error messages | Empty/error messages         | Use the same concepts             |

### What I recommend

Since you've already practiced handling empty inputs, missing results, and API errors in Class 10, you can use those same ideas for HW4.

Your process should be:

1. Start with Class 10 as a reference, rather than starting completely from scratch.
2. Write your own `home()` route and `home.html` based on what you learned in class.
3. Make your `results()` route display fake artwork data first.
4. Replace fake artwork data with your HW3 API function.
5. Test your error cases.

### What about your HTML?

If you've already written `home.html` and `results.html`, keep them! You don't need to recreate them unless something is missing.

I can't see the actual contents of your attached files in this message, so I haven't verified your code yet.

Can you paste your current `app.py` here? I'll help you compare it with Class 10 and identify what you can reuse, what you need to change, and what you should write yourself.

I'll follow your Stage 3 rules: hints and questions only for existing routes and HTML, rather than writing them for you.

Questions: Do you have idea how to write psecode?
Answer: Yes! For your HCDE 310 HW4, your pseudocode should describe how your Art Search web app works step by step, without writing actual Python code.

Since your assignment says to put pseudocode as `# comments` in `app.py`, let's plan what you need.

### 1. `home()` route — Search page

Think about what happens when someone first visits your website.

Your pseudocode should cover:

- What happens when a user visits `/`?
- Which HTML page should Flask display?

This should be very short, probably 2–3 comments.

### 2. `results()` route — Results page

This is the main part of your app.

Think about the order of these actions:

Get the search term from the form

Check whether the input is empty

Call your HW3 API function

Handle the API response

Results found / No results / API error

Display the results in `results.html`

Try turning each of these steps into a `# comment` in your own words.

### 3. `search_art(term)` function — API

This belongs in `api.py`, not `app.py`.

Because you're reusing HW3, think about:

- How do you send the search term to the Art Institute of Chicago API?
- How do you get the artwork information from the response?
- What should the function return if no artworks are found?

### Let's start with your own attempt

Before I give you more detailed hints, try writing the pseudocode for just your `results()` route.

You don't need perfect wording or Python syntax.

Question: After Flask receives the search term from `home.html`, what do you think it should check before calling your API?

Write your answer as a `# comment`, and we'll build from there!

Question:
Can you help me rewrite api base on my old code, attatchement is my old code

Answer:
Yes! We can turn your old HW3 API code into a search_art(term) function for HW4.
I couldn't access the old code attachment, though. Can you paste your HW3 fetch.py code here or upload the file again? I want to work from your actual code rather than write something completely new.
 
# AI-written
# Fake data for the skeleton (step 5): same shape as data["data"] in my sample_response.json.
# The second one has missing fields on purpose, like the Baroque Pearl cat with no artist.
FAKE_ARTWORKS = [
    {"title": "Lion (One of a Pair, South Pedestal)", "artist_title": "Edward Kemeys",
     "date_display": "1893", "place_of_origin": "Chicago",
     "department_title": "Arts of the Americas", "artwork_type_title": "Sculpture"},
    {"title": "Baroque Pearl Mounted as a Cat Holding a Mouse", "artist_title": None,
     "date_display": "17th century", "department_title": "Applied Arts of Europe"},
]


# AI-written
def search_art_fake(term):
    # Skeleton version: no internet, always the same 2 artworks
    return clean_artworks(FAKE_ARTWORKS)


# AI-written (the request + status check are my HW3 code, the AI put them in a function)
def search_art(term):
    """Takes the search term from the form and returns a list of artworks, or None if the request failed."""
    params = {
        "q": term,          # the user's search term, same as HW3 but from the form not input()
        "fields": FIELDS,
        "limit": 10,
    }
    try:
        response = requests.get(
            URL,
            params=params,
            headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"},
            timeout=10)     # don't let the page wait forever if the museum doesn't answer
    except requests.RequestException:
        # no answer at all (no wifi, wrong website), so there's no status code to check
        print("Your request failed: no answer from the API")
        return None

    # Same check as HW3: only use the data if the status code is 200
    if response.status_code != 200:
        # this print is for me in the terminal, the user sees a friendly message from app.py
        print(f'Your request failed with status code {response.status_code}: {response.reason}')
        return None

    data = response.json()
    artworks = data["data"]     # same path as HW3: the list of artworks is in data["data"]
    return clean_artworks(artworks)


# AI-written (the loop body is my HW3 printing loop, but it saves into a dict instead of print())
def clean_artworks(artworks):
    """Takes the raw artworks from the API and gives back only the fields I show, with no None."""
    results = []
    for art in artworks:
        # same defaults as HW3, `or` catches null values (.get alone would give None)
        title = art.get("title") or "Unknown title"
        artist = art.get("artist_title") or "Unknown artist"
        year = art.get("date_display") or "Unknown date"
        location = art.get("place_of_origin") or "Unknown location"
        department = art.get("department_title") or "Unknown department"
        type = art.get("artwork_type_title") or "Unknown type"

        results.append({"title": title, "artist": artist, "year": year,
                        "location": location, "department": department,
                        "type": type})
    return results