"""
Script:  NLPmarkdown.py
Purpose:  Customizes the analyze_book1.py code example from Think Python, 2nd Edition, by Allen Downey (http://thinkpython2.com)
http://thinkpython2.com/code/analyze_book1.py by adding Natural Language Toolkit for finding the root of a word

Reads files from a list of files that may be in multiple folders
"""

from __future__ import print_function, division

import random
import string
import re
import os
import nltk
from nltk.stem import WordNetLemmatizer

def process_file(filename, wordHist, skip_header):
    """Makes a wordHistogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    try:
        fp = open(filename.strip("\n"))
    except:
        print("\nDOUBLE CHECK OPENING: ", filename)
    if skip_header:
        skip_header(fp)
    try:    
        for line in fp:
            process_line(line, wordHist)
    except:
        print("\nDOUBLE CHECK PROCESSING LINES IN", filename)
    return wordHist

def skip_header(fp):
    """Reads from fp until it finds the line that ends the header
    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break

def process_line(line, wordHist):
    """Adds the words in the line to the wordHistogram.
    Modifies wordHist.
    line: string
    wordHist: wordHistogram (map from word to frequency)
    """
    strippables = string.punctuation + string.whitespace + string.digits

    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = re.sub("/", " ", word)
        word = word.lower()

        # remove URLs
        if word.startswith('http') or word.startswith('https') or word.startswith('www.'):
            continue
        elif word.endswith('.pdf') or word.endswith('online') or word.endswith('.org'):
            continue
        elif '.....' in word:
            continue
        elif '-' in word:
            continue
        else:
            # update the wordHistogram
            wordHist[word] = wordHist.get(word, 0) + 1
 
def most_common(wordHist):
    """Makes a list of word-freq pairs in descending order of frequency.
    wordHist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    c = [(value,key) for key, value in wordHist.items()]
    c.sort()
    c.reverse()
    return c

def print_most_common(wordHist, sumFile,num=10):
    """Prints the most commons words in a wordHistgram and their frequencies.
    wordHist: wordHistogram (map from word to frequency)
    num: number of words to print
    """
    c = most_common(wordHist)
    print("\n", num, ' MOST COMMON WORDS:', file = sumFile)
    for freq, word in c[:num]:
        print(word, '\t', freq, file=sumFile)

def subtractDict(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2
    d1, d2: dictionaries
    """
    res = {}
    for key, value in d1.items():
        if key not in d2:
            res[key] = value
    return res

def total_words(wordHist):
    """Returns the total of the frequencies in a wordHistogram."""
    return sum(wordHist.values())


def different_words(wordHist):
    """Returns the number of different words in a wordHistogram."""
    return len(wordHist)


def main(grammarFile,Documnts,longwordsFile,totWordsFile,outputFilename,summaryFile):

    lemmatizer = WordNetLemmatizer()
    grammarHist = {}
    grammarWords = process_file(grammarFile, grammarHist, skip_header=False)
    # Version 1 read all files in one folder
    #Documnts = [os.path.join(root, file) for root, folder, Documnt in os.walk(inputFolder) for file in Documnt]

    complexity = 10
    wordHist = {}
    for Documnt in Documnts:
        filename = re.sub('[\']','',Documnt)
        wordHist = process_file(filename, wordHist, skip_header=False)
    commonWords = most_common(wordHist)
    meaningWords = subtractDict(wordHist, grammarWords)
    
    longWords = [key for key,value in meaningWords.items() if len(key) > complexity and len(key) < complexity+5 and not re.findall('[^A-Za-z0-9]',key)]
    rootLong = [lemmatizer.lemmatize(longWord) for longWord in longWords]
    rootLong.sort()
    fo = open(longwordsFile, 'w')
    print(rootLong,file=fo)
    fo.close()

    fw = open(totWordsFile, 'w')
    print(total_words(wordHist),file=fw)
    print(different_words(wordHist),file=fw)
    fw.close()

    print("Summary statistics in ", summaryFile)
    fs = open(summaryFile,"w")
    print("NUMBER OF DOCUMENTS REVIEWED", len(Documnts), file=fs)
    print('\nTOTAL WORDS:', total_words(wordHist), file=fs)
    print('\nTOTAL DIFFERENT WORDS:', different_words(wordHist), file=fs)
    print_most_common(meaningWords,fs,50)
    print('\nTOTAL COMPLEX WORDS:', len(longWords), file=fs)
    print('\nCOMPLEX WORDS:', longWords, file=fs)

    # get stats for each document
    print("\nComputing statistics for each document")
    wordHist = {}
    docStatsRow = {}
    docStats = []
    totWords = 0
    difWords = 0
    totLongWords = 0
    for Documnt in Documnts:
        name = Documnt.split("/")
        wordHist = {}
        filename = re.sub('[\']','',Documnt)                            # strip the single quote so the file will open
        wordHist = process_file(filename, wordHist, skip_header=False)
        commonWords = most_common(wordHist)
        longWords = subtractDict(wordHist, grammarWords)
        longWords = [key for key,value in meaningWords.items() if len(key) > complexity and len(key) < complexity+5 and not re.findall('[^A-Za-z0-9]',key)]
        longWords.sort()

        totWords += total_words(wordHist)
        difWords += different_words(wordHist)
        totLongWords +=  len(longWords)

        docStatsRow['FILE_NAME'] = filename
        docStatsRow['TOT_WORDS']= total_words(wordHist)
        docStatsRow['TOT_DIF_WORDS'] = different_words(wordHist)
        docStatsRow['TOT_LONG_WORDS'] = len(longWords)
        docStatsRow['LONG_WORDS'] = longWords
        docStats.append(docStatsRow)
        docStatsRow = {}

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    df = pd.DataFrame(docStats)
    df.index.name = 'IDX'
    df.to_csv(outputFilename)

    print("\nFile statistics have been saved in ",outputFilename)

if __name__ == '__main__':
    grammarFile = 'resources/grammarWords.txt'
    longwordsFile = "/home/$USERNAME/test/Results/NLPv2_complexWords.txt"
    totWordsFile = "/home/$USERNAME/test/Results/NLPv2_totWordcount.txt"
    outputFilename = "/home/$USERNAME/test/Results/NLPv2_docStats.csv"
    summaryFile = "/home/$USERNAME/test/Results/NLPv2_summary.txt"
    # reads all files from a list of filenames
    with open("/home/$USERNAME/test/docsFiles.txt") as filenames:
        Documnts = ["/home/$USERNAME/"+filename for filename in filenames]
    main(grammarFile,Documnts,longwordsFile,totWordsFile,outputFilename,summaryFile)
