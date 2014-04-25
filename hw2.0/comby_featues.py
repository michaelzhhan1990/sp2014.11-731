#!/usr/bin/env python
import argparse
import json
import os, sys, math

file0=file('new_features','w+')
box=[]
#for line in open('features/features(r,p,meteor,3,6,7).txt'):
for line in open('extract_py/new.txt'):
    temp=''
    for i in line:
        if i!='}' and i!='\n':
            temp+=i
    temp+=', '
    box.append(temp)
    #print temp
it=0
for line in open('n-gram/prob.txt'):

    temp='"'+line[2:9]+'": '
    ite=12
    while line[ite]!='\n':
        temp+=line[ite]
        ite+=1
    str=box[it]+temp
    #print str
    #print box[it]

    print>>file0,str
    it+=1








