#!/usr/bin/env python
import argparse
import json
import os, sys, math

file0=file('prob.txt','w+')
argparser = argparse.ArgumentParser(prog='extract')
argparser.add_argument('-x', '--pairs', dest='pairs', default='data/en-cs.pairs', help='Reference-Hypothesis pairs')
args = argparser.parse_args()

lc = 0
sys.stderr.write('Extracting features for (ref,hyp) pairs from %s.\n' % args.pairs)
# loop over all (ref,hyp) pairs in the input file and extract evaluation features
box=[]
ite=1
trigrm=200000
judge=False
box={}
ite=1
for line in open('3.arpa'):
    if ite >=10 and ite<=14656:
        s=''
        for i in line:
            if i!='\n':
                s+=i

        s=s.rsplit();
        if len(s)==3:
            box[s[1]]=s[0]



    elif ite>=14658 and ite<=45601:
      s=''
      for i in line:
          if i!='\n':
              s+=i

      s=s.rsplit()
      if len(s)==3:
        box[(s[1],s[2])]=s[0]

    elif ite>=45604 and ite<=78156:
      s=''
      for i in line:
          if i!='\n':
              s+=i

      s=s.rsplit()
      if len(s)==4:
        box[(s[1],s[2],s[3])]=s[0]

    elif ite==78157:
          break

    ite+=1





for ref_hyp in open(args.pairs):
    lc += 1
    ref, hyp = ref_hyp.rstrip().split(' ||| ')
    #print hyp
    h=hyp.rsplit()
    #print h
    sum3=0
    oov=-0.36687523
    index=0
    print h
    if len(h)>=3:
        index=2
        while index<len(h):

            if (h[index-2],h[index-1],h[index])not in box:
                temp3=3*oov
            else :
                temp3=float(box[(h[index-2],h[index-1],h[index])])
            if (h[index-1],h[index])not in box:
                temp2=2*oov
            else :
                temp2=float(box[(h[index-1],h[index])])
            if h[index] not in box:
                temp1=oov
            else:
                temp1=float(box[h[index]])
            sum3+=0.5*sum3+0.3*temp2+0.2*temp1
            index+=1
    elif len(h)==2:
        if (h[0],h[1])not in box:
            temp2=2*oov
        else:
            temp2=float(box[(h[0],h[1])])
        if h[1] not in box:
            temp1=oov
        else:
            temp1=float(box[h[1]])
        sum3=0.6*temp2+0.5*temp1
    elif len(h)==1:
        if h[0] not in box:
            sum3=oov
        else:
            sum3=float(box[h[0]])

    k={"3-grams":10**((sum3))/len(h)}


    print >>file0,k