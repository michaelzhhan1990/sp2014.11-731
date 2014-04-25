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

for line in open('features.txt'):
    s=line.split(',')

    print s[0]
    s[1]=s[1][1:len(s[1])]
    print s[1]
    s[2]=s[2][1:len(s[2])]
    print s[2]
    s[3]=s[3][1:len(s[3])]
    print s[3]
    s[4]=s[4][1:len(s[4])]
    s[4]=s[4].split(':')
    print s[4]
    num1=s[4][1][1:len(s[4][1])]
    print num1
    num1=float(num1)
    print num1
    s[4][1]=num1*2
    s[5]=s[5][1:len(s[5])]
    s[5]=s[5].split(':')

    num2=s[5][1][1:len(s[5][1])]
    num2=float(num2)
    print s[5]
    print num2

    s[6]=s[6][1:len(s[6])-2]
    s[6]=s[6].split(':')

    num3=s[6][1][1:len(s[6][1])]
    num3=float(num3)
    print s[5]
    print num3

    print s[6]

    s[4][0]+=': '
    s[5][0]+=': '
    s[6][0]+=': '
    s[5][1]=num2
    s[6][1]=num3*2

    #break
    box0.append(s[0])
    box1.append(s[1])
    box2.append(s[2])
    box3.append(s[3])
    box4.append(s[4])
    box5.append(s[5])
    box6.append(s[6])

ite=0
for line in open ('new.txt'):
    temp=''
    for i in line:
        if i !='}' and i!='\n':
            temp+=i

    temp+=', '+box4[ite][0]+str(box4[ite][1])+', '+box5[ite][0]+str(box5[ite][1])+', '+box6[ite][0]+str(box6[ite][1])+'}'
    print >> file0,temp
    ite+=1








