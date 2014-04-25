#!/usr/bin/env python
import argparse
import json
import os, sys, math

def extract_features_n(hyp, ref,n,box):




    hwords = hyp.lower()
    rwords = ref.lower()
    lamb=0.5

    #if len(hwords)<n or len(rwords)<n:
     #   return 0.000000000001

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

    while i<=n:

            #box.append((i,0.000000000001))


        if len(hwords)>=i and len(rwords)>=i:
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
    while i<=n:
        if len(hwords)>=i and len(rwords)>=i:
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

    i=3
    while i<=n:
        if len(hwords)>=i and len(rwords)>=i:
            s_index=1
            while s_index<=len(hwords):
                t_index=0
                while t_index<=len(rwords):
                    K[(i,hwords[:s_index],rwords[:t_index])]=K[(i,hwords[:s_index-1],rwords[:t_index])]+K2[(i,hwords[:s_index],rwords[:t_index])]
                    t_index+=1
                s_index+=1
            box.append((i,K[(i,hwords,rwords)]))

        else:
            box.append((i,0.000000000001))
        i+=1



    return 0



def all(hyp, ref):
     n=10

     features={}
     box_st=[]
     box_ss=[]
     box_tt=[]
     extract_features_n(hyp,ref,n,box_st)
     extract_features_n(hyp,hyp,n,box_ss)
     extract_features_n(ref,ref,n,box_tt)
     ite=0
     while ite <len(box_ss):
         name=str(box_ss[ite][0])+'-gram'
         features[name]=box_st[ite][1]/math.sqrt(box_ss[ite][1]*box_tt[ite][1])
         ite+=1



     return features

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

