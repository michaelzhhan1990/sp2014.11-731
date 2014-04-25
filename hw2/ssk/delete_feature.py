#!/usr/bin/env python
import argparse
import json
import os, sys, math

def delete_all():
    file0=file('features.txt','w+')
    for line in open('myfeatures.json'):

        s=line.split(',')
        print line
        ite=1
        temp='{'
        ii=1
        while ii<len(s[ite]) :
            temp+=s[ite][ii]
            ii+=1

        ite=2
        temp+=','

        while ite<len(s)-1:

            temp+=s[ite]
            temp+=','
            ite+=1


        for i in s[ite]:
            if i!='\n':
                temp+=i



        print >>file0, temp
    return 0

def only_3():
    file0=file('features.txt','w+')
    for line in open('myfeatures.json'):

        s=line.split(',')
        print line
        ite=2
        temp='{'
        ii=1
        while ii<len(s[ite]) :
            temp+=s[ite][ii]
            ii+=1

        temp+='}'
        print >> file0,temp

def only_4():
    file0=file('features.txt','w+')
    for line in open('myfeatures.json'):

        s=line.split(',')
        print line
        ite=1
        temp='{'
        ii=1
        while ii<len(s[ite]) :
            temp+=s[ite][ii]
            ii+=1

        temp+='}'
        print >> file0,temp


def only_5():
    file0=file('features.txt','w+')
    for line in open('myfeatures.json_origin'):

        s=line.split(',')
        print line
        ite=4
        temp='{'
        ii=1
        while ii<len(s[ite])-1 :
            temp+=s[ite][ii]
            ii+=1

        temp+='}'
        print >> file0,temp

def ssk_pre_recall():
    file0=file('features.txt','w+')
    ssk_3=[]
    for line in open('/features/features(3-10).json'):

        s=line.split(',')
        print line
        ite=1
        temp=''
        ii=1
        while ii<len(s[ite]) :
            temp+=s[ite][ii]
            ii+=1
        temp+=','
        #ite+=1
        ite=4
        while ite<len(s)-1:

            temp+=s[ite]
            #temp+=','
            ite+=1


        #for i in s[ite]:
         #   if i!='\n':
          #      temp+=i

        temp+='}'
        ssk_3.append(temp)
        #print >> file0,temp,

        ite=0
    for line in open('myfeatures.json'):
        temp=''

        for i in line:
            if i !='}':
                temp+=i
            else :
                break

        temp+=', '

        temp+=ssk_3[ite]
        print >>file0,temp
        ite+=1

def ssk_select():
    file0=file('features.txt','w+')
    ssk_3=[]
    for line in open('../features/features(3-10).txt'):

        s=line.split(',')
        print line
        ite=1
        temp=''
        ii=1
        while ii<len(s[ite]) :
            temp+=s[ite][ii]
            ii+=1
        temp+=','
        #ite+=1

        #temp+=s[1]+','
        temp+=s[4]+','
        temp+=s[5]
        #for tt in s[7]:
         #   if tt!='\n':
          #      temp+=tt


        temp+='}'
        ssk_3.append(temp)
        #print >> file0,temp,

        ite=0
    for line in open('../extract_py/new.txt'):
        temp=''

        for i in line:
            if i !='}':
                temp+=i
            else :
                break

        temp+=', '

        temp+=ssk_3[ite]
        print >>file0,temp
        ite+=1
    return 0



ssk_select()

