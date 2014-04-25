#!/usr/bin/env python
from __future__ import division
import argparse
import sys,math
import model_lr
import heapq
import copy
from collections import namedtuple

parser = argparse.ArgumentParser(description='Simple phrase based decoder.')
parser.add_argument('-i', '--input', dest='input', default='data/test', help='File containing sentences to translate (default=data/input)')
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

def extract_english(states,result):
    n=result[1]

    pre=states[n][result][1]
    strr=states[n][result][2]
    return '' if pre is None else '%s%s ' % (extract_english(states,pre),strr )





for f in input_sents:
    # The following code implements a DP monotone decoding
    # algorithm (one that doesn't permute the target phrases).
    # Hence all hypotheses in stacks[i] represent translations of
    # the first i words of the input sentence.
    # HINT: Generalize this so that stacks[i] contains translations
    # of any i words (remember to keep track of which words those
    # are, and to estimate future costs)
    p={}   # edge




    origin={}
    for ite in xrange(1,len(f)+1):
            origin[ite]=0



    # get all possible edge from input
    for i in xrange(0,len(f)):
            p[i+1]={}
            for j in xrange(i+1,len(f)+1):
                p[i+1][j]=[]
                if f[i:j] in tm:
                    #p[i+1]=(j,tm[f[i:j]])    # p[i+1][j]=[(prob,english),(prob,english)]
                    for e in tm[f[i:j]]:
                        p[i+1][j].append((e.logprob,e.english))

                        #p[i+1][j].append(e)




    for tt in xrange(0,100):
        states={}
        check_times={}

        for ite in xrange(0,len(f)+1):
                states[ite]={}
                check_times[ite]={}


        begin=(lm.begin(),0,0,0,0)




        check_times[0][begin]=copy.deepcopy(origin)




        states[0][begin]=[0.0,None,'']


        for ss in xrange(1,2):   #reordering limits
            if ss in p:

                for t3 in p[ss]:
                    nn=t3-ss+1


                    if nn<=len(f):

                        check_temp=copy.deepcopy(origin)

                        for ite in xrange(ss,t3+1):
                                  check_temp[ite]+=1

                        for p_p in p[ss][t3]:
                            logprob=-0.1*ss   #distortion penalty
                            logprob+=p_p[0]
                            sttr=p_p[1]


                            for e in sttr.split():
                                (lm_state,word_logprob)=lm.score(lm.begin(),e)
                                logprob+=word_logprob



                            key1=(lm_state,nn,ss,t3,t3)

                            if key1 not in states[nn] or states[nn][key1][0]<logprob:
                                states[nn][key1]=[logprob,begin,sttr]
                                check_times[nn][key1]=copy.deepcopy(check_temp)




        for i in xrange(1,len(f)):
            #print i,
            #print 'level:'
            n=0
            for st in states[i]:
                for ss in xrange(max(1,st[4]-1),st[4]+2):

                    if ss in p:
                        #print
                        #print len(p[ss]),
                        #print ':',
                        for t3 in p[ss]:
                            if t3<st[2] or ss>st[3]:

                                 n=st[1]+t3-ss+1
                                 distortion=abs(st[4]-ss+1)

                                 if  n<=len(f):
                                     judge=False

                                     check_temp=copy.deepcopy(check_times[i][st])
                                     for temp in xrange(ss,t3+1):
                                        check_temp[temp]+=1
                                        if check_temp[temp]>1:
                                            judge=True
                                            break

                                     if judge==True:
                                         continue

                                     if ss==st[3]+1:
                                            l=st[2]
                                            m=t3
                                     elif t3==st[2]-1:
                                            l=ss
                                            m=st[3]
                                     else:
                                            l=ss
                                            m=t3
                                     r=t3






                                     for p_p in p[ss][t3]:
                                         logprob=states[i][st][0]-0.1*distortion


                                         logprob+=p_p[0]
                                         sttr=p_p[1]

                                         for e in sttr.split():
                                             (lm_state,word_logprob)=lm.score(st[0],e)
                                             logprob+=word_logprob

                                         tup1=(lm_state,n,l,m,r)


                                         if tup1 not in states[n] or states[n][tup1]<logprob:
                                            states[n][tup1]=[logprob,st,sttr]
                                            check_times[n][tup1]=copy.deepcopy(check_temp)

        for ite1 in states[len(f)]:
            states[len(f)][ite1][0]+=lm.end(ite1[0])



        heap={}
        for st in states[len(f)]:
            #if st[1]==len(f):
            heap[st]=states[len(f)][st][0]



        winner=max(heap,key=heap.get)
        print winner
        print check_times[len(f)][winner]
        stt=extract_english(states,winner)

        print stt
        break



















__author__ = 'hanz'
