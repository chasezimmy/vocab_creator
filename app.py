# -*- coding: utf-8 -*-
import random
import json
import cardsource
from bs4 import BeautifulSoup as bs

def pick_rand(vocab):
    if len(vocab) < 20:
        rand = vocab
    else:
        rand = random.sample(vocab, 20)
    return rand


def make_deck():
    vocab = {}
    card_source = [cardsource.BASIC, cardsource.ADVANCED] # Include source file

    list_name = ["basic", "advanced"]

    for n, source in enumerate(card_source):

        soup = bs(source, "html.parser")
        vocab_list = soup.find(class_='SetPage-termsList')

        for child in vocab_list:

            term = child.find(class_='SetPageTerm-wordText').find(class_='TermText').getText().strip()
            definition = child.find(class_='SetPageTerm-definitionText').find(class_='TermText').getText().strip()

            vocab[term] = {"def": definition, "learned": False, "list": list_name[n]}
    
    with open('test.json', 'w') as outfile:
        json.dump(vocab, outfile)


if __name__=='__main__':

    for n in range(0, 50):

        with open('vocab.json') as data_file:    
            vocab = json.load(data_file)

        learned = {}

        word_list = []
        for word in vocab:
            word_list.append(word)
        random_list = pick_rand(word_list)

        for term in random_list:
            learned[term] = {"def": vocab[term]["def"], "list": vocab[term]["list"]}
            vocab.pop(term, None)
        filename = 'week/week%d.json' % n
        with open(filename, 'w') as outfile:

            json.dump(learned, outfile)

        with open('vocab.json', 'w') as outfile:
            json.dump(vocab, outfile)
    
