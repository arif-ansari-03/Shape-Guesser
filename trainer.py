import neunet
import numpy

class Trainer:
    def __init__(self, network):
        self.network = network #assuming pass by reference. In case it isn't, the network in main.py can be reset to Trainer.network

    def cost(a, e):
        return (a - e)*(a - e)
    
    def costDerivative(a, e):
        return 2 * (a - e)
    
    def activationFunction(z):
        return 1 / (1 + numpy.exp(-z))
    
    def activationDerivative(z):
        a = 1 / (1 + numpy.exp(-z))
        return a - a*a

    def calc_grad(self, expected_output):
        calcZ = self.network.calcLayers() # z values
        calcA = [[self.activationFunction(x) for x in Layer] for Layer in calcZ] # a values, a = activationFunction(z)

        NV = [[self.cost(calcA[-1][i], expected_output[i]) for i in range(len(calcA[-1]))]]


        

    def upd_grad(gradient):

    
        