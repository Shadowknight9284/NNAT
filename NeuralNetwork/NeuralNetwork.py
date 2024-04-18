import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np
import pandas as pd

# Code in functions
def softplus(x, weights, biases):
    return np.log(1 + np.exp(np.dot(x, weights) + biases))
def sigmoid(x, weights, biases):
    return np.exp(np.dot(x, weights) + biases)/(1+np.exp(np.dot(x, weights) + biases))
def linear(x, weights, biases):
    return np.dot(x, weights) + biases
def relu(x, weights, biases):
    return np.maximum(0, np.dot(x, weights) + biases)
def derivativeSoftplus(x, weights, biases):
    return 1/(1+np.exp(-np.dot(x, weights) + biases))
def derivativeSigmoid(x, weights, biases):
    return np.exp(np.dot(x, weights) + biases)/(1+np.exp(np.dot(x, weights) + biases))**2
def derivativeLinear(x, weights, biases):
    return weights
def derivativeRelu(x, weights, biases):
    return np.where(np.dot(x, weights) + biases > 0, 1, 0)



# code in a method for make layers and nodes
# Idea is to make a node function that includes the function, weights and biases, and the list of next layer nodes

# make idea for one layer and one node
