#!/usr/bin/env python
from __future__ import division
import argparse
import sys,math
import models
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

tm = models.TM(opts.tm, sys.maxint)
lm = models.LM(opts.lm)
sys.stderr.write('Decoding %s...\n' % (opts.input,))
input_sents = [tuple(line.strip().split()) for line in open(opts.input).readlines()[:opts.num_sents]]

def extract_english(states,result0):
        pre=states[result0[1]][result0][1]
        strr=states[result0[1]][result0][2]
        return '' if pre is None else '%s%s ' % (extract_english(states,pre),strr )


#file0=file('result00','w+')
for line in open('a2_base'):
    tune_base=line.split(' ')
    break


tune_num=0


for f in input_sents:
    # The following code implements a DP monotone decoding
    # algorithm (one that doesn't permute the target phrases).
    # Hence all hypotheses in stacks[i] represent translations of
    # the first i words of the input sentence.
    # HINT: Generalize this so that stacks[i] contains translations
    # of any i words (remember to keep track of which words those
    # are, and to estimate future costs)
        p={}   # edge
    
        base=tune_base[tune_num]

        length=len(f)

        origin=''
        for ite in xrange(0,length):
                origin+='0'



        # get all possible edge from input
        for i in xrange(0,length):
                p[i+1]={}
                for j in xrange(i+1,length+1):
                    p[i+1][j]=[]
                    if f[i:j] in tm:
                        #p[i+1]=(j,tm[f[i:j]])    # p[i+1][j]=[(prob,english),(prob,english)]
                        for e in tm[f[i:j]]:
                            p[i+1][j].append((e.logprob,e.english))

                            #p[i+1][j].append(e)




    
        states=[]
        

        for ite in xrange(0,length+1):
                states.append({})



        b=origin

        states[0][(lm.begin(),0,0,0,0,b)]=[0.0,None,'']
        begin=(lm.begin(),0,0,0,0,b)

        

        for ss in xrange(1,6):   #reordering limits
            if ss in p:
                for t3 in p[ss]:
                    nn=t3-ss+1
                    #lagrange=0
                    check_temp=''
                    for ite in xrange(1,length+1):
                        if ite >= ss and ite <=t3   :
                                st_num=str(int(origin[ite-1])+1)
                                check_temp+=st_num
                        else:
                            check_temp+='0'


                    #for ite1 in xrange(ss,t3+1):
                     #       lagrange+=u[ite1]

                    for p_p in p[ss][t3]:
                        logprob=p_p[0]
                        sttr=p_p[1]


                        for e in sttr.split():
                            (lm_state,word_logprob)=lm.score(lm.begin(),e)
                            logprob+=word_logprob



                        temp=(lm_state,nn,ss,t3,t3,check_temp)

                        if temp not in states[nn] or states[nn][temp][0]<logprob and logprob>=base:
                            states[nn][temp]=[logprob,begin,sttr]
                            

                    check_temp=''




        for i in xrange(1,length):
            #print i
            n=0

            for st in states[i]:
                for ss in xrange(max(1,st[4]-4),st[4]+6):
                    if ss in p:
                        for t3 in p[ss]:
                            if t3<st[2] or ss>st[3]:
                                 n=st[1]+t3-ss+1
                                 distortion=abs(st[4]-t3+1)
                                 if distortion<=5  and n<=length:
                                     #lagrange=0
                                     #for ite1 in xrange(ss,t3+1):
                                            # lagrange+=u[ite1]
                                     jj=False

                                     check_temp=''
                                     last=st[5]
                                     check_temp=last[0:ss-1]


                                     for temp in xrange(ss,t3+1):
                                        linshi=int(last[ite-1])+1
                                        if linshi <=1:
                                            st_num=str(linshi)
                                            check_temp+=st_num

                                        else:
                                            jj=True
                                            break

                                     check_temp+=last[t3:length]

                                     if jj==True:
                                         break

                                     for p_p in p[ss][t3]:
                                         logprob=p_p[0]
                                         sttr=p_p[1]
                                         #logprob+=lagrange
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
                                         #logprob-=0.1*distortion

                                         tup=(lm_state,n,l,m,r,check_temp)
                                         if tup not in states[n] or states[n][tup][0]<logprob and logprob >=base:
                                            states[n][tup]=[logprob,st,sttr]
                                            #check_times[n][tup]=copy.deepcopy(check_temp)
                                     check_temp=''







        for ite1 in states[len(f)]:
            states[len(f)][ite1][0]+=lm.end(ite1[0])



        heap={}
        if states[len(f)]!={}:
            for st in states[len(f)]:

                heap[st]=states[len(f)][st][0]
            winner=max(heap,key=heap.get)
            #print winner

            stt=extract_english(states,winner)

            print stt
        
        else:
            print 'none big'
            
        tune_num+=1











__author__ = 'hanz'
