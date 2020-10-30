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

#Getting number of chains
print('Chains: ', len(st[0]))
print('All chains:', ','.join([ch.id for ch in st[0]]))

#Getting backbone residue connectivity
for i in st:
	for t in i:
		print('chain:',t.id)
		for r in t:
			print('Residue:',r.get_resname())


#Command line: python3 ex5.py 1ubq.pdb
