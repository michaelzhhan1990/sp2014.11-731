#!/usr/bin/env python
import argparse
import json
import os, sys, math

def extract_features_2(hyp, ref):
    hwords = hyp.lower()
    rwords = ref.lower()
    #refset = set(rwords)
    u=set()
    lamb=0.5

    i=0

    while i<len(hwords)-1:
        j=i+1
        while j<len(hwords):
            word=hwords[i]+hwords[j]
            u.add(word)
            j+=1
        i+=1
    K={}
    KK={}
    K2={}
    KK[(0,'','')]=1
    KK[(1,'','')]=0
    KK[(2,'','')]=0
    K[(1,'','')]=0
    K[(2,'','')]=0
    K2[(1,'','')]=0

    """
    s_index=1
    while s_index<=len(hwords):
        t_index=1
        while t_index<=len(rwords):
            Sum=0
            j=1
            while j<len(rwords):
                if rwords[j-1]==hwords[s_index-1]:
                    Sum+=lamb**(len(rwords)-j+2)
                j+=1
            K2[(1,hwords[:s_index],rwords[:t_index])]=Sum
            t_index+=1
        s_index+=1
    """




    i=1
    while i<=len(hwords):
        j=1
        while j<=len(rwords):
            KK[(0,hwords[:i],rwords[:j])]=1
            j+=1
        i+=1


    i=1
    while i<=len(hwords):
        KK[(0,hwords[:i],'')]=1
        KK[(1,hwords[:i],'')]=0
        KK[(2,hwords[:i],'')]=0
        K[(1,hwords[:i],'')]=0
        K[(2,hwords[:i],'')]=0
        K2[(1,hwords[:i],'')]=0

        i+=1

    j=1
    while j<=len(rwords):
        KK[(0,'',rwords[:j])]=1
        KK[(1,'',rwords[:j])]=0
        KK[(2,'',rwords[:j])]=0
        K[(1,'',rwords[:j])]=0
        K[(2,'',rwords[:j])]=0

        j+=1
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
    while i<2:
        s_index=1
        while s_index<=len(hwords):
            t_index=1
            while t_index<=len(rwords):
                if hwords[s_index-1]==rwords[t_index-1]:
                    K2[(i,hwords[:s_index],rwords[:t_index])]=lamb*(K2[(i,hwords[:s_index],rwords[:t_index-1])]+lamb*KK[(i-1,hwords[:s_index-1],rwords[:t_index-1])])
                else :
                    K2[(i,hwords[:s_index],rwords[:t_index])]=lamb*K2[(i,hwords[:s_index],rwords[:t_index-1])]

                KK[(i,hwords[:s_index],rwords[:t_index-1])]=lamb*KK[(i,hwords[:s_index-1],rwords[:t_index-1])]+K2[(i,hwords[:s_index],rwords[:t_index-1])]
                t_index+=1
            s_index+=1
        i+=1

    s_index=1
    while s_index<=len(hwords):
        t_index=1
        while t_index<=len(rwords):
            K[(2,hwords[:s_index],rwords[:t_index])]=K[(2,hwords[:s_index-1],rwords[:t_index])]+K2[(2,hwords[:s_index],rwords[:t_index])]
            t_index+=1
        s_index+=1

    k=K[(2,hwords,rwords)]/math.sqrt(K[(2,hwords,hwords)]*K[(2,rwords,rwords)])

    return {'2-gram':k}






argparser = argparse.ArgumentParser(prog='extract')
argparser.add_argument('-x', '--pairs', dest='pairs', default='data/en-cs.pairs', help='Reference-Hypothesis pairs')
args = argparser.parse_args()

lc = 0
sys.stderr.write('Extracting features for (ref,hyp) pairs from %s.\n' % args.pairs)
# loop over all (ref,hyp) pairs in the input file and extract evaluation features
for ref_hyp in open(args.pairs):
    lc += 1
    ref, hyp = ref_hyp.rstrip().split(' ||| ')
    fmap = extract_features_2(hyp, ref)
    print json.dumps(fmap)   # print evaluation feature map



  #Sum=0
            #j=1
            #while j<=t_index:
             #   if rwords[j-1]==hwords[s_index-1]:
              #      Sum+=KK[(1,hwords[:s_index-1],rwords[:j-1])]*lamb*lamb
               # j+=1



        #O(n|s||t|^2) one
    """
    i=1
    while i<2:
        s_index=1
        while s_index<=len(hwords):
            t_index=1
            while t_index<=len(rwords):
                Sum=0
                j=1
                while j<=len(rwords):
                    if rwords[j-1]==hwords[s_index-1]:
                        Sum+=KK[(i-1,hwords[:s_index-1],rwords[:j-1])]*lamb**(len(rwords)-j+2)
                    j+=1

                KK[(i,hwords[:s_index],rwords[:t_index])]=lamb*KK[(i,hwords[:s_index-1],rwords[:t_index])]+Sum
                t_index+=1



            s_index+=1
        i+=1

    """