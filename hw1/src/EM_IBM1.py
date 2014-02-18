from __future__ import division
__author__ = 'hanz'
#!/usr/bin/env python
# coding=utf-8
import sys
from initialize import *
def EM_IBM1(t, count, total,box_f,box_e) :
    uni_probability_initialize(t,count,total,box_f,box_e)
    number=0
    s_total={}
    ite=0


    while ite < 6:

        for sym in count:
            count[sym]=0
        for sy in total:
            total[sy]=0

        line=0
        while line < len(box_f):
            sse=box_e[line]
            ssf=box_f[line]
            for s1 in sse[0]:
                s_total[s1]=0
                for s0 in ssf[0]:
                    s_total[s1]+=t[(s1,s0)]

            for s1 in sse[0]:
                for s0 in ssf[0]:
                    count[(s1,s0)]+=t[(s1,s0)]/s_total[s1]
                    total[s0]+=t[(s1,s0)]/s_total[s1]

            line+=1
            if line==300:
                break



        for tem in t:
            t[tem]=count[tem]/total[tem[1]]
        ite+=1


    return 0




    """
        for sf in store_f:
            for se in store_e:
                if(se,sf) in t:
                    t[(se,sf)]=count[(se,sf)]/total[sf]
    """