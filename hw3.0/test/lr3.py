#!/usr/bin/env python
from __future__ import division
import argparse
import sys,math
import model_lr
import heapq
import copy
from collections import namedtuple

parser = argparse.ArgumentParser(description='Simple phrase based decoder.')
parser.add_argument('-i', '--input', dest='input', default='input0_3', help='File containing sentences to translate (default=data/input)')
parser.add_argument('-t', '--translation-model', dest='tm', default='../data/tm', help='File containing translation model (default=data/tm)')
parser.add_argument('-s', '--stack-size', dest='s', default=1, type=int, help='Maximum stack size (default=1)')
parser.add_argument('-n', '--num_sentences', dest='num_sents', default=sys.maxint, type=int, help='Number of sentences to decode (default=no limit)')
parser.add_argument('-l', '--language-model', dest='lm', default='../data/lm', help='File containing ARPA-format language model (default=data/lm)')
parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False,  help='Verbose mode (default=off)')
opts = parser.parse_args()

tm = model_lr.TM(opts.tm, sys.maxint)
lm = model_lr.LM(opts.lm)
sys.stderr.write('Decoding %s...\n' % (opts.input,))
input_sents = [tuple(line.strip().split()) for line in open(opts.input).readlines()[:opts.num_sents]]

def extract_english(states,result0):
        pre=states[result0[1]][result0][1]
        strr=states[result0[1]][result0][2]
        return '' if pre is None else '%s%s ' % (extract_english(states,pre),strr )

file1=file('lagrange0_3','w+')
file0=file('result0_3','w+')
line_num=0
for f in input_sents:
    # The following code implements a DP monotone decoding
    # algorithm (one that doesn't permute the target phrases).
    # Hence all hypotheses in stacks[i] represent translations of
    # the first i words of the input sentence.
    # HINT: Generalize this so that stacks[i] contains translations
    # of any i words (remember to keep track of which words those
    # are, and to estimate future costs)
    print >>file1,line_num
    p={}   # edge
    u={}   # langrange mutiplier
    times=60



    for ii in xrange(1,len(f)+1):
        u[ii]=0


    last_value=0
    llambda=0

    origin=[]
    for length in xrange(0,len(f)):
            origin.append(0)



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
        states=[]
        check_times=[]

        for ite in xrange(0,len(f)+1):
                states.append({})
                check_times.append({})




        check_times[0][(lm.begin(),0,0,0,0)]=copy.deepcopy(origin)




        states[0][(lm.begin(),0,0,0,0)]=[0.0,None,'']
        begin=(lm.begin(),0,0,0,0)

        #for pp in p:
         #   if pp[0]<=5:

        for ss in xrange(1,6):   #reordering limits
            if ss in p:
                for t3 in p[ss]:
                    nn=t3-ss+1
                    lagrange=0
                    check_temp=copy.deepcopy(origin)
                    for ite in xrange(ss,t3+1):
                                check_temp[ite-1]+=1

                    for ite1 in xrange(ss,t3+1):
                            lagrange+=u[ite1]

                    for p_p in p[ss][t3]:
                        logprob=p_p[0]
                        sttr=p_p[1]


                        for e in sttr.split():
                            (lm_state,word_logprob)=lm.score(lm.begin(),e)
                            logprob+=word_logprob

                        logprob-=0.1*ss  #distortion penalty
                        logprob+=lagrange

                        temp=(lm_state,nn,ss,t3,t3)

                        if temp not in states[nn] or states[nn][temp][0]<logprob:
                            states[nn][temp]=[logprob,begin,sttr]
                            check_times[nn][temp]=copy.deepcopy(check_temp)

                    check_temp=[]




        for i in xrange(1,len(f)):
            #print i
            n=0

            for st in states[i]:
                for ss in xrange(max(1,st[4]-5),st[4]+6):
                    if ss in p:
                        for t3 in p[ss]:
                            if t3<st[2] or ss>st[3]:
                                 n=st[1]+t3-ss+1
                                 distortion=abs(st[4]-t3+1)
                                 if distortion<=5  and n<=len(f):
                                     lagrange=0
                                     for ite1 in xrange(ss,t3+1):
                                             lagrange+=u[ite1]

                                     check_temp=copy.deepcopy(check_times[i][st])
                                     for temp in xrange(ss,t3+1):
                                                check_temp[temp-1]+=1

                                     for p_p in p[ss][t3]:
                                         logprob=p_p[0]
                                         sttr=p_p[1]
                                         logprob+=lagrange
                                         for e in sttr.split():
                                             (lm_state,word_logprob)=lm.score(st[0],e)
                                             logprob+=word_logprob
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

                                         logprob+=states[i][st][0]
                                         logprob-=0.1*distortion

                                         tup=(lm_state,n,l,m,r)
                                         if tup not in states[n] or states[n][tup][0]<logprob:
                                            states[n][tup]=[logprob,st,sttr]
                                            check_times[n][tup]=copy.deepcopy(check_temp)
                                     check_temp=[]







        for ite1 in states[len(f)]:
            states[len(f)][ite1][0]+=lm.end(ite1[0])



        heap={}
        for st in states[len(f)]:

            heap[st]=states[len(f)][st][0]
        winner=max(heap,key=heap.get)
        
        judge=False
        for iite in check_times[len(f)][winner]:
            if iite!=1:
                judge=True
                break

        if judge==False or tt==times:
            break
        else:
            print >>file1,tt,
            print >>file1,'times:',

            for ite in xrange(1,len(f)+1):
                if tt==0:
                    llambda=0

                else:
                    if heap[winner]>last_value:
                        llambda+=1

                    last_value=heap[winner]

                u[ite]=u[ite]-(check_times[len(f)][winner][ite-1]-1)*1/(1+llambda)
                print >>file1,u[ite],
            print >>file1

    stt=extract_english(states,winner)

    print >>file0,stt
    line_num+=1




__author__ = 'hanz'
