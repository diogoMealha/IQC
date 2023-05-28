from optimize_molecules import opt_mol, OptCriteria
from separate_molecules import sep_mol
from molecule_info import mol_info
import os

ORIGINAL_FOLDER = "ORIGINAL_XYZ"
OPTIMIZED_FOLDER = "OPTIMIZED_MOL2"


# criteria for optimization
opt_crit = OptCriteria()
# options
opt_crit.steps = "5000"
opt_crit.algorithm = "-sd"
opt_crit.forcefield = "UFF" # universal forcefield
opt_crit.converge_c = "1e-15"


# separate molecules from mesh into folder and return their name
mol_name_list = sep_mol(dest_folder=ORIGINAL_FOLDER, mesh_file_name="DATA/molecules_mesh.txt")

# criteria for optimization
opt_crit = OptCriteria()
# options
opt_crit.steps = "5000"
opt_crit.algorithm = "-sd"
opt_crit.forcefield = "UFF" # universal forcefield
opt_crit.converge_c = "1e-15"

# loop through all molecules and optimize
for mol_name in mol_name_list:
    opt_mol(molecule_name=mol_name, source=ORIGINAL_FOLDER, destination=OPTIMIZED_FOLDER, criteria=opt_crit)


# find data about each molecule
mol_data = {}
for mol_name in mol_name_list:
    mol_data[mol_name] = mol_info(molecule_name=mol_name, source=OPTIMIZED_FOLDER,forcefield=opt_crit.forcefield)

print(mol_data)