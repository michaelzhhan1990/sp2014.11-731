#!/usr/bin/env python
import argparse
import json
import os, sys, math

file0=file('features.txt','w+')
for line in open('myfeatures.json0'):
    ite=0
    temp=''
    while ite<len(line)-1:
        temp+=line[ite]
        ite+=1
    st='{"2-gram": '+temp+'}'
    print >>file0,st
