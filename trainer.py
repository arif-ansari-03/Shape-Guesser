import neunet

biases = [[0.0, 1.0], [0.0, 0.0], [0.0, 0.0]]
weights = [[[1.0, 0.0], [0.0, 1.0]], [[1.0, 0.0], [0.0, 1.0]], [[0.0, 0.0], [0.0, 0.0]]]

Layers = [neunet.Layer(2, 2, weights[i], biases[i]) for i in range(3)]
myNet = neunet.Network(3, Layers)

inLayer = [0.0, 0.0]
outLayer = myNet.calc_out(inLayer)
print(inLayer)
print(outLayer)