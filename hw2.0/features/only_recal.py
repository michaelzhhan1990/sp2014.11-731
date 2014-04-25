#!/usr/bin/env python
import argparse
import json
import os, sys, math

file0=file('new_features.txt','w+')
box0=[]
box1=[]
box2=[]
box3=[]
box4=[]
box5=[]
box6=[]
box7=[]
for line in open('features(3-10).txt'):
    s=line.split(',')
    print s[0]
    s[1]=s[1][1:len(s[1])]
    print s[1]
    s[2]=s[2][1:len(s[2])]
    print s[2]
    s[3]=s[3][1:len(s[3])]
    print s[3]
    s[4]=s[4][1:len(s[4])]
    print s[4]
    s[5]=s[5][1:len(s[5])]
    print s[5]
    s[6]=s[6][1:len(s[6])]
    print s[6]
    s[7]=s[7][1:len(s[7])-2]
    print s[7]

    #break
    box0.append(s[0])
    box1.append(s[1])
    box2.append(s[2])
    box3.append(s[3])
    box4.append(s[4])
    box5.append(s[5])
    box6.append(s[6])
    box7.append(s[7])


ite=0
for line in open('features(r,p,meteor,3,6,7).txt'):

       s=line.split(',')
       temp=s[0]+', '+box7[ite][0:len(box7[ite])]+'}'
       print >>file0,temp
       ite+=1

