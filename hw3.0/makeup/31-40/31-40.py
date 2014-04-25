#!/usr/bin/env python
import sys

fill=[0,0,0,0,0,0,0,0,0,0]

fill[0]=file('input_sent0','w+')
fill[1]=file('input_sent1','w+')
fill[2]=file('input_sent2','w+')
fill[3]=file('input_sent3','w+')
fill[4]=file('input_sent4','w+')
fill[5]=file('input_sent5','w+')
fill[6]=file('input_sent6','w+')
fill[7]=file('input_sent7','w+')
fill[8]=file('input_sent8','w+')
fill[9]=file('input_sent9','w+')

ite=0
for line in open('../../data/input3'):
    print >>fill[ite],line,
    ite+=1



fill[0]=file('base0','w+')
fill[1]=file('base1','w+')
fill[2]=file('base2','w+')
fill[3]=file('base3','w+')
fill[4]=file('base4','w+')
fill[5]=file('base5','w+')
fill[6]=file('base6','w+')
fill[7]=file('base7','w+')
fill[8]=file('base8','w+')
fill[9]=file('base9','w+')

ite=0
for line in open('../output.txt'):
    if ite>=30 and ite <40:
        print >>fill[ite-30],line,
    ite+=1

fill[0]=file('resul0','w+')
fill[1]=file('resul1','w+')
fill[2]=file('resul2','w+')
fill[3]=file('resul3','w+')
fill[4]=file('resul4','w+')
fill[5]=file('resul5','w+')
fill[6]=file('resul6','w+')
fill[7]=file('resul7','w+')
fill[8]=file('resul8','w+')
fill[9]=file('resul9','w+')

"""
ite=0
for line in open('result'):
    #if ite>=20 and ite <30:
    print >>fill[ite],line,
    ite+=1
"""