from bleu import *

# i from 1:400, j from 1:100

def g(i,j):
    h=''
    r=''
    ite=1
    for line in open('../data/dev.ref'):
        if ite==i:
            r=line
            break
        ite+=1

    begin=(i-1)*100
    actual_j=begin+j

    ite=1
    for line in open('dev_kbest_hyp'):
        if ite==actual_j:
            h=line
            break
        ite+=1
    #print r
    #print h


    stats=[]
    for i in bleu_stats(h,r):
        #print i
        stats.append(i)

    return bleu(stats)






