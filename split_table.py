

def MakeTPath():
    f = open("16S_in", "r")

    Lines = f.readlines()

    Table = []

    for line in Lines:
        if line[0] == '>':
            SeqId = line[1:].split(' ',1)
            TPath = SeqId[1].split(';')
            SeqId = SeqId[0]
            Table.append((SeqId,Table))

    print(Table)

if __name__ == '__main__':
    MakeTPath()