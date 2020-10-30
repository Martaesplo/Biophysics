from Bio.PDB.PDBIO import PDBIO
from Bio.PDB.PDBParser import PDBParser
import argparse, sys, Bio.PDB
import numpy as np

#Parsing 
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('--list', nargs ='+')
args = parser.parse_args()

parser = PDBParser(PERMISSIVE=1)
st = parser.get_structure('1UBQ','1ubq.pdb')

#Obtain the chain identifier
print (','.join([ch.id for ch in st[0]])) 

#Obtain only the chain information and store it in PDB format
chains_ok = args.list

for chn in st[0]:
    if chn.id not in chains_ok:
        st[0].detach_child(chn.id)

output_pdb_path = "chains_ex7.pdb"

pdbio = PDBIO()

pdbio.set_structure(st)
pdbio.save(output_pdb_path)


#Command line: python3 ex7.py 1ubq.pdb --list A C

