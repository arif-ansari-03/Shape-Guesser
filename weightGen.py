# a program to generate random weights
'''
0
70 x 70 = 19600

1
200

2
200

3
2
'''

import numpy

mult = 0.001

address = "out.txt"
file = open(address, 'w')

file.write("3\n")
file.write("200 19600\n")

weights = numpy.random.rand(200, 19600) * mult
biases = numpy.random.rand(200) * mult

for i in range(200):
    for j in range(19600):
        file.write(str(weights[i][j])+" ")
    file.write('\n')

for i in range(200):
    file.write(str(biases[i])+" ")
    file.write('\n')

weights = numpy.random.rand(200, 200) * mult
biases = numpy.random.rand(200) * mult

file.write("200 200\n")

for i in range(200):
    for j in range(200):
        file.write(str(weights[i][j])+" ")
    file.write('\n')

for i in range(200):
    file.write(str(biases[i]))
    file.write('\n')

weights = numpy.random.rand(4, 200) * mult
biases = numpy.random.rand(4) * mult

file.write("4 200\n")

for i in range(4):
    for j in range(200):
        file.write(str(weights[i][j])+" ")
    file.write('\n')

for i in range(4):
    file.write(str(biases[i]))
    file.write('\n')

file.close()