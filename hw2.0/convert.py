#!/usr/bin/env python
import argparse
import json
import os, sys, math

file0=file('data.txt','w+')
ite=1
for line in open('en-cs.pairs'):
    if ite>=10000:
        
        temp=''
        for i in line:
            if i !='\n':
               temp+=i
                
                
        print >>file0,temp
    ite+=1
