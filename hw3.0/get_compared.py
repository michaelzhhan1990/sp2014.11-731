#!/usr/bin/env python
import sys
bad_sens=[0,3,4,5]

file0=file('data/version1_partial_data/result4_good.txt','w+')
ite=0
for line in open('result4'):
    if ite not in bad_sens:
        print>> file0, line,
    ite+=1


file1=file('data/version1_partial_data/cp4_good.txt','w+')
ite=0
for line in open('data/output_base_4.txt'):
    if ite not in bad_sens:
        print>> file1, line,
    ite+=1





__author__ = 'hanz'
