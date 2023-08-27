import numpy

class Layer:

    def __init__(self, Num_nodes, Num_in_nodes, Weights, Biases):
        self.numNodes = Num_nodes               #number of nodes in output
        self.numInNodes = Num_in_nodes          #number of incoming nodes
        self.weights = Weights
        self.biases = Biases

    def calc_out( self, inLayer ):
        outLayer = numpy.matmul(self.weights, inLayer)
        for i in range(self.numNodes):
            outLayer[i] += self.biases[i]
            outLayer[i] = 1/(1 + numpy.exp(-outLayer[i]))

        return outLayer
    
class Network:

    def __init__(self, NumLayers, Layers):
        self.numLayers = NumLayers #does not include input layer
        self.layers = Layers #does not include input layer

    def lastLayer(self)
        return self.Layers[self.numLayers-1]
    
    def calcLayers(self, inArray):
        self.calc_layers = {}

        for ()

    def calc_out( self , inArray ):
        outArray = [x for x in inArray]
        for i in range(self.numLayers):
            outArray = self.layers[i].calc_out( outArray )

        return outArray             # The final output of the neural network
    


