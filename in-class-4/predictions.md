# Class 4: Five broken snippets

Your name: Riley Fang
Collaborator: Karen

# Part 1: Predict

**Don't run anything yet.** Read each snippet in `exercise.py` and write your guesses. A wrong guess is fine: the point is to compare.

## Snippet 1
- Which line breaks? I think this line will break print("Find it in room " + exhibit["Room"]
- What error will Python show? (the kind and the message)? It will be a key error, we try to ask key form dictionary and they type R instead of r, this cause the key error.
- What's the fix? Change R to r

## Snippet 2
- Which line breaks?I think this line will break print("Find it in room " + exhibit["Room"]
- What error will Python show? (the kind and the message)? It will be a type error. "Find it in th room" is a string and room is a number(int)
- What's the fix?  Change + to , it will fix the error because we 

## Snippet 3
- Which line breaks?print(i + 1, exhibits[i]) 
- What error will Python show? (the kind and the message)? It is a index error, they add i+1 in the for loops and it will cuade i be 1 index bigger then this list have.
- What's the fix? We remove the +1 from for loop.

## Snippet 4
- Which line breaks? print(count_visits(visit, 243))
- What error will Python show? (the kind and the message)? it will be name error because it write visit instead of visits, there is no "visit" list in this code
- What's the fix? write visits instead of visit

## Snippet 5
- Which line breaks? print(title.upper())
- What error will Python show? (the kind and the message)? I'm not sure what error type it is. I think this will cause error because we don't have return in the longest_title() and so title actully contain nothing and it is not able to print out.
- What's the fix?

# Part 2: Run

Run `python3 exercise.py`. Python stops at the first error, so fix that snippet in `exercise.py`, run again, and see the next one. Fill in what actually happened.

## Snippet 1
- Which line broke?
- What error did Python show?
- What's the fix?

## Snippet 2
- Which line broke?
- What error did Python show?
- What's the fix?

## Snippet 3
- Which line broke?
- What error did Python show?
- What's the fix?

## Snippet 4
- Which line broke?
- What error did Python show?
- What's the fix?

## Snippet 5
- Which line broke?
- What error did Python show?
- What's the fix?

When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

- Snippet #:
- Our guess before asking:
- Chat:
- Did it give you too much? What did you do?
