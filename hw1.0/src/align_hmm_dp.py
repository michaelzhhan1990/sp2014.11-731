from __future__ import division
__author__ = 'hanz'
#!/usr/bin/env python
# coding=utf-8
import sys

def align(a,t,box_f,box_e):
    file0=file('output.txt','w+')
    line=0
    while line<len(box_f):
        ssf=box_f[line][0]
        sse=box_e[line][0]
        lf=box_f[line][1]-1
        le=box_e[line][1]


        index_f=1
        max=0
        index_e=0
        while index_e<le:
            if t[(ssf[index_f],sse[max])] <t[(ssf[index_f],sse[index_e])]:
                max=index_e
            index_e+=1

        aa={}
        # aa is the optimal alignment
        aa[1]=max+1

        index_f=2

        print >> file0,'0'+'-'+str(max),
        while index_f<=lf:
            max=0
            index_e=0
            while index_e<le:
                if (t[(ssf[index_f],sse[max])]*a[(max+1,aa[index_f-1],le)]) <(t[(ssf[index_f],sse[index_e])]*a[(index_e+1,aa[index_f-1],le)]):
                    max=index_e
                index_e+=1
            aa[index_f]=max+1

            print >>file0,str(index_f-1)+'-'+str(max),

            index_f+=1
        print >> file0

        line+=1






    return 0