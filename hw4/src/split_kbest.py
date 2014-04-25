import sys


file1=file('dev_kbest_hyp','w+')
file2=file('dev_kbest_f','w+')

for line in open('../data/dev.100best'):
    s=line.split('|||')
    #print s

    ite0=0
    output0=''
    while ite0<len(s[0])-1:
        output0+=s[0][ite0]
        ite0+=1

    ite1=1
    output1=''
    while ite1< len(s[1])-1:
        output1+=s[1][ite1]
        ite1+=1

    ite2=1
    output2=''
    while ite2 < len(s[2]):
        output2+=s[2][ite2]
        ite2+=1
    #print output0
    print >>file1,output1
    print >>file2,output2,








__author__ = 'hanz'
