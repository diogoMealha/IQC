import os
MAX_CARBON_NUMBER = 100
DST_FOLDER = "CARBON_BASE"
for i in range(2, MAX_CARBON_NUMBER + 1):
    with open(f'{DST_FOLDER}/C_{i}.smi', "w") as file:
        for j in range(0, i):
            file.write("C")
        file.write("\n")
        file.close()

for i in range(2, MAX_CARBON_NUMBER + 1):
    command_change = f'obabel {DST_FOLDER}/C_{i}.smi -O {DST_FOLDER}/C_{i}.xyz --gen3d'
    command_delete = f'rm {DST_FOLDER}/C_{i}.smi'
    os.system(command_change)
    os.system(command_delete)





