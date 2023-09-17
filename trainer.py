import neunet
import numpy
import matplotlib.pyplot as plt
import pylab
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
    
    def updateGrad(self, input, calcA, nodeVals, GW, GB):
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

        for i in range(len(GW)):
            GW[i] = numpy.add(GW[i], weightGrad[i])

        for i in range(len(GB)):
            GB[i] = numpy.add(GB[i], weightGrad[i])

        print(biasGrad)     
        print(weightGrad)   


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
        GW = []
        GB = []
        for layer in self.network.Layers:
            GW.append(zeros(len(layer.weights), len(layer.weights[0])))
            GB.append(zeros(len(layer.biases), len(layer.biases[0])))

        # for loop goes through images, calculates gradients and adds them onto gw and gb
        address = []
        for i in range(10):
            self.Img.update(address[i])
            grad(self.Img.imageArray, output[i], GW, GB)

        for i in range(len(self.network.Layers)):
            Layers[i].weights = numpy.add(Layers[i].weights, GW[i])
            Layers[i].biases = numpy.add(Layers[i].biases, GB[i])

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

# I = ImageReader()
# I.update("ellipse.u01.0001.png")


# print(I.imageGrid)
# print(N.calc_out(I.imageGrid.flatten()))

# N = neunet.Network()
# N.readWeights("out.txt")

# print(N.calc_out([2, 1]))

# calcZ = N.calcLayers([1, 3]) # z values, sigmoid of z values is given to the next layer as input
# calcA = [[N.activationFunction(x) for x in y] for y in calcZ] # a values, a = activationFunction(z)
        
# print(calcZ)
# print()
# print(calcA)



    
        