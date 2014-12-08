# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 15:32:00 2014

@author: Administrator
"""

def clean(infile,sep,outfile):
    out_file=open(outfile,'w')
    in_file=open(infile,'r')
    u_dict = {}
    o_dict = {}
    u_idx = 0
    o_idx = 0
    for line in in_file:
        u,o,r,t = line.split(sep)
        if not u_dict.has_key(u):
            u_dict[u]=u_idx
            u_idx+=1
        if not o_dict.has_key(o):
            o_dict[o]=o_idx
            o_idx+=1
        out_file.write(str(u_dict[u])+'\t'+str(o_dict[o])+'\t'+r+'\t'+t)
    out_file.flush()
    in_file.close()
    out_file.close()
    
if __name__=='__main__':
    file = r'G:\projects_lwj\data\ml-1m\ratings.dat'
    out_file=r'G:\projects_lwj\data\ml-1m\original_ratings.txt'
    clean(file,'::',out_file)