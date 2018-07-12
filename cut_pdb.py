#!/usr/bin/python
import sys
import re
import math
import datetime
import os
import re

"""
This code is to cut PDB files based on fields. This code is used to cut the orginal PDB saved in the refined/ directory from res. # 3614 and above and only the B chian.  

Made by Salah Salah (SalahEzSalah@gmail.com)
Date:  Juny 10th. 2018
"""

for i in range(1,51): # Because I have 50 PDB
	with open("../input_data/activation_core/"+str(i).zfill(2)+".pdb",'w') as new_pdb:
		refined_location = "../input_data/refined/"+str(i).zfill(2)+"_5t9r_norm_psi_Class50_SVD12_bfac290_4.5A_real_space_refined.pdb"
		# Read all PDB files from ryr1_energyCalculations/input_data/refined
		file_name = open(refined_location).readlines() 
		for line in file_name:
			fields = line.split()
			if len(fields) > 8:
				if fields[0] == "ATOM":
					if len(fields) == 10: # because the the chain id and the res # are in the same columns
						chian_id = fields[4][:1]
						if chian_id == 'B' and fields[4][1:] >= "3614":
							new_pdb.write(line)
					#if len(fields) == 11: # because the the chain id and the res # are in separate columns
						#chian_id = fields[4]
						#if chian_id == 'B' and fields[4][1:] == "3741":
							#new_pdb.write(line)
		new_pdb.close()



	

