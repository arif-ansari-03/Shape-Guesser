import neunet
import numpy

class Trainer:
    def __init__(self, network):
        self.network = network # the network is passed by reference

    def cost(self, a, e):
        return (a - e)*(a - e)
    
    def costDerivative(self, a, e):
        return 2 * (a - e)
    
    def activationDerivative(self, z):
        a = 1 / (1 + numpy.exp(-z))
        return a * (1 - a)
    
    def layerGrad(self, input, calcA, nodeVals):
        weightGrad = []
        biasGrad = []

        temp = []
        for i in range(len(nodeVals[0])):
            temp.append([nodeVals[0][i][0] * inp[0] for inp in input])
        weightGrad.append(temp)

        for i in range(1, len(nodeVals)):
            temp = []

            for j in range(len(nodeVals[i])):
                temp.append([nodeVals[i][j][0] * a[0] for a in calcA[i-1]])

            weightGrad.append(temp)
        biasGrad = nodeVals

        print(biasGrad)     # this cost and weight gradient is for a single input, however we have to calc
        print(weightGrad)   # this for all the inputs and add to an overall biad and weight grad (TODO)


    def calcNodeVals(self, calcA, calcZ, expectedOutput):
        n = self.network.numLayers
        nodeVals = list(n*'a')

        nodeVals[n-1] = [[self.activationDerivative(calcZ[n-1][i][0])*self.costDerivative(calcA[n-1][i][0], expectedOutput[i][0])] for i in range(len(expectedOutput))]
        

        for i in range(n-2, -1, -1):
            temp = [[0] for x in range(len(calcA[i]))]

            a = len(nodeVals[i+1])
            b = len(temp)

            for j in range(a):
                for k in range(b):
                    temp[k][0] += self.network.layers[i+1].weights[j][k] * nodeVals[i+1][j][0]

            for k in range(b):
                temp[k][0] *= self.activationDerivative(calcZ[i][k][0])

            nodeVals[i] = temp

        return nodeVals         


    def grad(self, input, expectedOutput):
        calcZ = self.network.calcLayers(input) # z values, sigmoid of z values is given to the next layer as input
        calcA = [[[self.network.activationFunction(x[0])] for x in y] for y in calcZ] # a values, a = activationFunction(z)

        nodeVals = self.calcNodeVals(calcA, calcZ, expectedOutput)

        self.layerGrad(input, calcA, nodeVals)


Layers = [ [2, 2, [[1, 2], [3, 3]], [0, 0]],
           [2, 2, [[0, 0], [0, 0]], [1, 1]],
           [2, 2, [[0, 3], [3, 1]], [1, 0]] ]
        
N1 = neunet.Network(len(Layers), [neunet.Layer(Layers[x]) for x in range(len(Layers))])
T1 = Trainer(N1)

T1.grad([[1], [1]], [[0.9], [0.9]])



    
        