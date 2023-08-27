import neunet

class Trainer:
    def __init__(self, network):
        self.network = network

    def cost_grad(self, expected_output): # gradient for the last layer
        node_values = [cost(expected_output[x], self.lastLayer[x]) for x in range(self.lastLayer.)]            

    def calc_grad(expected_output):
        

    def upd_grad(gradient):

    
        