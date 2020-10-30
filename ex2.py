from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser
import argparse, sys, Bio.PDB
import numpy as np

#Parsing
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('residue_number', type=int)
args = parser.parse_args()

parser = PDBParser(PERMISSIVE=1)
st = parser.get_structure('1UBQ','1ubq.pdb')

#Generating a list of atoms for a given residue number:
res_num = args.residue_number #I have given the residue number: 20

selec = []
res = st[0]["A"][res_num]

print ("Residue", res.get_resname(), res.id[1])
print("Atoms:")
for atom in res.get_atoms(): 
    print(res.get_resname(), res.id,
              atom.get_name(), atom.get_coord())


#Command line: python3 ex2.py 1ubq.pdb 30
