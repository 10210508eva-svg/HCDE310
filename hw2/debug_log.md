# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
*copy it exactly*
fangyixuan@fangyixuandeMacBook-Pro-246 HCDE310 % /Users/fangyixuan/Desktop/HCDE310/.venv/bi
n/python /Users/fangyixuan/Desktop/HCDE310/hw2/part3.py
Traceback (most recent call last):
  File "/Users/fangyixuan/Desktop/HCDE310/hw2/part3.py", line 16, in <module>
    if artwork["artist"] in counts:
       ~~~~~~~^^^^^^^^^^
KeyError: 'artist'

### 2. What I thought it meant
I thought KeyError meant that the dictionary didn't have this key. I thought I needed to either change something in my code or check whether the key actually existed in the dictionary.

### 3. What it actually meant
I realized that the error meant the key didn't exist in the dictionary. I originally thought "artist" existed in every dictionary, but the error occurred because some dictionaries were missing this key.
### 4. The fix
I can use .get("artist", "unknown") to get artist's name. If the dictionary contains the "artist" key, it will return the artist's name. If the key is missing, it will return "unknown" instead. 
## Entry 2

### 1. Error message
*copy it exactly*
fangyixuan@fangyixuandeMacBook-Pro-246 hw2 % /Users/fangyixuan/Desktop/HCDE310/.venv/bin/py
thon /Users/fangyixuan/Desktop/HCDE310/hw2/part4.py
  File "/Users/fangyixuan/Desktop/HCDE310/hw2/part4.py", line 27
    counts = {}
               ^
IndentationError: unindent does not match any outer indentation levelfangyixuan@fangyixuandeMacBook-Pro-246 hw2 % /Users/fangyixuan/Desktop/HCDE310/.venv/bin/py
thon /Users/fangyixuan/Desktop/HCDE310/hw2/part4.py
  File "/Users/fangyixuan/Desktop/HCDE310/hw2/part4.py", line 27
    counts = {}
            
IndentationError: unindent does not match any outer indentation level

### 2. What I thought it meant
I wasn't quite sure what this error meant. At first, I thought I wasn't allowed to create a dictionary here, but the assignment asked me to create one. I was struggling to understand what went wrong. I also thought the IndentationError might be caused by incorrect spacing, so I tried adjusting the spaces to fix it.

### 3. What it actually meant
I asked Claude for help, and it explained that Python was having trouble with the indentation before counts = {}. The problem wasn't that I couldn't create a dictionary there, is that the indentation didn't match the structure of my code.

### 4. The fix
I needed to adjust the indentation of counts = {} so that it was at the correct level. In my code, it should be aligned with the for loop instead of the def statement. 