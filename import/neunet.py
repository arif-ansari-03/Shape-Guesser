class Param:
    def __init__(self, matrix, bias):
        self.weights = matrix
        self.biases = bias

    
class Layer:

    def __init__(self, column, param):
        self.column = column
        self.param = param

    def print(self):
        print(self.layer)
        print("\n")
        print(self.param.weights + "\n" + self.param.bias)