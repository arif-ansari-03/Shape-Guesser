import neunet
import numpy
import matplotlib.pyplot as plt
import pylab
import os
from PIL import Image

class Trainer:
    def __init__(self, network):
        self.network = network # the network is passed by reference

    ''' ==== CALCULATION FUNCTIONS ==== '''
    def cost(self, a, e):
        return (a - e)*(a - e)
    
    def costDerivative(self, a, e):
        return 2 * (a - e)
    
    def activationDerivative(self, z):
        a = 1 / (1 + numpy.exp(-z))
        return a * (1 - a)
    
    def updateGrad(self, input, calcA, nodeVals):
        weightGrad = []
        biasGrad = []

        temp = []
        for i in range(len(nodeVals[0])):
            temp.append([nodeVals[0][i] * inp for inp in input])
        weightGrad.append(temp)

        for i in range(1, len(nodeVals)):
            temp = []

            for j in range(len(nodeVals[i])):
                temp.append([nodeVals[i][j] * a for a in calcA[i-1]])

            weightGrad.append(temp)
        biasGrad = nodeVals

        for i in range(len(self.GW)):
            self.GW[i] = numpy.add(self.GW[i], weightGrad[i])

        for i in range(len(self.GB)):
            self.GB[i] = numpy.add(self.GB[i], biasGrad[i])  


    def calcNodeVals(self, calcA, calcZ, expectedOutput): #calculates the reptitive factor in gradient
        n = self.network.numLayers
        nodeVals = list(n*'a')

        nodeVals[n-1] = [self.activationDerivative(calcZ[n-1][i])*self.costDerivative(calcA[n-1][i], expectedOutput[i]) for i in range(len(expectedOutput))]
        

        for i in range(n-2, -1, -1):
            temp = [0 for x in range(len(calcA[i]))]

            a = len(nodeVals[i+1])
            b = len(temp)

            for j in range(a):
                for k in range(b):
                    temp[k] += self.network.layers[i+1].weights[j][k] * nodeVals[i+1][j]

            for k in range(b):
                temp[k] *= self.activationDerivative(calcZ[i][k])

            nodeVals[i] = temp

        return nodeVals         


    def grad(self, input, expectedOutput):
        calcZ = self.network.calcLayers(input) # z values, sigmoid of z values is given to the next layer as input
        calcA = [[self.network.activationFunction(x) for x in y] for y in calcZ] # a values, a = activationFunction(z)
        
        nodeVals = self.calcNodeVals(calcA, calcZ, expectedOutput)

        self.updateGrad(input, calcA, nodeVals)



    ''' ==== SAMPLE INTERACTION FUNCTIONS ==== '''    

    def sampleGrad(self):           # to find and update gradient of a sample
        self.Img = ImageReader()    # a lot of sampleGrad() is not fully implemented yet

        n = self.network.numLayers 
        self.GW = []
        self.GB = []
        for l in self.network.layers:
            self.GW.append(numpy.zeros((len(l.weights), len(l.weights[0]))))
            self.GB.append(numpy.zeros((len(l.biases),)))

        self.Img.update("ellipse.u01.0001.png")
        self.grad(self.Img.imageArray, [0, 1, 0, 0])

        for i in range(len(self.GW)):
            N.layers[i].weights = numpy.add(N.layers[i].weights, self.GW[i] * (-0.1))

        for i in range(len(self.GB)):
            N.layers[i].biases = numpy.add(N.layers[i].biases, self.GB[i] * (-0.1)) 

    '''  === Output resulting weights === '''

    def writeWeigts(self, address):
        self.network.writeWeights(address)



class ImageReader:
    def __init__(self):
        pass

    def update(self, address):
        self.image = Image.open(address)
        self.imageGrid = numpy.asarray(self.image)
        self.imageArray = numpy.ndarray.flatten(self.imageGrid) 

    def close(self):
        self.image.close() 

    def display(self):
        plt.imshow(self.imageGrid)
        plt.show()


I = ImageReader()
I.update("ellipse.u01.0001.png")

N = neunet.Network()
N.readWeights("out.txt")

print(N.calc_out(I.imageArray))
T = Trainer(N)

for i in range(1000):
    T.sampleGrad()
    if i % 100 == 0:
        print(N.calc_out(I.imageArray))

N.writeWeights("out2.txt")

# print(os.listdir())
# print(os.getcwd())
# os.chdir("dataset\\data")
# print(os.getcwd())
# print(os.listdir())
        