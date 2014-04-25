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
    oov=-0.37991187
    index=0
    while index<len(h)-2:
        if (h[index],h[index+1],h[index+2]) in box:
            sum3+=0.5*float(box[(h[index],h[index+1],h[index+2])])

        elif (h[index],h[index+1]) in box:
            sum3+=0.3*float(box[(h[index],h[index+1])])

        elif h[index] in box:
            sum3+=0.2*float(box[h[index]])
        index+=1

    print len(h)
    print index
    print index+1

    if len(h)>=3 and(h[index],h[index+1])in box:
        sum3+=0.3*float(box[(h[index],h[index+1])])
    elif len(h)>=3 and h[index] in box and h[index+1] in box :
        sum3+=0.2*float(box[h[index]])+0.2*float(box[h[index+1]])
    elif len(h)>=3 and h[index] in box:
        sum3+=0.2*(float(box[h[index]])+oov)
    elif len(h)>=3 and h[index+1] in box:
        sum3+=0.2*(float(box[h[index+1]])+oov)
    elif len(h)>=3 :
        sum3+=0.4*oov
    elif len(h)==2:
        if (h[0],h[1]) in box:
            sum+=0.3*float(box[(h[0],h[1])])
        elif h[0] in box and h[1] in box :
            sum3+=0.2*float(box[h[0]])+0.2*float(box[h[1]])
        elif h[0] in box:
            sum3+=0.2*float(box[h[0]])+0.2*oov
        elif h[1] in box:
            sum3+=0.2*float(box[h[1]])+0.2*oov
        elif h[0] not in box and h[1] not in box:
            sum3+=0.4*oov

    index=0
    sum2=0
    while index<len(h)-2:
        if (h[index],h[index+1]) in box:
            sum2+=float(box[(h[index],h[index+1])])
        else:
            sum2+=oov
        index+=1
    index=0
    sum1=0
    while index<len(h):
        if h[index] in box:
            sum1+=float(box[h[index]])
        else:
            sum1+=oov
        index+=1

    k={"3-grams":10**((0.2*sum1+0.3*sum2+0.5*sum3)/len(h))}
    #k={"3-grams":10**(sum3)}

    print >>file0,k

    #0.2*sum1