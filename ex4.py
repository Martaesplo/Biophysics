from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser
import argparse, sys, Bio.PDB
import numpy as np

#Parsing 
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('residue_type', type=str)
args = parser.parse_args()

parser = PDBParser(PERMISSIVE=1)
st = parser.get_structure('1UBQ','1ubq.pdb')

#Determining a list of residues with CA atoms of a given type:
selec = []

res_t = args.residue_type #I have given to it SER residue

print('Residue:', res_t)
for a in st.get_atoms():
	if a.get_parent().get_resname() in res_t:
		if a.id == 'CA':
			selec.append(a)

print('Coordinates:')
for at in selec:
	print(at.get_parent().get_resname(), at.get_parent().id, 
	at.get_name(), at.get_coord())


#Command line: python3 ex4.py 1ubq.pdb SER
