# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 16:41:07 2014

@author: ui01
"""

#==============================================================================
import numpy as np
import scipy as sp
from scipy.sparse import linalg
# 
# #mv-100k
user_size=943
item_size=1682
data=np.genfromtxt('D:/academic/data/movielens-100k/rel.rating')
print 'data loaded'

a=sp.sparse.lil_matrix((user_size,item_size))
for i in range(data.shape[0]):
    a[data[i,0]-1,data[i,1]-1]=data[i,2]

# 
# size=user_size+item_size
# 
# a=sp.sparse.lil_matrix((size,size))
# for i in range(data.shape[0]):
#     u_idx=data[i,0]-1
#     o_idx=data[i,1]-1
#     rate=data[i,2]
#     a[u_idx,user_size+o_idx]=rate
#     a[user_size+o_idx,u_idx]=rate
#==============================================================================

#a=np.array(a.todense())
#
#for i in range(mat.shape[0]):
#    for j in range(mat.shape[1]):
#        if mat[i,j]!=mat[j,i]:
#            print str(i)+","+str(j)


print 'finish'