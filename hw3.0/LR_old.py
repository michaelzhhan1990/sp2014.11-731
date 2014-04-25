#!/usr/bin/env python
from __future__ import division
import argparse
import sys,math
import model_lr
import heapq
import copy
from collections import namedtuple

parser = argparse.ArgumentParser(description='Simple phrase based decoder.')
parser.add_argument('-i', '--input', dest='input', default='data/input2', help='File containing sentences to translate (default=data/input)')
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

def extract_english(states,result0):
        pre=states[result0[1]][result0][1]
        strr=states[result0[1]][result0][2]
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
    u={}   # langrange mutiplier
    times=0
    if len(f)<=10:
        times=10
    elif len(f)>10 and len(f)<20:
        times=20
    else:
        times=30



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
            #u[(lm.begin(),0,0,0,0)]=[]

            #for length in xrange(0,len(f)):

            #     check_times[0][(lm.begin(),0,0,0,0,'')].append(0)



        states[0][(lm.begin(),0,0,0,0)]=[0.0,None,'']
        begin=(lm.begin(),0,0,0,0)

        #for pp in p:
         #   if pp[0]<=5:

        for ss in xrange(1,6):   #reordering limits
            if ss in p:
                for t3 in p[ss]:
                    nn=t3-ss+1

                    for p_p in p[ss][t3]:
                        logprob=p_p[0]
                        sttr=p_p[1]


                        for e in sttr.split():
                            (lm_state,word_logprob)=lm.score(lm.begin(),e)
                            logprob+=word_logprob

                        logprob-=0.1*ss  #distortion penalty

                        for ite1 in xrange(ss,t3+1):
                            logprob+=u[ite1]

                        temp=(lm_state,nn,ss,t3,t3)

                        if temp not in states[nn] or states[nn][temp][0]<logprob:
                            states[nn][temp]=[logprob,begin,sttr]
                            #states[nn][temp].append(0)
                            #states[nn][temp].append(None)
                            #states[nn][temp][0]=logprob
                            #states[nn][temp][1]=begin

                            check_times[nn][temp]=copy.deepcopy(origin)
                            #for ite in xrange(0,len(f)):
                                #check_times[nn][temp].append(0)
                            for ite in xrange(ss,t3+1):
                                check_times[nn][temp][ite-1]+=1



        for i in xrange(1,len(f)):
            #print i
            n=0
            temp_states={}
            for st in states[i]:
                #if st[1]==i:   # topology

                     #x_new=[]
                     #for ii in xrange(0,len(f)):
                      #   x_new.append(check_times[i][st][ii])

                     #for pp in p:   # no penalty for reordering yet

                for ss in xrange(max(1,st[4]-5),st[4]+6):
                    if ss in p:
                        for t3 in p[ss]:
                            if t3<st[2] or ss>st[3]:
                                 n=st[1]+t3-ss+1
                                 distortion=abs(st[4]-t3+1)
                                 if distortion<=5  and n<=len(f):

                                     for p_p in p[ss][t3]:
                                         logprob=p_p[0]
                                         sttr=p_p[1]

                                         for e in sttr.split():
                                             (lm_state,word_logprob)=lm.score(st[0],e)
                                             logprob+=word_logprob

                                         for ite1 in xrange(ss,t3+1):
                                             logprob+=u[ite1]

                                         #n=st[1]+pp[1]-pp[0]+1
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
                                         if (tup not in states[n] and tup not in temp_states) or (tup not in states[n] and tup in temp_states and temp_states[tup][0]<logprob)  or (tup in states[n] and states[n][tup][0]<logprob and tup not in temp_states) or (tup in states[n] and states[n][tup][0] <logprob and tup in temp_states and temp_states[tup][0]<logprob):
                                            temp_states[tup]=[logprob,st,sttr]
                                            #temp_states[tup].append(0)
                                            #temp_states[tup].append(None)
                                            #temp_states[tup][0]=logprob
                                            #temp_states[tup][1]=st

                                            check_times[n][tup]=copy.deepcopy(check_times[i][st])
                                            for temp in xrange(ss,t3+1):
                                                check_times[n][tup][temp-1]+=1

                                            """
                                            y_new=[]
                                            for ii in xrange(0,len(f)):
                                                y_new.append(check_times[i][st][ii])
                                            for temp in xrange(pp[0],pp[1]+1):
                                                y_new[temp-1]+=1
                                            check_times[n][tup]=[]
                                            for iterator in y_new:
                                                check_times[n][tup].append(iterator)
                                            """



            for st in temp_states:

                states[st[1]][st]=temp_states[st]

        for ite1 in states[len(f)]:
            states[len(f)][ite1][0]+=lm.end(ite1[0])



        heap={}
        for st in states[len(f)]:
            #if st[1]==len(f):
            heap[st]=states[len(f)][st][0]
        winner=max(heap,key=heap.get)
        #print winner

        #print extract_english(states,winner)

        judge=False
        for iite in check_times[len(f)][winner]:
            if iite!=1:
                judge=True
                break

        if judge==False or tt==times:
            #result=winner
            break
        else:
            for ite in xrange(1,len(f)+1):
                if tt==0:
                    llambda=0

                else:
                    if heap[winner]>last_value:
                        llambda+=1

                    last_value=heap[winner]

                u[ite]=u[ite]-(check_times[len(f)][winner][ite-1]-1)*1/(1+llambda)

    stt=extract_english(states,winner)

    print stt





    # find best translation by looking at the best scoring hypothesis
    # on the last stack




    """
    def extract_english_recursive(h):
        return '' if h.predecessor is None else '%s%s ' % (extract_english_recursive(h.predecessor), h.phrase.english)
    print extract_english_recursive(winner)

    if opts.verbose:
        def extract_tm_logprob(h):
            return 0.0 if h.predecessor is None else h.phrase.logprob + extract_tm_logprob(h.predecessor)
        tm_logprob = extract_tm_logprob(winner)
        sys.stderr.write('LM = %f, TM = %f, Total = %f\n' %
            (winner.logprob - tm_logprob, tm_logprob, winner.logprob))
    """


__author__ = 'hanz'
