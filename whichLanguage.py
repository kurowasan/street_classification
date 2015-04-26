from __future__ import division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import collections
import math as m
import re

df_english = pd.read_csv("/Users/jean-francoisrajotte/projects/street_lang/language_names/english_names.txt", sep = ",")
df_french = pd.read_csv("/Users/jean-francoisrajotte/projects/street_lang/language_names/french_names.txt", sep = ",")


def getBigramFrequency(df, n=2):
    """Get the frequency for a defined number of letter
    """
    bigramFreq = {}
    nbOccurence = 0

    for name in df['Name']:
        name = name.lower()

        for i, letter in enumerate(name):
            bigram = ""

            if(i <= len(name) - n):
                for ii in range(n):
                    bigram += str(name[i + ii])

                if(bigram in bigramFreq):
                    bigramFreq[bigram] += 1
                    nbOccurence += 1
                else:
                    bigramFreq[bigram] = 1
                    nbOccurence += 1

    for letter, occurence in bigramFreq.items():
        bigramFreq[letter] = occurence/nbOccurence
    return (bigramFreq)

def getBigramFrequencySingleWord(name, n=2):
    bigramFreq = {}

    nbOccurence = 0
    name = name.lower()
    for i, letter in enumerate(name):
        bigram = ""
        if(i <= len(name) - n):
            for ii in range(n):
                bigram += str(name[i + ii])

            if(bigram in bigramFreq):
                bigramFreq[bigram] += 1
                nbOccurence += 1
            else:
                bigramFreq[bigram] = 1
                nbOccurence += 1

    for letter, occurence in bigramFreq.items():
        bigramFreq[letter] = occurence/nbOccurence
    return (bigramFreq)


##Creating the dictionaries
freqEnglish = list()
freqFrench = list()

for nbLetters in range(4):
    freqEnglish.append(getBigramFrequency(df_english, n=nbLetters))
    freqFrench.append(getBigramFrequency(df_french, n=nbLetters))

for nbLetters in range(1,4):
    for key in freqEnglish[nbLetters]:
        if key not in freqFrench[nbLetters]:
            freqFrench[nbLetters][key] = 0

    for key in freqFrench[nbLetters]:
        if key not in freqEnglish[nbLetters]:
            freqEnglish[nbLetters][key] = 0


trigramEnglish = collections.OrderedDict(sorted(freqEnglish[3].items(), key=lambda x: x[1]))
trigramFrench = collections.OrderedDict(sorted(freqFrench[3].items(), key=lambda x: x[1]))
trigramDiff = collections.OrderedDict({})

for key,value in trigramFrench.items():
    trigramDiff[key] = trigramFrench[key] - trigramEnglish[key]

bigramEnglish = collections.OrderedDict(sorted(freqEnglish[2].items(), key=lambda x: x[1]))
bigramFrench = collections.OrderedDict(sorted(freqFrench[2].items(), key=lambda x: x[1]))
bigramDiff = collections.OrderedDict({})

for key,value in bigramFrench.items():
    bigramDiff[key] = (bigramFrench[key] - bigramEnglish[key]) * m.fabs(bigramFrench[key] - bigramEnglish[key])

def clean_str(word):
    """Remove generic stuff from the street
        Like Rue, Avenue...
    """
    tosub = 'Rue|Avenue|Chemin|Canal|Place|Rang|Boulevard|Autoroute|Pont|Croissant|De la |des |du |de | road| | Street'
    return re.sub(tosub, '', word)


def whichLanguage(word):
    freqWord = list()
    mse = 0
    mse2 = 0

    for nbLetters in range(3):
        freqWord.append(getBigramFrequencySingleWord(clean_str(word), n=(nbLetters + 1)))

    bigram = 0
    trigram = 0

    for key in freqWord[1]:
        if key in bigramDiff.keys():
            bigram += bigramDiff[key]

    for key in freqWord[2]:
        if key in trigramDiff.keys():
            trigram += trigramDiff[key]

    return (bigram + trigram)

if __name__=='__main__':
    for word in df_french['Name']:
        print(word)
        #print(whichLanguage(word, freqEnglish, freqFrench))
        print(whichLanguage(word))
