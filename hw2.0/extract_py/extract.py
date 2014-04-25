#!/usr/bin/env python
import argparse
import json
import os, sys, math


def extract_features(hyp, ref):
    hwords = hyp.lower().split()
    rwords = ref.lower().split()
    refset = set(rwords)
    precision = sum(1.0 for word in hwords if word in refset) / len(hwords)
    recall=sum(1.0 for word in hwords if word in refset) / len(rwords)

    hw_trun=[]
    rw_trun=[]
    for hw in hwords:
        num=0
        temp=''
        for i in hw:
            if num <6 and num<len(hw):
                temp+=i
                num+=1
            else :
                break
        hw_trun.append(temp)

    for rw in rwords:
        num=0
        temp=''
        for i in rw:
            if num <6 and num<len(rw):
                temp+=i
                num+=1
            else :
                break
        rw_trun.append(temp)

    refset1=set(rw_trun)

    prec_trun=sum(1.0 for word in hw_trun if word in refset1) / len(hw_trun)
    recall_trun=sum(1.0 for word in hw_trun if word in refset1) / len(rwords)
    #print refset1
    #print hw_trun




    #return {'tune':4*precision*recall*prec_trun*recall_trun/(precision*recall*prec_trun+precision*recall*recall_trun+recall*recall_trun*prec_trun+precision*prec_trun*recall_trun)}
    #return {'recall':recall_trun}
    #return {'prec':precision,'recall':recall,'trun_r':recall_trun,'trun_p':prec_trun}
    return {'recall':recall}

argparser = argparse.ArgumentParser(prog='extract')
argparser.add_argument('-x', '--pairs', dest='pairs', default='../data/en-cs.pairs', help='Reference-Hypothesis pairs')
args = argparser.parse_args()

lc = 0
sys.stderr.write('Extracting features for (ref,hyp) pairs from %s.\n' % args.pairs)
# loop over all (ref,hyp) pairs in the input file and extract evaluation features
for ref_hyp in open(args.pairs):
    lc += 1
    ref, hyp = ref_hyp.rstrip().split(' ||| ')
    fmap = extract_features(hyp, ref)
    print json.dumps(fmap)   # print evaluation feature map
