#!/usr/bin/env python



def initializer(f,p,u,origin,tm):

    for ite in xrange(1,len(f)+1):
        u[ite]=0

    for ite in xrange(1,len(f)+1):
            origin[ite]=0

    # get all possible edge from input
    for i in xrange(0,len(f)):
            p[i+1]={}
            for j in xrange(i+1,len(f)+1):
                p[i+1][j]=[]
                if f[i:j] in tm:
                    for e in tm[f[i:j]]:
                        p[i+1][j].append((e.logprob,e.english))










__author__ = 'hanz'
