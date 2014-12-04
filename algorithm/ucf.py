# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 15:26:19 2014

@author: Administrator
"""

import numpy as np
import scipy as sp

def gen_ajacent_from_txt(file,sep=None):
    data=np.genfromtxt(file,delimiter=sep)
    mat = sp.sparse.coo_matrix((data[:,2],(data[:,0]-1,data[:,1]-1)))
    return mat.tocsr()
    
def calcu_cosine_similarity(A):
    similarity = np.dot(A, A.T)
    square_mag = np.diag(similarity)

    # inverse squared magnitude
    inv_square_mag = 1 / square_mag
    
    # if it doesn't occur, set it's inverse magnitude to zero (instead of inf)
    inv_square_mag[np.isinf(inv_square_mag)] = 0
    
    # inverse of the magnitude
    inv_mag = np.sqrt(inv_square_mag)
    
    # cosine similarity (elementwise multiply by inverse magnitudes)
    cosine = similarity * inv_mag
    cosine = cosine.T * inv_mag
    return cosine
    
if __name__=='__main__':
    file = 'G:\\projects_lwj\\data\\ml-1m\\ratings.dat'
    mat=gen_ajacent_from_txt(file,'::')
    cos=calcu_cosine_similarity(mat.toarray())