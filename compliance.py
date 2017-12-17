#!/usr/bin/env python3
import sys
from os import path
import re


TRANSLATION = {'diversity': 'schmiversity',
                'entitlement': 'schmentitlement',
                'evidence-based': 'schmevidence-based',
                'fetus': 'schmetus',
                'science-based': 'schmience-based',
                'transgender': 'schmansgender',
                'vulnerable': 'schmulnerable'}

files_to_process  = sys.argv[1:]

def getcasetranslation(word, transdict):
    if word.lower() == word:
         return transdict.get(word,word)
    elif word.title() == word:
         return transdict.get(word.lower(),word).title()
    elif word.capitalize() == word:
        return transdict.get(word.lower(),word).capitalize()
    return word

def translate(line, translation):
    translated_words = [getcasetranslation(w,translation) for w in line.split()]
    return ' '.join(translated_words)

for filename in files_to_process:
    with open(filename) as f:
        content = f.readlines()
        f.close()
        result = []
        for line in content:
            result.append(translate(line, TRANSLATION))
        with open(filename + '_compliant','w') as f:
            f = open(filename+'_compliant','w')
            for line in result:
                f.writelines(line + '\n')
            f.close()
        print('Fixed ' + str(len(result)) + ' compliance breaches in: ' + filename)
