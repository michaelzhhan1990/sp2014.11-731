import sys

for line in open('sample.json'):
    #s=line.split(' ')
    s=list(line)
    print s
    break
for line in open('../test_data/iris.trainfeat'):
    s=list(line)

    print s
    break

for line in open('y.json'):
    s=list(line)
    print s
    break
for line in open('../test_data/iris.trainresp'):
    s=list(line)
    print s
    break



__author__ = 'hanz'
