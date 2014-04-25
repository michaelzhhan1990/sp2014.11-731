#!/usr/bin/env python
from __future__ import division
import sys,math
import models
import heapq
import copy


def generate_states(st,states,state_dic,check_dic,p,origin,length,u,lm,final_dic):
    base_log=state_dic[st[0]][st][0]
    base_str=state_dic[st[0]][st][2]
    base_pre=state_dic[st[0]][st][1]

    if st[0]<length:

        for s in xrange(max(1,st[3]-5),st[3]+6):

            n=0
            if s in p:
                for t in p[s]:
                    if t<st[1] or s>st[2]:
                        n=st[0]+t-s+1
                        distortion=abs(st[3]-t+1)
                        check_temp=copy.deepcopy(check_dic[st[0]][st])
                        if distortion<=5 and n<=length:

                            lagrange=0
                            for ite in xrange(s,t+1):
                                lagrange+=u[ite]
                                check_temp[ite]+=1

                            for p_p in p[s][t]:
                                logprob=p_p[0]+lagrange
                                sttr=p_p[1]


                                for e in sttr.split():
                                    (lm_state,word_logprob)=lm.score(st[4],e)
                                    logprob+=word_logprob

                                if s==st[2]+1:
                                    l=st[1]
                                    m=t
                                elif t==st[1]-1:
                                    l=s
                                    m=st[2]
                                else:
                                    l=s
                                    m=t

                                r=t

                                logprob+=base_log
                                logprob-=0.1*distortion
                                tup=(n,l,m,r,lm_state)

                                if tup not in state_dic[n]:
                                    heapq.heappush(states,tup)
                                    state_dic[n][tup]=[logprob,st,sttr]
                                    check_dic[n][tup]=copy.deepcopy(check_temp)

                                elif state_dic[n][tup][0]<logprob:
                                    state_dic[n][tup][0]=logprob
                                    check_dic[n][tup]=copy.deepcopy(check_temp)

                        check_temp=None

    else:
        log=base_log
        log+=lm.end(st[4])
        final_dic[st]=[log,base_pre,base_str]











__author__ = 'hanz'
