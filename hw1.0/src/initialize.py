from __future__ import division
__author__ = 'hanz'
#!/usr/bin/env python
# coding=utf-8
import sys

def uni_probability_initialize(t,count,total,box_f,box_e):



    parallel="/Users/hanz/sp2014.11-731/hw1/data/dev-test-train.de-en"
    align="/Users/hanz/sp2014.11-731/hw1/data/dev.align"
    line_num=0
    file=open(parallel)
    for line in file:
        little_boxf=[]  # one sentence
        little_boxe=[]

        s=line.split('|||')
        s[0]=s[0].strip().split(" ")
        s[1]=s[1].strip().split(" ")
        s[0].insert(0,' ')
        number=len(s[0])*len(s[1])
        for s0 in s[0]:
            if s0 not in total :
                total[s0]=0

            for s1 in s[1]:
                #count[(s1,s0)]=0
                if (s1,s0) in t:
                    t[(s1,s0)]+=1/number
                else:
                    t[(s1,s0)]=1/number

        for s0 in s[0]:
            little_boxf.append(s0)
        for s1 in s[1]:
            little_boxe.append(s1)


        line_num+=1
        box_f.append((little_boxf,len(s[0])))
        box_e.append((little_boxe,len(s[1])))

        if line_num==300:
            break


    for tem in t:
        count[tem]=0

    file.close()
    return 0








