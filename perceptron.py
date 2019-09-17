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
        x_u = x_u.insert(0,1)
        return self.__sign(sum(self.weights*x_u))

    def fit(self, x, t):
        if len(x[0]) != self.dim:
            print('Error: dimensions of input ({}) do not match to dimensions of Perceptron ({})'.format(len(x[0]), self.dim))

        for i in range(len(x)):
            x[i] = x[i].insert(0,1) # Add 1 at zero position of input so weight_0 can be included in sum

        M = [0] * len(x)
        z = x * t
        M_old = []
        while M_old != M:
            M_old = M
            for i in range(self.dim):
                if self.weights*z[i]<0:
                    self.__update_weights(z[i])
                    M[i] += 1

    def __update_weights(self, z_i):
        self.weights += self.learning_rate * z_i

    def __sign(self, a):
        if a >=0:
            return 1
        else:
            return -1
