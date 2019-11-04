from flask import render_template, request
from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import itertools

class WordForm(FlaskForm):
    avail_letters = StringField("Letters")
    submit = SubmitField('Go')


@app.route('/')
def index():
    form = WordForm()
    return render_template('index.html', form=form)

@app.route('/words', methods=['GET','POST'])
def letters_2_words():
    with open('sowpods.txt') as f:
        good_words = set(x.strip().lower() for x in f.readlines())

    form = WordForm()
    if form.validate():
        letters = form.avail_letters.data
    else:
        print("NOT TRUE", form.errors)

    word_set = set()
    for l in range(3,len(letters)+1):
        for word in itertools.permutations(letters,l):
            w = "".join(word)
            if w in good_words:
                word_set.add(w)


    return render_template('wordlist.html', wordlist=sorted(word_set))
