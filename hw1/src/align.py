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

        while index_f<=lf:
            max=0
            index_e=0
            while index_e<le:
                if (t[(sse[max],ssf[index_f])]*a[(index_f,max+1,le,lf)]) <(t[(sse[index_e],ssf[index_f])]*a[(index_f,index_e+1,le,lf)]):
                    max=index_e
                index_e+=1

            print >> file0,str(index_f-1)+'-'+str(max),

            index_f+=1
        print >>file0
        line+=1






    return 0