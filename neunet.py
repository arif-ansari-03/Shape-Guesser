import numpy

class Layer:

    def __init__(self, Num_nodes, Num_in_nodes, Weights, Biases):
        self.numNodes = Num_nodes               #number of nodes in output
        self.numInNodes = Num_in_nodes          #number of incoming nodes
        self.weights = Weights
        self.biases = Biases

    # def __init__(self, arr):
    #     self.numNodes = arr[0]               
    #     self.numInNodes = arr[1]           
    #     self.weights = arr[2] 
    #     self.biases = arr[3] 

    def calc_out( self, inLayer ):
        outLayer = numpy.matmul(self.weights, inLayer)
        for i in range(self.numNodes):
            outLayer[i] += self.biases[i]
            outLayer[i] = 1/(1 + numpy.exp(-outLayer[i]))

        return outLayer
    
    def calcZ( self, inLayer ):

        outLayer = numpy.matmul(self.weights, inLayer)
        for i in range(self.numNodes):
            outLayer[i] += self.biases[i]

        return outLayer
    
class Network:

    def __init__(self, NumLayers = 0, Layers = []):
        self.numLayers = NumLayers #does not include input layer
        self.layers = Layers #does not include input layer

    def activationFunction(self, z):
        return 1 / (1 + numpy.exp(-z))

    def lastLayer(self):
        return self.Layers[self.numLayers-1]
    
    def calcLayers(self, inArray):
        calc_layers = []
        outArray = inArray.copy()

        for i in range(self.numLayers):
            outArray = self.layers[i].calcZ(outArray)
            calc_layers.append(outArray.copy())
            outArray = [self.activationFunction(x) for x in outArray]

        return calc_layers

    def calc_out( self , inArray ):
        outArray = [x for x in inArray]
        for i in range(self.numLayers):
            outArray = self.layers[i].calc_out( outArray )

        return outArray             # The final output of the neural network

    
    def readWeights(self, address):
        
        with open(address, 'r') as file:
            reader = file.read()

        reader = str(reader)
        reader = reader.replace('\n', ' ')
        reader = reader.split()
        print(len(reader))

        i = 0
        reader = [float(x) for x in reader if x != '\n' and x != ' ']
        N = int(reader[i])
        layers = []
        i += 1

        for k in range(1, N+1):
            m = int(reader[i])
            i+=1
            n = int(reader[i])
            i+=1

            weights = numpy.zeros((m, n), dtype = 'f')
            biases = numpy.zeros((m,), dtype = 'f')

            for r in range(m):
                for c in range(n):
                    weights[r][c] = float(reader[i])
                    i+=1

            for r in range(m):
                biases[r] = float(reader[i])
                i+=1

            layers.append(Layer(m, n, weights, biases))

        self.layers = layers
        self.numLayers = N

    def writeWeights(self, address):
        file = open(address, 'w')

        file.write(str(self.numLayers)+'\n')

        for layer in self.layers:
            file.write((str(len(layer.weights)) + " " + str(len(layer.weights[0])) + '\n'))
            t = ""
            for row in layer.weights:
                for x in row:
                    t += str(x) + " "
                file.write(t)
                file.write('\n')
                t = ""
            
            for i in layer.biases:
                file.write(str(i)+'\n')

        file.close()



    


