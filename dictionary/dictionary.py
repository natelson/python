import json
from difflib import get_close_matches

def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    close_words = get_close_matches(word, data.keys(), cutoff=0.8)
    if len(close_words) > 0:
        x = input("Did you mean {} . Y/N".format(close_words[0]))
        if x.upper() == 'Y':
            return data[close_words[0]]
        else:
            return 'Make new search.'
    else:
        return 'Word not found.'

data = json.load(open('data/data.json'))

while True:
    word = input("Enter the word you want to search:")
    answear = meaning(word)
    if type(answear) == list:
        for item in answear:
            print(item)
    else:
        print(answear)

    more_words = input("Are you want search new words? Y/N")
    if more_words.upper() == 'N':
        break

