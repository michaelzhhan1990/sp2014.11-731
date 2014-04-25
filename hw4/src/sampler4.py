import sys
from g import *
from x import *


def sample():
    file1=file('sample4','w+')
    sampler=[]
    for i in xrange(301,401):
        print i
        v=[]
        for j in xrange(1,101):
            for jj in xrange(1,101):
                if j!=jj:
                    real=g(i,j)-g(i,jj)
                    n=abs(real)
                    if real>0 and n>=0.05:
                        v.append((n,x(i,j),x(i,jj),1))
                    elif real<0 and n>=0.05:
                        v.append((n,x(i,j),x(i,jj),-1))



        v.sort(reverse=True)
        ite=0
        #print v

        while ite <100 and ite<len(v):
            a0=v[ite][1][0]-v[ite][2][0]
            a1=v[ite][1][1]-v[ite][2][1]
            a2=v[ite][1][2]-v[ite][2][2]
            b=v[ite][3]

            sampler.append(((a0,a1,a2),b))
            ite+=1

    for ite in sampler:
        print >>file1,ite


sample()








__author__ = 'hanz'
