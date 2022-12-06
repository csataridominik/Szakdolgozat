import random
import matplotlib.pyplot as plt
import numpy as np




def dev(array):
    n = len(array)

    mean = sum(array) / n

    deviations = [(x - mean) ** 2 for x in array]

    variance = sum(deviations) / n

    return variance


def read_cover_(a):
    f = open("16S_in", "r")
    f_out = open("test_1000seq_50_k", 'a')

    firsLine = f.readline()
    firsLine = firsLine.split(' ', 1)[0]
    restSeq = f.read()
    coverage = [0] * len(restSeq)
    coverage2 = [0] * len(restSeq)

    randomlist = []

    Single_read = int(len(restSeq)/250)
    #print("Singel Read:  " +str((Single_read)))

    for s in range(0, a):

        for i in range(0, Single_read):
            n = random.randint(0, len(restSeq) - 250)
            randomlist.append(n)

            for delete in range(randomlist[-1], (randomlist[-1] + 250)):
                coverage[delete] += 1
            # if range(n - 50, n + 50) in randomlist:
            #   i = i - 1
            # else:
            string_out = firsLine + "|" + "S" + str(randomlist[-1]) + "E" + str(randomlist[-1] + 250) + "C" + str(
                s) + "\n" \
                         + restSeq[randomlist[-1]:(randomlist[-1] + 250)] + "\n"
            f_out.write(string_out)

            ##MÁSIK RANDOM --------------------------------------------------------------------------

            # n = random.randint(0, len(restSeq) - 250)
            starting_points = random.choices(range(0, len(restSeq) - 250), k=Single_read)

        for start in starting_points:


            for delete in range(start, start + 250):
                coverage2[delete] += 1
            # if range(n - 50, n + 50) in randomlist:
            #   i = i - 1
            # else:
            # string_out =firsLine+"|"+"S"+str(randomlist[-1])+"E"+str(randomlist[-1]+250)+"C"+str(s)+"\n" \
            # +restSeq[randomlist[-1]:(randomlist[-1]+250)]+"\n"
            # f_out.write(string_out)

   # print(coverage)
  #  print("Variance: " + str(dev(coverage)))

 #   print(coverage2)
#    print("Variance: " + str(dev(coverage)))


    return coverage


def Singel_read250bp():
    f = open("16S_in", "r")
    f_out = open("16S_reads", 'a')

    firsLine = f.readline()
    restSeq = f.read()
    # print(restSeq[0:250])

    x = 0
    y = 250
    end = 0

    while 1 == 1:
        string01 = restSeq[x:y]
        x = y
        y += 250

        if y > len(restSeq):
            y = len(restSeq)
            end = 1

        string_out = firsLine + "S" + str(x) + "E" + str(y) + "\n" + restSeq[x:y] + "\n"
        f_out.write(string_out)

        if end == 1:
            break

    f.close()

    # print('2' * 1000)


def reads():
    FileIn = open("16S_in", "r")
    FileOut = open("16S_reads", "w")
    strr = FileIn.read()
    buckets = [0] * 1575
    for k in range(0, 180):
        FileOut.write(">" + str(k))
        FileOut.write("\n")

        start = random.randint(0, 1328)
        FileOut.write(strr[start:(start + 250)].format('formatted'))
        for i in range(250):
            buckets[start + i] += 1

        FileOut.write("\n")

    print(buckets)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Singel_read250bp()
    # reads()



    temp_a=[0]*1791
    for i in range(0 , 1000):
        temp_a=np.add(read_cover_(30), temp_a)

    plt.plot(temp_a)
    plt.title("Coverage Method 1")
    plt.show()



