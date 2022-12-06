
import matplotlib.pyplot as plt


def group_by_length():
    def random(a):
        f = open("16S_in", "r")
        f_out = open("final_read_fastq_20220913_v2", 'a')

        firsLine = f.readline()
        firsLine = firsLine.split(' ', 1)[0]
        restSeq = f.read()

        coverage = [0] * len(restSeq)
        # --------------------

        c = int((len(restSeq) + 50) / (((len(restSeq) - 200) * a) / 150))
        print("c:  " + str(c))

        # --------------------
        x = len(restSeq)

        short_reads = 0

        it_end = 0

        Length_diff = []

        while it_end < len(restSeq):

            if it_end + 150 > len(restSeq):
                if it_end + 50 > len(restSeq):
                    it_end = len(restSeq) + 1
                    break
                else:
                    read_end = len(restSeq)
            else:
                read_end = it_end + 150

            for delete in range(it_end, read_end):
                coverage[delete] += 1

            string_out = "@" + firsLine[1:] + "|" + "S" + str(it_end) + "E" + str(read_end) + "\n" \
                         + restSeq[it_end:read_end] + "\n" + "+" \
                         + "\n" + "H" * (read_end - it_end) + "\n"

            f_out.write(string_out)

            Length_diff.append(read_end - it_end)
            print(read_end - it_end)

            it_end += c

        plt.plot(coverage)
        plt.title("4th shifting Method")
        plt.show()

        plt.plot(Length_diff)
        plt.title("Length different: " + str(len(Length_diff)))
        plt.show()


#final prod.
def random(a):
    f = open("16S_in", "r")
    f_out = open("final_read_fastq_20220913_v2", 'a')

    firsLine = f.readline()
    firsLine = firsLine.split(' ', 1)[0]
    restSeq = f.read()

    coverage = [0] * len(restSeq)
    #--------------------

    c = int((len(restSeq)+50)/(((len(restSeq)-200)*a)/150))
    print("c:  " + str(c))

    #--------------------
    x = len(restSeq)

    short_reads = 0

    it_end =0

    Length_diff =[]

    while it_end < len(restSeq):

        if it_end+150 > len(restSeq):
            if it_end + 50 > len(restSeq):
                it_end = len(restSeq)+1
                break
            else:
                read_end =len(restSeq)
        else:
            read_end = it_end+150


        for delete in range(it_end,read_end):
            coverage[delete] += 1

        string_out = "@"+firsLine[1:] + "|" + "S" + str(it_end) + "E" + str(read_end) + "\n" \
                     + restSeq[it_end:read_end] + "\n"+ "+" \
        +"\n" +"H" * (read_end-it_end)+"\n"

        f_out.write(string_out)

        Length_diff.append(read_end-it_end)
        print(read_end-it_end)


        it_end += c



    plt.plot(coverage)
    plt.title("4th shifting Method")
    plt.show()

    plt.plot(Length_diff)
    plt.title("Length different: " +str(len(Length_diff)))
    plt.show()



def shift3(a):
    f = open("16S_in", "r")
    f_out = open("shifted_reads", 'a')

    firsLine = f.readline()
    firsLine = firsLine.split(' ', 1)[0]
    restSeq = f.read()

    coverage = [a] * len(restSeq)

    x = len(restSeq)
    short_reads = 0

    while x > 0:
        if x - 250 > 0:
            x -= 250
            short_reads += 1
        else:
            break

    cover = int(((short_reads + 1) * 250 - len(restSeq)) / short_reads)
    print("EZ: " + str(cover))

    for s in range(0, a):

        for i in range(0, short_reads):

            for delete in range(i * (250 - cover), i * (250 - cover) + 250):
                coverage[delete] -= 1

            string_out = firsLine + "|" + "S" + str(i * (250 - cover)) + "E" + str(i * (250 - cover) + 250) + "C" + str(
                s) + "\n" \
                         + restSeq[i * (250 - cover):i * (250 - cover) + 250] + "\n"
            f_out.write(string_out)

        #eredeti: remain = len(restSeq) - ((short_reads -1) * (250 - cover) + 250)
        remain = len(restSeq) - ((short_reads -1) * (250 - cover) + 250-cover)

        for delete in range(len(restSeq) - remain, len(restSeq)):
            coverage[delete] -= 1

        string_out = firsLine + "|" + "S" + str(len(restSeq) - remain) + "E" + str(len(restSeq)) + "C" + str(
            s) + "\n" \
                     + restSeq[len(restSeq) - remain:len(restSeq)] + "\n"
        f_out.write(string_out)

    print(coverage)
    plt.plot(coverage)
    plt.title("Coverage Method Shifting 3")
    plt.show()


