def label(year):
    if year <1900:
        return "old"
    return "modern"

print(label(1889), label(1942))

titles= ["Nighthwaks", "THe bedroom", "Sky above clauds IV"]

def title_with(word, titles):
    """" Return a list of titles with the word in it """
    title_with_word =[]
    for t in titles:
        if word in t.lower():
            title_with_word.append(t)
    return title_with_word

print(title_with("the", titles))
