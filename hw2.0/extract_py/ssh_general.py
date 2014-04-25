#!/usr/bin/env python
import argparse
import json
import os, sys, math

def extract_features_2(hyp, ref):
    hwords = hyp.lower()
    rwords = ref.lower()
    lamb=0.5

    K={}
    K1={}
    K2={}
    K1[(0,'','')]=1
    K1[(1,'','')]=0
    K1[(2,'','')]=0
    K[(1,'','')]=0
    K[(2,'','')]=0
    K2[(1,'','')]=0


    i=0

    while i<=2:
        s_index=0
        while s_index<=len(hwords):
            t_index=0
            while t_index<=len(rwords):
                if min(s_index,t_index)<i:
                    K[(i,hwords[:s_index],rwords[:t_index])]=0
                    K1[(i,hwords[:s_index],rwords[:t_index])]=0

                if s_index==0 or t_index==0:
                    K2[(i,hwords[:s_index],rwords[:t_index])]=0


                K1[(0,hwords[:s_index],rwords[:t_index])]=1
                t_index+=1
            s_index+=1
        i+=1





    """
    s_index=1
    while s_index<=len(hwords):
        t_index=1
        while t_index<=len(rwords):
            K2[(1,hwords[:s_index],rwords[:t_index])]=KK[(1,hwords[:s_index],rwords[:t_index])]-lamb*KK[(1,hwords[:s_index-1],rwords[:t_index])]
            t_index+=1
        s_index+=1
    """


    #o(n|s||t|)one
    i=1
    while i<=2:
        s_index=1
        while s_index<=len(hwords):
            t_index=1
            while t_index<=len(rwords):
                if hwords[s_index-1]==rwords[t_index-1]:
                    K2[(i,hwords[:s_index],rwords[:t_index])]=lamb*(K2[(i,hwords[:s_index],rwords[:t_index-1])]+lamb*K1[(i-1,hwords[:s_index-1],rwords[:t_index-1])])
                else :
                    K2[(i,hwords[:s_index],rwords[:t_index])]=lamb*K2[(i,hwords[:s_index],rwords[:t_index-1])]

                K1[(i,hwords[:s_index],rwords[:t_index-1])]=lamb*K1[(i,hwords[:s_index-1],rwords[:t_index-1])]+K2[(i,hwords[:s_index],rwords[:t_index-1])]
                t_index+=1
            s_index+=1
        i+=1

    s_index=1
    while s_index<=len(hwords):
        t_index=0
        while t_index<=len(rwords):
            K[(2,hwords[:s_index],rwords[:t_index])]=K[(2,hwords[:s_index-1],rwords[:t_index])]+K2[(2,hwords[:s_index],rwords[:t_index])]
            t_index+=1
        s_index+=1



    return K[(2,hwords,rwords)]



def all(hyp, ref):
    st=extract_features_2(hyp,ref)
    ss=extract_features_2(hyp,hyp)
    tt=extract_features_2(ref,ref)
    return {'2-gram':st/math.sqrt(ss*tt)}


argparser = argparse.ArgumentParser(prog='extract')
argparser.add_argument('-x', '--pairs', dest='pairs', default='data/en-cs.pairs', help='Reference-Hypothesis pairs')
args = argparser.parse_args()

lc = 0
sys.stderr.write('Extracting features for (ref,hyp) pairs from %s.\n' % args.pairs)
# loop over all (ref,hyp) pairs in the input file and extract evaluation features
for ref_hyp in open(args.pairs):
    lc += 1
    ref, hyp = ref_hyp.rstrip().split(' ||| ')
    fmap = all(hyp, ref)
    print json.dumps(fmap)   # print evaluation feature map





