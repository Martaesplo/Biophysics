from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser
import argparse, sys, Bio.PDB
import numpy as np

#Parsing
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

parser = PDBParser(PERMISSIVE=1)
st = parser.get_structure('1UBQ','1ubq.pdb')

ato=[]
dist=3.5

#Getting all the atoms
for a in st.get_atoms():
	ato.append(a)

neighb = NeighborSearch(ato)

c=0

#Getting the number of hydrogen bonds
for a1, a2 in neighb.search_all(dist):
	atom1 = a1.get_name()
	atom2 = a2.get_name()
	if atom1 in 'NOS' and atom2 in 'NOS':
		if (atom1 == 'N' and atom2 !='N') or (atom1 == 'O' and atom2 != 'O') or (atom1 == 'S' and atom2 != 'S'):
			print('atom1=',a1,'atom2=',a2)
			c+=1
print('Number of hydrogen bonds:',c)


#Command line: python3 ex3.py 1ubq.pdb
