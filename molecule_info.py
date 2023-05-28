# find the biggest carbon distance and calculate energy
import math
import os
def mol_info(molecule_name, source, forcefield):
    mol_name = molecule_name + ".mol2"
    fetch_folder = source

    read_codes = False; c_codes = {} # mol2 file ids of Carbon atoms that have a C-C bond
    read_distances = False; distances = [] # bool to decide if its time to read distances

    with open(f'{fetch_folder}/{mol_name}') as f:
        # carbon distance
        for line in f:
            if read_distances: # calc dist between carbon atoms if there is a bond
                info = line[:-1].split() # 0: count 1: ATOM 1 2: ATOM 2
                if info[1] in c_codes.keys() and info[2] in c_codes.keys():
                    # calculate the distance
                    ATOM1 = c_codes[info[1]] # pos of carbon 1
                    ATOM2 = c_codes[info[2]] # pos of carbon 2
                    distances.append(round(math.dist(ATOM1, ATOM2), 4))

            if line[:-1] == "@<TRIPOS>BOND": # get info on C codes -> bons
                read_codes = False
                read_distances = True

            if read_codes:
                info = line[:-1].split() # 0: id 1: ATOM 2-4: pos
                if info[1] == 'C':
                    c_codes[info[0]] = (float(info[2]), float(info[3]), float(info[4]))

            if line[:-1] == "@<TRIPOS>ATOM": # get info on C codes -> pos
                read_codes = True

        f.close()
        # energy
        mol_energy = None

        # set file optimized in xyz
        command_changeFormat = f'obabel -i mol2 {source}/{mol_name} -o xyz -O {source}/{molecule_name}.xyz'
        os.system(command_changeFormat)
        foo_file = 'energy.txt' # store output of obenergy tp read last line
        command_energy = f'obenergy -ff {forcefield} {source}/{molecule_name}.xyz > {foo_file}'
        command_rm_energy_file = f'rm {foo_file}'
        os.system(command_energy)
        # read last line of energy.txt

        with open(foo_file, "r") as file:
            last_line = file.readlines()[-1]
        mol_energy = float(last_line.split()[3])
        file.close()

        os.system(command_rm_energy_file) # delete after read

        if len(distances) == 0:
            print(mol_name)
            return [None, None]
        return [max(distances), mol_energy]

