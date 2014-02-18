from __future__ import division
__author__ = 'hanz'
#!/usr/bin/env python
# coding=utf-8
import sys
from initialize import *
from EM_IBM1 import *
from ibm2_initialize import *
from EM_IBM2 import *
from align import *

t={}
total={}
count={}
box_f=[]
box_e=[]
EM_IBM1(t,count,total,box_f,box_e)
a={}
total_a={}
EM_IBM2(a,t,count,total,total_a,box_f,box_e)
align(a,t,box_f,box_e)




