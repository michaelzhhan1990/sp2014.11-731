from __future__ import division
__author__ = 'hanz'
#!/usr/bin/env python
# coding=utf-8
import sys


def ibm2_initialize(a,total_a,box_f,box_e):
    ite=0
    while ite<len(box_f):
        lf=box_f[ite][1]-1
        le=box_e[ite][1]
        if(0,1,le,lf) not in a:
            i=0
            while i<=lf:
                j=1
                while j<=le:
                    a[(i,j,le,lf)]=1/(lf+1)
                    j+=1
                i+=1
        if (1,le,lf) not in total_a:
            j=1
            while j<=le:
                total_a[(j,le,lf)]=0
                j+=1

        ite+=1
    return 0