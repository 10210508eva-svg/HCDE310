# HW2 Part 6 – AI log (`ai_log.md`)

The tutor walks you through the routine (Try → Predict → Run → Explain → Log) as you chat, so your transcript shows most of it. In `ai_log.md`:

---

## 1. One prediction
*copy one prediction you made in a chat. Were you right? If not, what surprised you?*
I ask my ai to brainstorm with me one how to do part 3. I have .gee("artist", "unknown") there and it said that it is a good starting point. I think i'm right because it if the first thing you nee dto do in a forloop, we don't want out code crah becuas eof the data missing. 
here is the thing they give me 
1. Loop through the artworks and get each one’s artist. You’ve started this.
2. Keep a counting dictionary and add 1 to that artist’s count each time.
3. After the loop, find which artist has the biggest count.
I surprise thay they give me a big overview of what I can do. I thinkk it wasn't too help ful tho, it just give me some overview that i might need to do.

## 2. What clicked
*pick one thing you were stuck on or didn't know. Without looking at the transcript, explain it in your own words.*
I didn't know how to add a dictionary to a list. I asked AI what specific method I should use to add things to a list. I think it explained how to do it, but it didn't give me the exact answer. I had to ask multiple questions and try different things while working on my code. Eventually, I figured out how to use .append() to add a dictionary to a list, and I now understand how it works.

## 3. Too much?
*Did the tutor ever give you too much? What did you do? (one line)*
I think the AI tutor gave me helpful information without giving me the exact answer. I could Google the terms it suggested if I needed more help. It never wrote the code for me and only answered my questions, so I don't think it gave me too much information.

## 4. Transcripts
*paste every tutor chat you used for HW2 (one is fine if that's all you had)*
Q. what will the code shows if one variable are missing in list of dictionay
A. Good question. The answer depends on exactly how your code tries to read that missing value, and there’s more than one way to do it.

Before we get to predicting, could you paste the code where you loop through your list of dictionaries and read the values out, even if it isn’t finished?

Q. A screenshot of part3. brainstorm with me how to do this
A. Good start. You’re already using .get() with a default of "Unknown", and that’s a smart way to handle a missing key. It’s also part of the answer to the question you asked earlier.

Here’s the big-picture plan, without any code:

Loop through the artworks and get each one’s artist. You’ve started this.
Keep a counting dictionary and add 1 to that artist’s count each time.
After the loop, find which artist has the biggest count.

Before we get to steps 2 and 3, let’s make sure step 1 works. Your editor has put a yellow squiggle under art on the last line. Without running it yet, what do you predict will happen when Python reaches that line, and why?

Q. should i create a decitonary manually?
A. Not by hand, no. If you typed the counts in yourself, your code would break the moment the data changed. Your code should build the dictionary while the loop runs: you start with an empty one before the loop, and the loop fills it in. That’s the same idea as the letter-counting pattern from Class 3 that your assignment mentions.

We’ll get to that step soon. First let’s make sure step 1 actually runs, so here’s my question again: what do you predict Python will do when it reaches art.get(...), given the squiggle under art?

Q. how to add dictionary into list
A.Good news: you already know the tool for this. A dictionary can go into a list like any other item, using the same .append() from the snacks example. The list doesn’t care what kind of thing you put in it.

Here’s a tiny example with different data:

python
pets = []
pets.append({"name": "Mochi", "age": 3})
print(pets)

Predict: what do you think this will print? Pay attention to which brackets you expect to see on the outside and which on the inside.

Q. Do you know how to add things into dictionary ? i want earch artist be a category
A. Yes. “Each artist as a category” is exactly right: each artist will be a key, and the number of works will be its value.

Here’s a tiny example with different data and a different task (no counting involved):

python
pets = {}
pets["Mochi"] = 3
print(pets)

Predict: what do you think this will print?

Q. A scrreenshot of my error on part 3 (key error)

A. You’ve made real progress here. You fixed art → artwork, corrected the key to "artist", started with an empty counts dictionary, and wrote the if/else counting logic yourself.

Now for the error. A KeyError means you asked a dictionary for a key it doesn’t have. Using square brackets, something["key"], means “give me this key, and crash if it isn’t there.” The 'artist' after the colon tells you which key Python couldn’t find.

So the code is working fine for most artworks and then hits one dictionary that doesn’t have an "artist" key at all.

Which line do you think the traceback is pointing to, and which artwork in your list do you think caused it?

Q. fangyixuan@fangyixuandeMacBook-Pro-246 hw2 % /Users/fangyixuan/Desktop/HCDE310/.venv/bin/py
thon /Users/fangyixuan/Desktop/HCDE310/hw2/part4.py
  File "/Users/fangyixuan/Desktop/HCDE310/hw2/part4.py", line 27
    counts = {}

A.Now I can see the full error. Here’s what this kind of error means in plain language.

IndentationError means Python is upset about the spacing at the start of a line, not about the code itself. Python uses indentation to decide which lines belong together, like which lines are inside a def, a for, or an if. Lines in the same group have to start at exactly the same column.

“unindent does not match any outer indentation level” means a line moved back to the left, but it stopped at a spot that doesn’t line up with any earlier line. Picture lines at 0 spaces and 4 spaces, and then a line at 2 spaces. Python can’t tell which group that line belongs to. A common hidden cause is mixing tabs and spaces: two lines can look lined up on screen even though Python counts them differently.

Feedback on your section 2: you were right that this is about spacing, and right to suspect that making a dictionary there wasn’t the problem. That’s a good instinct. What’s missing is the idea that the spacing has to match another specific line exactly.

Here’s what will help you write sections 3 and 4. Which line above line 27 do you think counts = {} is supposed to line up with, and does its starting position match that line exactly?

