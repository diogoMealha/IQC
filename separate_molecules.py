def sep_mol(dest_folder, mesh_file_name):
    PATH = dest_folder + "/"
    COMMENT = "Comments: "
    MESH_FILE = mesh_file_name

    mesh_info_dic = {}
    file_name = None
    # store data
    with open(MESH_FILE, 'r') as f:
        for line in f.readlines():
            if line[0] == 'M' or line == "end":
                if file_name is not None:
                    mesh_info_dic[file_name][0] = str(len(mesh_info_dic[file_name]) - 1) + "\n"
                file_name = line[:-1].replace(" ", "_")
                if(line != "end"):
                    mesh_info_dic[file_name] = [0]
            else:
                mesh_info_dic[file_name].append(line)
        f.close()

    # write data
    for key in mesh_info_dic.keys():
        with open(PATH + key + ".xyz", 'w') as f:
            f.write(mesh_info_dic[key][0])
            f.write("Name: " + key + " " + COMMENT + "\n")
            for line in mesh_info_dic[key][1:]:
                foo = line.split()
                f.write(f'{foo[0]} \t {foo[1]} \t {foo[2]} \t {foo[3]}\n')

    # return list of all molecule names
    return [mol_name for mol_name in mesh_info_dic.keys()]
