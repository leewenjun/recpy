# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 16:16:14 2014

@author: Administrator
"""
import numpy as np
def precision(predition,test,l=10):
    top_idxs= np.argsort(-predition,axis=1);
    m,k=top_idxs.shape
    recall=0.
    precision=0.
    num=0
    for i in test.keys():
        if np.all(predition[i,:]==0.):
            continue
        p=top_idxs[i,0:l].tolist()
        num+=1
        t=test[i]
        s=len(set(p).intersection(t))
        precision+=float(s)/l
        recall+=float(s)/len(t)
    precision/=num
    recall/=num
    f1=2*recall*precision/(precision+recall)
    return precision,recall,f1
    
def load_test(test_file):
    in_file=open(test_file,'r')
    test={}
    for line in in_file:
        u,o,r,t=line.split('\t')
        key = int(float(u))
        value= int(float(o))
        if not test.has_key(key):
            test[key]=set()
        test[key].add(value)
    return test
     
if __name__=='__main__':
    test_file=r'/Volumes/GRMCULXFRER/ml-1m/test.txt'
    t=load_test(test_file)
    precision,recall,f1=precision(prediction,t)