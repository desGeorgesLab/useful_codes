#!/usr/bin/python
import sys
import re
import math
import datetime
import os
import re

"""
This code calculates the atom_to_atom distance from two pdb.  It outputs new set
of PDBs into output_dir and the new atom_to_atom distance is saved in the B-factor column. 
"""


filename_1 = "G:/Salah/RYR/12_2017_SVDexp_290bfactor_maps_models_5t9r_ca/13_5t9r_cif_ca_class3_fit-coot-0_real_space_refined.pdb"

output_dir = "G:/Salah/RYR/12_2017_SVDexp_290bfactor_maps_models_5t9r_ca/new_b_factor/"
template = '{0:4s}{1:2s}{2:>5s}{3:1s}{4:<4s}{5:1s}{6:>3s}{7:1s}{8:1s}{9:>4s}{10:4s}{11:>8.3f}{12:>8.3f}{13:>8.3f}{14:>6.2f}{15:>6.2f}{16:<4s}{17:>2s}\n'

pdb_lines_1 = open(filename_1).readlines() 


#### This loop creates a list of lists with the x y z coords and saves new pdb with b-factor zero becuase we are calculating the distance
#    relative to this file
xyz = []
list_of_lists = []
new_file_13 = output_dir+'13_new_b_factor.pdb'
with open(new_file_13,'w') as fp:
    for line in pdb_lines_1:
        fields = line.split()
        if fields[0] != 'ATOM':
            fp.write(line)
        if fields[0] == 'ATOM':
            if len(fields) == 11:
                chainID = fields[4]
                res_number = fields[5]
                x = float(fields[6])
                y = float(fields[7])
                z = float(fields[8])
                xyz.append(fields[6])
                xyz.append(fields[7])
                xyz.append(fields[8])
                end = fields[10]
            if len(fields) == 10:
                chainID = fields[4][:1]
                res_number = fields[4][1:]
                xyz.append(fields[5])
                xyz.append(fields[6])
                xyz.append(fields[7])
                x = float(fields[5])
                y = float(fields[6])
                z = float(fields[7])
                end = fields[9]
            if len(fields) == 12:
                chainID = fields[4]
                res_number = fields[5]
                x = float(fields[6])
                y = float(fields[7])
                z = float(fields[8])
                xyz.append(fields[6])
                xyz.append(fields[7])
                xyz.append(fields[8])
                end = fields[11]
            list_of_lists.append(xyz)
            xyz = []
            fp.write(template.format(fields[0],'  ',fields[1],' ',fields[2],' ',fields[3],' ',chainID,res_number,'    ',x,y,z,1.00,0.00,'    ',end))
    fp.close()
            




            
distances = []


#### This loop goes calculates the atom_to_atom distance between file 13 and every file in the dir
for i in range(1,51):
    filename_2 = "G:/Salah/RYR/12_2017_SVDexp_290bfactor_maps_models_5t9r_ca/"+str(i).zfill(2)+"_5t9r_cif_ca_class3_fit-coot-0_real_space_refined.pdb"
    pdb_lines_2 = open(filename_2).readlines()
    new_file = output_dir+str(i).zfill(2)+'_new_b_factor.pdb'
    k = 0
    with open(new_file,'w') as fp:
        for line in pdb_lines_2:
            fields = line.split()
            if fields[0] != 'ATOM':
                fp.write(line)
            if fields[0] == 'ATOM':
                
                if len(fields) == 11:  # sometimes in the pdb we have col 4 and 5 in one col :(
                    chainID = fields[4]
                    res_number = fields[5]
                    x = float(fields[6])
                    y = float(fields[7])
                    z = float(fields[8])
                    x1 = math.pow(float(list_of_lists[k][0]) - float(fields[6]),2)
                    x2 = math.pow(float(list_of_lists[k][1]) - float(fields[7]),2)
                    x3 = math.pow(float(list_of_lists[k][2]) - float(fields[8]),2)
                    end = fields[10]
                if len(fields) == 10:
                    chainID = fields[4][:1]
                    res_number = fields[4][1:]
                    x = float(fields[5])
                    y = float(fields[6])
                    z = float(fields[7])
                    x1 = math.pow(float(list_of_lists[k][0]) - float(fields[5]),2)
                    x2 = math.pow(float(list_of_lists[k][1]) - float(fields[6]),2)
                    x3 = math.pow(float(list_of_lists[k][2]) - float(fields[7]),2)
                    end = fields[9]
                if len(fields) == 12:
                    chainID = fields[4]
                    res_number = fields[5]
                    x = float(fields[6])
                    y = float(fields[7])
                    z = float(fields[8])
                    x1 = math.pow(float(list_of_lists[k][0]) - float(fields[6]),2)
                    x2 = math.pow(float(list_of_lists[k][1]) - float(fields[7]),2)
                    x3 = math.pow(float(list_of_lists[k][2]) - float(fields[8]),2)
                    end = fields[11]
                d = math.sqrt(x1+x2+x3)
                distances.append(d)
                fp.write(template.format(fields[0],'  ',fields[1],' ',fields[2],' ',fields[3],' ',chainID,res_number,'    ',x,y,z,1.00,d,'    ',end))
                k += 1
        fp.close()


     
print ('Done')

