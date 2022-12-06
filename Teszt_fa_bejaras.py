def Make_tree2array(names_file):
    names = {}

    for line in names_file:
        if line == "\n":
            print("empty row")
            continue

        data = [attr.strip() for attr in line.split("|")[0:2]]
        print(data[0] + "  -  " + data[1])
        names[data[1]] = int(data[0])

    return names


def Nodes2Array(nodes_file):
    nodes = {}

    for line in nodes_file:
        if line == "\n":
            print("empty row")
            continue

        data = [attr.strip() for attr in line.split("|")[0:3]]

        nodes[int(data[0])] = [int(data[1]), data[2]]
    return nodes


def Find_Value2Key_in_Names(Key, nodes, names, Taxon):
    if Key in sorted(names):
        Key_in_nodes = names[Key]
        if Key_in_nodes in sorted(nodes):
            if nodes[Key_in_nodes][1] == Taxon:
                return Key
            # ----------------------------------------------------------------------------
            else:
                Find_Value2Key_in_Names(nodes[Key_in_nodes][0], nodes, names, Taxon)
        else:
            print("Key_in_nodes cannot be found.")
    else:
        print("Key cannot be found.")
    print("")


if __name__ == '__main__':
    names_file = open("names.dmp", "r")
    nodes_file = open("nodes.dmp", "r")

    na = Make_tree2array(names_file)
    no = Nodes2Array(nodes_file)
    key = Find_Value2Key_in_Names('F', no, na, "genus")
    if type(key) != str:
        print("str")


    print(key)
    print(na[key])
