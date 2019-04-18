import numpy as np
from numpy import dot
from numpy.linalg import norm
from sklearn import preprocessing

#
# def getCosineSimilarity(x1, x2):
#     cos_sim = dot(x1, x2) / (norm(x1) * norm(x2))
#     return cos_sim
#
#
# mat = [[3, 1, 2, 4, 5], [6, 21, -2, 4, 8], [9, 1, 2, 0, 5], [-3, 1, -2, 4, 5]]
# mat = np.array(mat)
#
# simMat = np.zeros((len(mat), len(mat)))
#
# for i in range(0, len(mat)):
#     for j in range(0, len(mat)):
#         simMat[i][j] = getCosineSimilarity(mat[i], mat[j])
#
# print(simMat)
#
# mat = preprocessing.normalize(mat)
#
# print(np.mat(mat) * np.mat(mat).T)
#
#
#
# ls = [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   4,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0, 103, 190, 155, 124, 233, 137,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0, 134, 255, 253, 255, 253, 252, 205,
#        154,  23,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0, 192, 255, 255, 154,  37,
#        226, 255, 255, 105,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   6, 209, 223,
#          7,   0,  49, 234, 227,  23,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 111,
#        255,  89,   0,   1, 174, 248,  56,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#         44, 247, 169,   0,   0, 118, 255, 103,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   7, 208, 227,  18,   0,  14, 241, 168,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   3,   0,   0,   0,   0,   0,
#          0,   0,   0, 139, 253,  67,   0,   0, 111, 254,  45,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,  91, 199, 254, 225,  68,   0,
#          0,   0,   0,   0,  87, 253, 140,   0,   0,   3, 221, 188,   0,
#          0,   0,   0,   0,   0,   0,   0,  17, 169, 255, 203, 127, 204,
#        253, 128,   2,   0,  20, 158, 255, 191,   7,   0,   0,  81, 255,
#         75,   0,   0,   0,   0,   0,   0,   0, 203, 243, 248, 112,   1,
#          0,   7, 150, 255, 241, 238, 252, 250, 123,   3,   0,   0,   0,
#        194, 216,   2,   0,   0,   0,   0,   0,   0,   0,  84, 168,  46,
#          0,   0,   0,   0,   0,  80, 136, 136, 117,  38,   0,   0,   0,
#          0,  81, 255, 105,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,  38, 240, 197,   5,   0,   0,   0,   0,   0,   0,   0,
#          2,  33,  34,  34,  34,  21,  17,  17,   5,   0,   0,   0,   0,
#          0,   0,   0,  70, 226, 229,  23,   0,   0,   0,   0,   0,   0,
#          0,   0, 100, 255, 255, 255, 255, 255, 255, 255, 251, 217, 177,
#        138, 106, 102, 118, 194, 254, 208,  43,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,  13,  82,  85,  85,  94, 102, 102, 102, 123,
#        163, 202, 240, 255, 255, 254, 201, 112,   5,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,  16,  17,  12,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#          0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
#    


a = []
for i in range(10000):
    a.append(np.random.randint(-256, 256, 784))
a = np.array(a)


np.savetxt('data.txt', a)