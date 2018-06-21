import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--method', required=False, default='both', help='input method')
params = parser.parse_args()


def loaddata(fileName):
    f = open(fileName)
    start = f.readline()
    data = f.readline()
    return start, data


def loadNext(now, next):
    length = abs(int(now) - int(next))
    print(next, length)
    return length,next



def findNextIndex_SSTF(start,datas):
    length = []
    for data in datas:
        l = abs(int(start) - int(data))
        length.append(l)
    minIndex = length.index(min(length))
    return minIndex



def findNext_SCAN(now,data):
    biggerList = []
    smallerList = []
    for d in data:
        if int(d) > int(now):
            biggerList.append(d)
    if (len(biggerList)==0):
        if len(data)!=0:
            for d2 in data:
                if int(d2)<int(now):
                    smallerList.append(d2)
            return max(smallerList)
        else:
            return None
    return min(biggerList)



if __name__=="__main__":
    l = 0
    start, data = loaddata('data')
    n = len(data.split())
    X = np.zeros(n)
    N = np.zeros(n)
    Move = np.zeros(n)

    m = params.method
    if m == 'SSTF':

        data2 = data.split().copy()
        n = len(data2)
        i = 0
        for d in data.split():

            nextIndex = findNextIndex_SSTF(start, data2)
            ll,nn = loadNext(start, data2[nextIndex])
            l += ll
            N[i] = nn
            X[i] = i
            Move[i] = ll
            i+=1
            start = data2[nextIndex]
            data2.remove(data2[nextIndex])

        fig = plt.figure()
        plt.bar(X, N, 0.4, color="green")
        plt.xlabel("次数")
        plt.ylabel("序列")

        plt.show()
        plt.waitforbuttonpress()
        plt.close()
        print("SSTF方式:平均寻道长度：%.1f" % (l / n))


    elif m =='SCAN':
        data2 = data.split().copy()
        i = 0
        for d in data:
            next = findNext_SCAN(start, data2)
            if next == None:
                break
            ll,nn= loadNext(start, next)
            l+=ll
            N[i] = nn
            X[i] = i
            Move[i] = ll
            i += 1
            start = next
            data2.remove(next)
        fig = plt.figure()
        plt.bar(X, N, 0.4, color="green")
        plt.xlabel("次数")
        plt.ylabel("序列")

        plt.show()
        plt.waitforbuttonpress()
        plt.close()
        print("SCAN方式:平均寻道长度：%.1f" % (l / n))

    elif m=='both':
        data2 = data.split().copy()
        n = len(data2)
        i = 0
        for d in data.split():
            nextIndex = findNextIndex_SSTF(start, data2)
            ll, nn = loadNext(start, data2[nextIndex])
            l += ll
            N[i] = nn
            X[i] = i
            Move[i] = ll
            i += 1
            start = data2[nextIndex]
            data2.remove(data2[nextIndex])

        fig = plt.figure()
        plt.bar(X, N, 0.4, color="green")
        plt.xlabel("次数")
        plt.ylabel("序列")
        plt.title("SSTF方式:平均寻道长度：%.1f" % (l / n))
        plt.show()
        plt.waitforbuttonpress()
        plt.close()
        print("SSTF方式:平均寻道长度：%.1f" % (l / n))

        i = 0
        data2 = data.split().copy()
        for d in data:
            next = findNext_SCAN(start, data2)
            if next == None:
                break
            ll, nn = loadNext(start, next)
            l += ll
            N[i] = nn
            X[i] = i
            Move[i] = ll
            i += 1
            start = next
            data2.remove(next)
        fig = plt.figure()
        plt.bar(X, N, 0.4, color="green")
        plt.xlabel("次数")
        plt.ylabel("序列")
        plt.title("SCAN方式:平均寻道长度：%.1f" % (l / n))
        plt.show()
        plt.waitforbuttonpress()
        plt.close()
        print("SCAN方式:平均寻道长度：%.1f" % (l / n))



