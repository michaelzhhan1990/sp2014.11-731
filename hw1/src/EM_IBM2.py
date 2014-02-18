from __future__ import division
__author__ = 'hanz'
#!/usr/bin/env python
# coding=utf-8
import sys
from EM_IBM1 import *
from ibm2_initialize import *
def EM_IBM2(a,t,count,total,total_a,box_f,box_e):
    ibm2_initialize(a,total_a,box_f,box_e)
    ite=0
    count_a={}

    while ite<10:
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
            j=1

            while j<=le:
                s_total[sse[j-1]]=0
                i=0
                while i<=lf:
                    s_total[sse[j-1]]+=t[(sse[j-1],ssf[i])]*a[(i,j,le,lf)]
                    i+=1
                j+=1

            j=1

            while j<=le:
                i=0
                while i<=lf:
                    c=t[(sse[j-1],ssf[i])]*a[(i,j,le,lf)]/s_total[sse[j-1]]
                    count[(sse[j-1],ssf[i])]+=c
                    total[ssf[i]]+=c
                    count_a[(i,j,le,lf)]+=c
                    total_a[(j,le,lf)]+=c
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
            a[aa]=count_a[aa]/total_a[(aa[1],aa[2],aa[3])]


        ite+=1
    return 0
