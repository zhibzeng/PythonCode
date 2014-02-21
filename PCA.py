__author__ = 'I304905'
import matplotlib as plt
from numpy import *


def pca(data, nRedDim=0, normalise=1):
     # 数据标准化
    m = mean(data, axis=0)
    data -= m
    # 协方差矩阵
    C = cov(transpose(data))
    # 计算特征值特征向量，按降序排序
    evals, evecs = linalg.eig(C)
    indices = argsort(evals)
    indices = indices[::-1]
    evecs = evecs[:, indices]
    evals = evals[indices]
    if nRedDim > 0:
        evecs = evecs[:, :nRedDim]

    if normalise:
        for i in range(shape(evecs)[1]):
            evecs[:, i] / linalg.norm(evecs[:, i]) * sqrt(evals[i])
    # 产生新的数据矩阵
    x = dot(transpose(evecs), transpose(data))
    # 重新计算原数据
    y = transpose(dot(evecs, x))+m
    return x, y, evals, evecs


def execute():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = random.normal(5, .5, 1000)
    y = random.normal(3, 1, 1000)
    a = x*cos(pi/4) + y*sin(pi/4)
    b = -x*sin(pi/4) + y*cos(pi/4)
    plt.plot(a, b, '.')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('原数据集')
    data = zeros((1000, 2))
    data[:, 0] = a
    data[:, 1] = b
    x, y, evals, evecs = pca(data, 1)
    print(y)
    plt.figure()
    plt.plot(y[:, 0], y[:, 1], '.')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('重新构造数据')
    plt.show()


def __main__():
    execute()


