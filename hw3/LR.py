#!/usr/bin/env python
import argparse
import sys,math
import model_lr
import heapq
from collections import namedtuple

parser = argparse.ArgumentParser(description='Simple phrase based decoder.')
parser.add_argument('-i', '--input', dest='input', default='data/input', help='File containing sentences to translate (default=data/input)')
parser.add_argument('-t', '--translation-model', dest='tm', default='data/tm', help='File containing translation model (default=data/tm)')
parser.add_argument('-s', '--stack-size', dest='s', default=1, type=int, help='Maximum stack size (default=1)')
parser.add_argument('-n', '--num_sentences', dest='num_sents', default=sys.maxint, type=int, help='Number of sentences to decode (default=no limit)')
parser.add_argument('-l', '--language-model', dest='lm', default='data/lm', help='File containing ARPA-format language model (default=data/lm)')
parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,  help='Verbose mode (default=off)')
opts = parser.parse_args()

tm = model_lr.TM(opts.tm, sys.maxint)
lm = model_lr.LM(opts.lm)
sys.stderr.write('Decoding %s...\n' % (opts.input,))
input_sents = [tuple(line.strip().split()) for line in open(opts.input).readlines()[:opts.num_sents]]

hypothesis = namedtuple('hypothesis', 'logprob, lm_state, predecessor, phrase')

for f in input_sents:
    # The following code implements a DP monotone decoding
    # algorithm (one that doesn't permute the target phrases).
    # Hence all hypotheses in stacks[i] represent translations of
    # the first i words of the input sentence.
    # HINT: Generalize this so that stacks[i] contains translations
    # of any i words (remember to keep track of which words those
    # are, and to estimate future costs)
    initial_hypothesis = hypothesis(0.0, lm.begin(), None, None)

    states={}
    check_times={}

    check_times[(lm.begin(),0,0,0,0)]=[]
    for length in xrange(0,len(f)):

        check_times[(lm.begin(),0,0,0,0)].append(0)


    states[(lm.begin(),0,0,0,0)]=0.0
    p={}

    for i in xrange(0,len(f)):
        for j in xrange(i+1,len(f)+1):
            if f[i:j] in tm:
                for e in tm[f[i:j]]:
                    p[(i+1,j,e.english)]=e.logprob

    for pp in p:
        if pp[0]<=5:    #reordering limits
            logprob=p[pp]


            for e in pp[2].split():
                (lm_state,word_logprob)=lm.score(lm.begin(),e)
                logprob+=word_logprob

            temp=(lm_state,pp[1]-pp[0]+1,pp[0],pp[1],pp[1])
            states[temp]=logprob

            check_times[temp]=[]
            for ite in xrange(0,len(f)):
                check_times[temp].append(0)
            for ite in xrange(pp[0],pp[1]+1):
                check_times[temp][ite-1]=1



    for i in xrange(1,len(f)+1):
        print i

        temp_states={}
        for st in states:
            if st[1]==i:   # topology

                 for pp in p:   # no penalty for reordering yet
                     judge=False
                     if abs(pp[0]-st[4])<5 and (pp[0]>st[3] or pp[1]<st[2]):
                         y_new=[]

                         for ii in xrange(0,len(f)):
                             if check_times[st][ii]==0:
                                y_new.append(0)
                             else:
                                 y_new.append(1)

                         for temp in xrange(pp[0],pp[1]+1):
                             if y_new[temp-1]==1:
                                 judge=True
                                 break

                             #y_new[temp-1]+=1

                         if judge==False:
                             for temp in xrange(pp[0],pp[1]+1):
                                 y_new[temp-1]+=1

                             logprob=p[pp]
                             for e in pp[2].split():
                                 (lm_state,word_logprob)=lm.score(st[0],e)
                                 logprob+=word_logprob
                             n=st[1]+pp[1]-pp[0]+1
                             if pp[0]==st[3]+1:
                                 l=st[2]
                                 m=pp[1]
                             elif pp[1]==st[2]-1:
                                 l=pp[0]
                                 m=st[3]
                             else:
                                 l=pp[0]
                                 m=pp[1]
                             r=pp[1]

                             temp_states[(lm_state,n,l,m,r)]=logprob
                             check_times[(lm_state,n,l,m,r)]=[]

                             for iterator in y_new:
                                check_times[(lm_state,n,l,m,r)].append(iterator)

                         else:
                             continue

        for st in temp_states:
            states[st]=temp_states[st]



    stacks = [{} for _ in f] + [{}]
    stacks[0][lm.begin()] = initial_hypothesis
    for i, stack in enumerate(stacks[:-1]):
        # extend the top s hypotheses in the current stack
        for h in heapq.nlargest(opts.s, stack.itervalues(), key=lambda h: h.logprob): # prune
            for j in xrange(i+1,len(f)+1):
                if f[i:j] in tm:
                    for phrase in tm[f[i:j]]:
                        logprob = h.logprob + phrase.logprob
                        lm_state = h.lm_state


                        if lm_state==('<s>','the'):
                            print

                        for word in phrase.english.split():
                            #print lm_state
                            (lm_state, word_logprob) = lm.score(lm_state, word)
                            #print lm_state
                            logprob += word_logprob
                        logprob += lm.end(lm_state) if j == len(f) else 0.0
                        new_hypothesis = hypothesis(logprob, lm_state, h, phrase)
                        if lm_state not in stacks[j] or stacks[j][lm_state].logprob < logprob: # second case is recombination
                            stacks[j][lm_state] = new_hypothesis

    # find best translation by looking at the best scoring hypothesis
    # on the last stack
    print stacks[3]#[('army','turkish')]
    print stacks[2]#[('army',)]
    print stacks[22]
    break
    winner = max(stacks[-1].itervalues(), key=lambda h: h.logprob)
    def extract_english_recursive(h):
        return '' if h.predecessor is None else '%s%s ' % (extract_english_recursive(h.predecessor), h.phrase.english)
    print extract_english_recursive(winner)

    if opts.verbose:
        def extract_tm_logprob(h):
            return 0.0 if h.predecessor is None else h.phrase.logprob + extract_tm_logprob(h.predecessor)
        tm_logprob = extract_tm_logprob(winner)
        sys.stderr.write('LM = %f, TM = %f, Total = %f\n' %
            (winner.logprob - tm_logprob, tm_logprob, winner.logprob))



__author__ = 'hanz'
