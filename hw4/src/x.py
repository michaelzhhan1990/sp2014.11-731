import sys

def x(i,j):

    begin=(i-1)*100
    actual_j=begin+j
    ite=1
    output=[]
    for line in open('dev_kbest_f'):
        if ite==actual_j:
            s=line.split(' ')
            #print s

            for it,actu in enumerate(s):
                temp=actu.split('=')

                if it < len(s)-1:
                    output.append(temp[1])

                elif it ==len(s)-1:
                    kk=temp[1].split('\n')
                    output.append(kk[0])


            break
        ite+=1
    return (float(output[0]),float(output[1]),float(output[2]))







__author__ = 'hanz'
