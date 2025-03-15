
def process(text):
    words = text.split()
    count_words = len(words)
    return count_words

def calculate_letters(text):
    letters = dict()
    for le in text:
        if le.isalpha() :
            le = le.lower()
            letters[le] = letters.get(le,0) + 1
    return letters

def sort_dict(letters):
    return dict( sorted(letters.items(), key= lambda item : item[1] ,reverse=True) )
    