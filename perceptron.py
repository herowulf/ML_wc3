import numpy as np

class Perceptron():
    def __init__(self, dim):
        self.dim = dim
        self.weights = self.__initialize_weights(self.dim)
        self.learning_rate = 1

    def __initialize_weights(self, dim):
        weights = np.random.random(dim+1)
        return weights

    def predict(self, x_u):
        return self.__sign(np.sum(self.weights[1:]*x_u) + self.weights[0])

    def fit(self, x, t):
        if len(x[0]) != self.dim:
            print('Error: dimensions of input ({}) do not match to dimensions of Perceptron ({})'.format(len(x[0]), self.dim))
        z = x * t
        finished_fit = False
        while !finished_fit:
            for i in range(self.dim):
                
        pass

    def __update_weights(self):
        pass

    def __sign(self, a):
        if a >=0:
            return 1
        else:
            return -1
