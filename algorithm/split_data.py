# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 15:56:03 2014

@author: Administrator
"""
import numpy as np

def eight_two_by_time(infile,train_file,test_file):
    out_file=open(train_file,'w')
    data = np.genfromtxt(infile)
    idx=np.argsort(data[:,3])
    flag=int(data.shape[0]*0.8)
    for i in range(0,flag):
        out_file.write(str(data[idx[i],0])+'\t'+str(data[idx[i],1])+'\t'+str(data[idx[i],2])+'\t'+str(data[idx[i],3])+'\n')
    out_file.flush()
    out_file.close()
    
    out_file=open(test_file,'w')
    for i in range(flag,data.shape[0]):
        out_file.write(str(data[idx[i],0])+'\t'+str(data[idx[i],1])+'\t'+str(data[idx[i],2])+'\t'+str(data[idx[i],3])+'\n')
    out_file.flush()
    out_file.close()
    
if __name__=='__main__':
    file = r'G:\projects_lwj\data\ml-1m\original_ratings.txt'
    train_file=r'G:\projects_lwj\data\ml-1m\train.txt'
    test_file=r'G:\projects_lwj\data\ml-1m\test.txt'
    eight_two_by_time(file,train_file,test_file)