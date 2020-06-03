# Nadia
An NLP web-app written using TextBlob

## Intro

Nadia is an basic web-app using **TextBlob** and Flask. Enter the text and run a command to analyse it. Currently has 6 built in functions to parse, tag etc. Uses the **Wordnet** Corpora based out of **NLTK**. These are the functions as described on the site:

- pol - Checks for sentiment of the text (positive or negative)
- sub - Checks for subjectivity of the text (objective or subjective)
- spel - Corrects the spelling of the text
- parse - Parses the text
- noun - Finds the nouns in the text
- tag - Tags the words in the text 

## Get Started

Install all the dependencies using:

```
$ pip install r-requirements.txt
```

**Note:** There may be some trouble installing TextBlob, so download it independently using pip or conda install

## Pip Version

```
$ pip install -U textblob
$ python -m textblob.download_corpora
```
## Conda Version 

```
$ conda install -c conda-forge textblob
$ python -m textblob.download_corpora
```

Clone the repo and run:

```
$ python app.py
```

## To-do

- [ ] Organise the webpage
- [ ] Add backlinks
- [ ] Deploy to Heroku
