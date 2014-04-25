from __future__ import division
__author__ = 'hanz'
#!/usr/bin/env python
# coding=utf-8
import sys
from EM_IBM1 import *
from hmm_initialize import *

def EM_HMM(a,t,count,total,total_a,box_f,box_e):
    hmm_initialize(a,total_a,box_e)
    ite=0
    count_a={}

    while ite<6:
        #set all count and total to 0
        for tt in total:
            total[tt]=0
        for cc in count:
            count[cc]=0
        for aa in a:
            count_a[aa]=0
        for tta in total_a:
            total_a[tta]=0

        line=0
        while line < len(box_f):
            ssf=box_f[line][0]
            sse=box_e[line][0]
            lf=box_f[line][1]-1
            le=box_e[line][1]
            s_total={}
            j=0

            while j<=lf:
                s_total[ssf[j]]=0
                i=1
                while i<=le:
                    ii=1
                    while ii<=le:
                        s_total[ssf[j]]+=t[(ssf[j],sse[i-1])]*a[(i,ii,le)]
                        ii+=1
                    i+=1
                j+=1

            j=0

            while j<=lf:
                i=1
                while i<=le:
                    ii=1
                    while ii<=le:
                        c=t[(ssf[j],sse[i-1])]*a[(i,ii,le)]/s_total[ssf[j]]
                        count[(ssf[j],sse[i-1])]+=c
                        total[sse[i-1]]+=c
                        count_a[(i,ii,le)]+=c
                        total_a[(ii,le)]+=c
                        ii+=1
                    i+=1
                j+=1

            line+=1
        for tt in t:
            t[tt]=0
        for aa in a:
            a[aa]=0
        for tt in t:
            t[tt]=count[(tt[0],tt[1])]/total[tt[1]]
        for aa in a:
            a[aa]=count_a[aa]/total_a[(aa[1],aa[2])]


        ite+=1
    return 0
