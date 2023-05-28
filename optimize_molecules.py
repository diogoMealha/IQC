import os
class OptCriteria:
    # optimization criteria info
    algorithm = None  # algorithm used
    steps = None  # number of steps
    forcefield = None  # used forcefield
    converge_c = None  # convergence criteria


def opt_mol(molecule_name, source, destination, criteria: OptCriteria):
    # outputs the molecule in an optimized state
    mol_xyz = molecule_name + ".xyz"
    mol_pdb = molecule_name + ".pdb"
    mol_mol2 = molecule_name + ".mol2"

    fetch_folder = source  # folder with original molecules
    save_folder = destination  # folder with optimized molecules

    # optimize molecule parameters
    ALGORITHM = criteria.algorithm
    FORCEFIELD = criteria.forcefield
    CONVERGENCE_CRITERIA = criteria.converge_c
    N_STEPS = criteria.steps

    # obminize outputs molecule in pdb format
    command_optimize = f'obminimize {ALGORITHM} -ff {FORCEFIELD} -c ' \
                       f'{CONVERGENCE_CRITERIA} -n {N_STEPS} ' \
                       f'{fetch_folder}/{mol_xyz} > {save_folder}/{mol_pdb}'  #

    # transform to mol2 format
    command_to_mol2 = f'obabel -i pdb {save_folder}/{mol_pdb} -o mol2 -O {save_folder}/{mol_mol2}'

    # remove the pdb file
    command_remove_pdb = f'rm {save_folder}/{mol_pdb}'

    # final commands
    os.system(command_optimize)
    os.system(command_to_mol2)
    os.system(command_remove_pdb)



