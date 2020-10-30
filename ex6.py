from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser
import argparse, sys, Bio.PDB
import numpy as np

#Parsing
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('residue1', type=int)
parser.add_argument('residue2', type=int)
args = parser.parse_args()

parser = PDBParser(PERMISSIVE=1)
st = parser.get_structure('1UBQ','1ubq.pdb')

#Residue selection
res10 = args.residue1
res20 = args.residue2

res1 = st[0]["A"][res10]
res2 = st[0]["A"][res20]

print("Residue 1 is", res1.get_resname()) #Giving as input residue 10
print("Residue 2 is", res2.get_resname()) #Giving as input residue 20


#Computing of distances between atoms of residue1 and residue 2
print("\nAtom1 Atom2 dist1 dist2\n-------------------------")
for at1 in res1.get_atoms():      
    for at2 in res2.get_atoms():
        dist = at2 - at1     
        vector = at2.coord - at1.coord
        distance = np.sqrt(np.sum(vector ** 2))
        print(at1, at2, dist, distance)


#Command line: python3 ex6.py 1ubq.pdb 10 20
