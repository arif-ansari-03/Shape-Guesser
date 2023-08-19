import numpy

class Layer:

    def __init__(self, Num_nodes, Num_in_nodes, Weights, Biases):
        self.numNodes = Num_nodes               #number of nodes in output
        self.numInNodes = Num_in_nodes          #number of incoming nodes
        self.weights = Weights
        self.biases = Biases

    def calc_out( inLayer ):
        outLayer = numpy.matmul(Layer.Weights, inLayer)
        for i in range(Layer.numNodes):
            outLayer[i] += Layer.Biases[i]
            outLayer[i] = 1/(1 + numpy.exp(-outLayer[i]))

        return outLayer
    
class Network:

    def __init__(self, NumLayers, Layers):
        self.numLayers = NumLayers
        self.layers = Layers

    def calc_out( inArray ):
        outArray = list(inArray)
        for i in range(Network.numLayers):
            outArray = Network.layers[i].calc_out( outArray )

        return outArray             # The final output of the neural network
    


