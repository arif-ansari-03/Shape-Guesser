import neunet
import numpy

class Trainer:
    def __init__(self, network):
        self.network = network # the network is passed by reference

    def cost(a, e):
        return (a - e)*(a - e)
    
    def costDerivative(a, e):
        return 2 * (a - e)
    
    def activationDerivative(z):
        a = 1 / (1 + numpy.exp(-z))
        return a - a*a

    def calc_grad(self, input, expected_output):
        calcZ = self.network.calcLayers(input) # z values, sigmoid of z values is given to the next layer as input
        calcA = [[[self.network.activationFunction(x[0]) for x in y]] for y in calcZ] # a values, a = activationFunction(z)


Layers = [ [2, 2, [[1, 2], [3, 3]], [0, 0]],
           [2, 2, [[0, 0], [0, 0]], [1, 1]],
           [2, 2, [[0, 3], [3, 1]], [1, 0]] ]
        
N1 = neunet.Network(len(Layers), [neunet.Layer(Layers[x]) for x in range(len(Layers))])
T1 = Trainer(N1)

T1.calc_grad([[2], [3]], [[3], [4]])



    
        