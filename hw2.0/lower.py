#!/usr/bin/env python
import argparse
import json
import os, sys, math
file0=file('lower_data.txt','w+')
for line in open ('data/en-cs.pairs'):

    print >>file0,line.lower(),