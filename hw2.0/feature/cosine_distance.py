#!/usr/bin/env python
import argparse
import re, math
import json
import os
import sys
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

text1 = 'This is a foo bar sentence .'
text2 = 'This sentence is similar to a foo bar sentence .'

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

cosine = get_cosine(vector1, vector2)

#print 'Cosine:', cosine



argparser = argparse.ArgumentParser(prog='extract')
argparser.add_argument('-x', '--pairs', dest='pairs', default='data/en-cs.pairs', help='Reference-Hypothesis pairs')
args = argparser.parse_args()

lc = 0
sys.stderr.write('Extracting features for (ref,hyp) pairs from %s.\n' % args.pairs)
# loop over all (ref,hyp) pairs in the input file and extract evaluation features

for ref_hyp in open(args.pairs):
    lc += 1
    ref, hyp = ref_hyp.rstrip().split(' ||| ')
    hwords = hyp.lower().split()
    rwords = ref.lower().split()
    temp1=''
    temp2=''
    for i in hwords:
        temp1+=i
    for i in rwords:
        temp2+=i
    print temp1
    print temp2
    v1=text_to_vector(temp1)
    v2=text_to_vector(temp2)
    cosine=get_cosine(v1,v2)
    print {'cos-distance':-cosine}



