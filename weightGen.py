# a program to generate random weights
'''
0
70 x 70 = 19600 k1

1
20 k2

2
20 k3

3
4 k4
'''

# add negative weights and biases as well 

k1 = 19600
k2 = 2
k3 = 2
k4 = 4

import numpy

mult = 0.00001
mult2 = 1

address = "out.txt"
file = open(address, 'w')

file.write("3\n")
file.write(str(k2)+" "+str(k1)+"\n")

weights = numpy.random.rand(k2, k1) * mult
biases = numpy.random.rand(k2) * 0.000005

for i in range(k2):
    for j in range(k1):
        file.write(str(weights[i][j])+" ")
    file.write('\n')

for i in range(k2):
    file.write(str(biases[i])+" ")
    file.write('\n')

weights = numpy.random.rand(k3, k2) * mult2
biases = numpy.random.rand(k3) * mult2

file.write(str(k3)+" "+str(k2)+"\n")

for i in range(k3):
    for j in range(k2):
        file.write(str(weights[i][j])+" ")
    file.write('\n')

for i in range(k3):
    file.write(str(biases[i]))
    file.write('\n')

weights = numpy.random.rand(k4, k3) * mult2
biases = numpy.random.rand(k4) * mult2

file.write(str(k4)+" "+str(k3)+"\n")

for i in range(k4):
    for j in range(k3):
        file.write(str(weights[i][j])+" ")
    file.write('\n')

for i in range(k4):
    file.write(str(biases[i]))
    file.write('\n')

file.close()