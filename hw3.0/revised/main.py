#!/usr/bin/env python
from __future__ import division
import argparse
import sys,math
import models
import copy
import heapq
from collections import namedtuple
from initializer import  *
from generate_states import *

def extract_english(states,result0):
        pre=states[result0[0]][result0][1]
        strr=states[result0[0]][result0][2]
        return '' if pre is None else '%s%s ' % (extract_english(states,pre),strr )



parser = argparse.ArgumentParser(description='Simple phrase based decoder.')
parser.add_argument('-i', '--input', dest='input', default='data/test', help='File containing sentences to translate (default=data/input)')
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

times=50
for f in input_sents:
    length=len(f)
    p={}
    origin={}
    u={}
    initializer(f,p,u,origin,tm)

    last_value=0
    llambda=0

    for time in xrange(0,times):
        final_dic={}
        states_prob={}
        check_times={}

        states=[]
        for ite in xrange(0,length+1):
            states_prob[ite]={}
            check_times[ite]={}

        begin=(0,0,0,0,lm.begin())
        states_prob[0][begin]=[0.0,None,'']
        check_times[0][begin]=copy.deepcopy(origin)
        heapq.heappush(states,begin)
        while states!=[]:
            st=heapq.heappop(states)
            generate_states(st,states,states_prob,check_times,p,origin,length,u,lm,final_dic)

        winner=max(final_dic,key=final_dic.get)
        print winner
        print extract_english(states_prob,winner)
        judge=False
        dic =check_times[length][winner]
        for ite in xrange(1,length+1):
            if dic[ite]!=1:
                judge=True
                break

        if judge==False or time ==50:
            break
        else:
            for ite in xrange(1,length+1):
                if time==0:
                    llambda=0

                else:
                    if final_dic[winner]>last_value:
                        llambda+=1

                    last_value=final_dic[winner]

                u[ite]=u[ite]-(check_times[length][winner][ite]-1)*1/(1+llambda)

    result=extract_english(states_prob,winner)
    print result








        














__author__ = 'hanz'
