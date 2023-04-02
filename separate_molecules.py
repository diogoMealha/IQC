mesh_info = {}
file_path__ = None
with open('molecules_mesh.txt', 'r') as f:
    for line in f.readlines():
        if(line[0] == 'M' or line == "end"):
            if file_path__ != None:
                mesh_info[file_path__][0] = str(len(mesh_info[file_path__]) - 1) + "\n"
             
            file_path__ = line[:-1].replace(" ", "_")
            if(line != "end"):
                mesh_info[file_path__] = [0]
        else:
            mesh_info[file_path__].append(line)

PATH = "FOLDER/"
COMMENT = "Carbon bond length: "
for key in mesh_info.keys():
    with open(PATH + key + ".xyz", 'w') as f:
        f.write(mesh_info[key][0])
        f.write(COMMENT + "\n")
        for line in mesh_info[key][1:]:
            foo = line.split()
            f.write(f'{foo[0]} \t {foo[1]} \t {foo[2]} \t {foo[3]}\n')


