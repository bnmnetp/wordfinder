from flask import render_template
from app import app
import itertools

@app.route('/')
def index():
    return "Hello world"

@app.route('/words/<string:letters>')
def letters_2_words(letters):
    with open('sowpods.txt') as f:
        good_words = set(x.strip().lower() for x in f.readlines())

    word_set = set()
    for l in range(3,len(letters)+1):
        for word in itertools.permutations(letters,l):
            w = "".join(word)
            if w in good_words:
                word_set.add(w)


    return render_template('wordlist.html', wordlist=sorted(word_set))
