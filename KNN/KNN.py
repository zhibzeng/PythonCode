__author__ = 'JeffreyTseng'
from numpy import *
import operator
import matplotlib as mpl


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'B', 'C', 'D']
    return group, labels


def main():
    group, label = createDataSet()
    print(group)
    print(label)


if __name__ == "__main__":
    main()


