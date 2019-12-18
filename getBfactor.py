#!/usr/bin/python
import sys
import re
import math
import datetime
import os
import re

"""
This code returns the maximum B-factor in each file in a dir.
"""

pdb_dir = "G:/Salah/RYR/12_2017_SVDexp_290bfactor_maps_models_5t9r_ca/new_b_factor/"
#output_dir = "G:/Salah/RYR/aligned/pdbs/"
bfactorlist = []
bfactorlist_2 = []
k = 0
for i in range (1,51): # number of files in the dir
    new_file = pdb_dir+str(i).zfill(2)+'_new_b_factor.pdb'
    pdb_lines_1 = open(new_file).readlines()
    for line in pdb_lines_1:
        fields = line.split()
        if fields[0] == 'ATOM':
            if len(fields) == 12:
                Bfactor = float(fields[10])
                bfactorlist.append(Bfactor)
            if len(fields) == 11:
                Bfactor = float(fields[9])
                bfactorlist.append(Bfactor)
        
    bfactorlist_2.append(bfactorlist)
    bfactorlist = []

print ('Done appending to list')


for k in range(0,50):
    print (str(k+1)+" "+str(max(bfactorlist_2[k])))

print ('Done :)')
