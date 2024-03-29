""" jm8wx 7/15/2019 """

import numpy as np

class Network():
    """ A basic MLP. 
    
        The list `layer_sizes` is a list of the number of neurons in each layer.
        It includes the input and output layers. """
    def __init__(self, layer_sizes):
        self.num_layers = len(layer_sizes)
        self.layer_sizes = layer_sizes
        # Initialize a bias for each neuron
        self.biases = [np.random.randn(y, 1) for y in layer_sizes[1:]]
        # Initialize a weight for every possible connection between layers,
            # since this is a feedforward network
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
        
        
    def feedforward(self, a):
        """ Runs a through the network and returns the output of the final layer. """
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(a, w) + b)
        return a
    
    def SGD(self, training_data, epochs=10, mini_batch_size=10, eta=0.5, test_data=None):
        """ Trains the neural network using mini-batch stochastic gradient descent.
        
            The `training_data` is a list of tuples `(x, y)` represent training inputs
            and their corresponding labels. 
            
            If `test_data` is provided then the network will be evaluated against the
            test data at the end of each epoch, and progress will be printed out. This
            is useful but slows the training process. """
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for epoch in range(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)
            ]
            
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            
            if test_data:
                print('Epoch {}: {} / {}'.format(j, self.evaluate(test_data), n_test))
            else:
                print('Epoch {} complete.'.format(j))
    
    def update_mini_batch(self, mini_batch, eta):
        """ Apply gradient descent for a single mini_batch and update internal
            weights and biases.
            
            The `mini_batch` is a list of tuples `(x, y)` and `eta` is the 
            learning rate. """
        
        nabla_b = [np.zeros(b.shape) for b in self.biases)]
        nabla_w = [np.zeros(w.shape) for w in self.weights)]
        
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
            
        self.weights = [w-(eta/len(mini_batch))*nw for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb for b, nb in zip(self.biases, nabla_b)]
    
    def backprop(self, x, y):
        """ @todo """
        return
    
    def evaluate(self, test_data):
        """ Return the number of inputs for which the neural network outputs
            the correct result. """
        
        test_results = [(np.argmax(self.feedforward(x)), y) for (x,y) in test_data]
        
        return sum(int(x == y) for (x, y) in test_results)

def sigmoid(z):
    """ The sigmoid function. """
    return 1.0 / (1.0 + np.exp(-z))