from __future__ import division
__author__ = 'hanz'
#!/usr/bin/env python
# coding=utf-8
import sys


def hmm_initialize(a,total_a,box_e):
    ite=0
    while ite<len(box_e):

        le=box_e[ite][1]
        if(1,1,le) not in a:
            i=1
            while i<=le:
                ii=1
                while ii<=le:
                    a[(i,ii,le)]=1/(le)
                    ii+=1
                i+=1
        if (1,le) not in total_a:
            ii=1
            while ii<=le:
                total_a[(ii,le)]=0
                ii+=1

        ite+=1
    return 0