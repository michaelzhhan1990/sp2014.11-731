#!/usr/bin/env python
import argparse
import json
import os, sys, math

file0=file('data.txt','w+')
ite=1
for line in open('data/en-cs.pairs'):
   if ite>9999:
       print >>file0,line,
   ite+=1
