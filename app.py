#!python3

from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    out = ''
    if request.method == 'POST' and 'label' in request.form:
        label = request.form.get('label')
        command = request.form.get('command')
        out = nlp_run(label, command)
    return render_template("index.html",
	                        out=out)

def nlp_run(label, command):
    text = TextBlob(label)
    sentvalue = text.sentiment.polarity
    subvalue = text.sentiment.subjectivity
    tags = text.tags
    parse = text.parse()
    nouns = text.noun_phrases
    correct = text.correct()
    if command == "pol":
        if sentvalue < 0:
            tst = "The polarity is " + str(sentvalue) + " ," "which means the text is negative"
            return tst
        elif sentvalue > 0:
            tst = "The polarity is " + str(sentvalue) + " ," "which means the text is positive"
            return tst
        elif sentvalue == 0:
            tst = "Polarity cannot be detected :("
            return tst
    
    elif command == "spel":
        return correct
    elif command == "tag":
        tst = str(tags)
        return tst
    elif command == "parse":
        tst = str(parse)
        return tst
    elif command == "noun":
        tst = str(nouns)
        return tst
    elif command == "sub":
        if subvalue > 0.5:
            tst = "The subjectivity is " + str(sentvalue) + " ," "which means the text is subjective"
            return tst
        elif subvalue < 0.5:
            tst = "The subjectivity is " + str(sentvalue) + " ," "which means the text is objective"
            return tst
        elif subvalue == 0.5:
            tst = "subjectivity cannot be detected :("
            return tst
    

if __name__ == '__main__':
    app.run()
    app.debug = True
    



    