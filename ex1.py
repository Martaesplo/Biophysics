#Marta Espano Lopez

from Bio.PDB.NeighborSearch import NeighborSearch
from Bio.PDB.PDBParser import PDBParser
import argparse, sys, Bio.PDB
import numpy as np


#Parsing 
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('distance', type=float)
args = parser.parse_args()


#Determining a list of residues with CA atoms at a given distance:
MAXDIST = args.distance  #I gave to it the value of 20
parser = PDBParser(PERMISSIVE=1)
st = parser.get_structure('1UBQ','1ubq.pdb')

l=[]

for at in st.get_atoms():
    if at.id == 'CA':
        l.append(at)
        print("ATOM:", at.get_parent().get_resname(),at.get_parent().id[1], at.id)	

nbsearch = NeighborSearch(l)

print("NBSEARCH:")

ncontact = 1

for at1, at2 in nbsearch.search_all(MAXDIST):
    print("Contact: ", ncontact)
    print("at1", at1, at1.get_serial_number(), at1.get_parent().get_resname())
    print("at2", at2, at2.get_serial_number(), at2.get_parent().get_resname())
    print()
    ncontact += 1


#Command line: python3 ex1.py 1ubq.pdb 20
