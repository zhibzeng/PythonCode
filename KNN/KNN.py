__author__ = 'JeffreyTseng'
from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1], [0.01, 0.01], [1.0, 1.11]])
    labels = ['A', 'B', 'C', 'D', 'C', 'A']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def File2Matrix(filename):
    fileOpen = open(filename)
    fileOnLines = fileOpen.readlines()
    lines = len(fileOnLines)
    returnMat = zeros((lines, 3)) #Create a lines X 3 matrix
    labelsVector = []
    index = 0
    for line in fileOnLines:
        line = line.strip()
        dataList = line.split('\t')
        returnMat[index, :] = dataList[0:3]
        labelsVector.append(int(dataList[-1]))
        index += 1
    return returnMat, labelsVector


def autoNum(dataset):
    minValue = dataset.min()
    maxValue = dataset.max()
    ranges = maxValue - minValue
    normDataset = zeros(shape(dataset))
    rows = dataset.shape[0]
    normDataset = dataset - tile(minValue, (rows, 1))
    normDataset = normDataset / tile(ranges, (rows, 1))
    return normDataset, ranges, minValue




def main():
    # group, labels = createDataSet()
    # print(group)
    # print(labels)
    # result = classify0([0, 0], group, labels, 3)
    # print('result='+result)
    returnMat, labelVector = File2Matrix('datingTestSet2.txt')
    norMat, ranges, minValues = autoNum(returnMat)
    print(norMat[0, :])
    import matplotlib
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(returnMat[:, 1], returnMat[:, 2], 15.0*array(labelVector), 15.0*array(labelVector))
    plt.show()




if __name__ == "__main__":
    main()


