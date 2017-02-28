# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 09:27:05 2017

@author: jmorel
"""

def pd_2Dtranslate(list_of_stuff,size=8):
    """
    Translates 1D list into Np 2D array using basic list generation. This is similar/combined functionality
    of numpy.reshape or numpy.asarray.
    
    Parameters
    -----
    input_list: list
        List of items to be translated into Np array
    size: int, optional
        Size of each level of 2D array (ie lenght of each row). Default = 8 due to well plate row number.
        By specifying the size and knowing the number of points in the list, the length of each column is 
        implied.
    
    Output
    -----
    2D Numpy array
    """
    #Requires data to be a full array
    # If excess points > 0 array will not be filled
    if len(list_of_stuff)%size>0:
        print('ERROR: Size of input does allow fully filled array of size nx%i'%size)
        exit
    
    import numpy as np #Use for final array generation
    cols_by_rows=[] #Final level 2 list 
    rows=[] #Rows of data
    row_pos=0 #Current position inside row
    for i in list_of_stuff:
        #If the size of the row is reached:
        if row_pos>=size:
            cols_by_rows.append(rows)
            rows=[i]
            row_pos=1
        #Else appending new items row wise
        else:
            rows.append(i)
            row_pos+=1
            #If the end of the input list is reached:
            if row_pos==len(list_of_stuff):
                cols_by_rows.append(rows)
    return np.array(cols_by_rows)
