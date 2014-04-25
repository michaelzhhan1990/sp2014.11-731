import sys
import json
for line in open('../test_data/shuttle.trainresp'):
    print line
    s=list(line)
    print s


    break





file0=file('sample.json','w+')
file1=file('y.json','w+')
ite=0
for line in open('sample'):
    s=line[2:len(line)-7]
    #print s
    ss=s.split(',')
    #print ss
    #print ss[0]
    #print ss[1][1:len(ss[1])]
    #print ss[2][1:len(ss[2])]
    #st=str(ite)+'\t'+'{"one": '+ss[0]+','+' "two": '+ss[1][1:len(ss[1])]+','+' "three": '+ss[2][1:len(ss[2])]+'}'
    #print >>file0,st
    #str(ite)+'\t'+'{"one": '+ss[0]+','+' "two": '+ss[1][1:len(ss[1])]+','+' "three": '+ss[2][1:len(ss[2])]+'}'
    data={'one':float(ss[0]),'two':float(ss[1][1:len(ss[1])]),'three':float(ss[2][1:len(ss[2])])}
    je=json.dumps(data)
    print >>file0,str(ite)+'\t'+je

    #print je


    y=line[len(line)-4]


    if y=='-':
        print >>file1,str(ite)+'\t'+'-1'
    else:
        print >>file1,str(ite)+'\t'+'1'

    ite+=1
















__author__ = 'hanz'