def shift2(a):
    f = open("16S_in", "r")
    f_out = open("shifted_reads", 'a')

    firsLine = f.readline()
    firsLine = firsLine.split(' ', 1)[0]
    restSeq = f.read()

    coverage = [a] * len(restSeq)

    x = len(restSeq)
    short_reads = 0

    while x > 0:
        if x - 250 > 0:
            x -= 250
            short_reads += 1
        else:
            break

    cover = int(((short_reads+1) * 250 - len(restSeq)) / short_reads)
    print("EZ: " + str(cover))

    for s in range(0, a):

        for i in range(0, short_reads):

            for delete in range(i * (250 - cover), i * (250 - cover) + 250):
                coverage[delete] -= 1

            string_out = firsLine + "|" + "S" + str(i * (250 - cover)) + "E" + str(i * (250 - cover) + 250) + "C" + str(
                s) + "\n" \
                         + restSeq[i * (250 - cover):i * (250 - cover) + 250] + "\n"
            f_out.write(string_out)

        remain = len(restSeq) - ((short_reads - 1) * (250 - cover) + 250)

        for delete in range(len(restSeq) - remain, len(restSeq)):
            coverage[delete] -= 1

        string_out = firsLine + "|" + "S" + str(len(restSeq) - remain) + "E" + str(len(restSeq)) + "C" + str(
            s) + "\n" \
                     + restSeq[len(restSeq) - remain:len(restSeq)] + "\n"
        f_out.write(string_out)

    print(coverage)
    plt.plot(coverage)
    plt.title("Coverage Method Shifting 2")
    plt.show()


def shift(a):
    f = open("16S_in", "r")
    f_out = open("shifted_reads", 'a')

    firsLine = f.readline()
    firsLine = firsLine.split(' ', 1)[0]
    restSeq = f.read()

    coverage = [a] * len(restSeq)

    x = len(restSeq)
    short_reads = 0

    while x > 0:
        if x - 250 > 0:
            x -= 250
            short_reads += 1
        else:
            break

    cover = int(x / short_reads)

    for s in range(0, a):

        for i in range(0, short_reads):

            for delete in range(i * (250 - cover), i * (250 - cover) + 250):
                coverage[delete] -= 1

            string_out = firsLine + "|" + "S" + str(i * (250 - cover)) + "E" + str(i * (250 - cover) + 250) + "C" + str(
                s) + "\n" \
                         + restSeq[i * (250 - cover):i * (250 - cover) + 250] + "\n"
            f_out.write(string_out)

        remain = 250 - x

        for delete in range(len(restSeq) - remain, len(restSeq)):
            coverage[delete] -= 1

        string_out = firsLine + "|" + "S" + str(len(restSeq) - remain) + "E" + str(len(restSeq)) + "C" + str(
            s) + "\n" \
                     + restSeq[len(restSeq) - remain:len(restSeq)] + "\n"
        f_out.write(string_out)

    print(coverage)
    plt.plot(coverage)
    plt.title("Coverage Method Shifting")
    plt.show()


if __name__ == '__main__':
    shift(30)
    shift2(30)
    shift3(30)
    random(30)
