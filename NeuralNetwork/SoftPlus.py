import numpy as np
import matplotlib.pyplot as plt

def softplus(x):
    return np.log(1 + np.exp(x))

def neural_network(inputs):
    # Weights and biases for the hidden layer
    weights_hidden = np.array([[0.5, -0.3], [0.8, 0.2]])
    biases_hidden = np.array([0.2, -0.1])

    # Weights and biases for the output layer
    weights_output = np.array([0.6, 0.4])
    bias_output = 0.1

    # Calculate values for the hidden layer
    hidden_layer_values = softplus(np.dot(inputs, weights_hidden) + biases_hidden)

    # Calculate the output of the neural network
    output = softplus(np.dot(hidden_layer_values, weights_output) + bias_output)

    return output

# Example usage
inputs = np.array([0.5, -0.2])  # Replace with your desired input values
result = neural_network(inputs)
print("Output:", result)



# Given points
points = np.array([[1, 0], [2, 4], [4, 8], [6, 10]])

# Model parameters
a = 1.0
b = 1.0
c = 1.0

# Learning rate
learning_rate = 0.01

# Number of iterations
epochs = 1000

# Gradient Descent
for epoch in range(epochs):
    gradients_a = 2 * np.sum((a * points[:, 0]**2 + b * points[:, 0] + c - points[:, 1]) * points[:, 0])
    gradients_b = 2 * np.sum(a * points[:, 0]**2 + b * points[:, 0] + c - points[:, 1])
    gradients_c = 2 * np.sum(a * points[:, 0]**2 + b * points[:, 0] + c - points[:, 1])

    a -= learning_rate * gradients_a
    b -= learning_rate * gradients_b
    c -= learning_rate * gradients_c

# Plotting the data points and the fitted curve
x_values = np.linspace(0, 7, 100)
y_values = a * x_values**2 + b * x_values + c

plt.scatter(points[:, 0], points[:, 1], label='Data Points')
plt.plot(x_values, y_values, color='red', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

print(f"Fitted Curve: Y = {a:.2f}X^2 + {b:.2f}X + {c:.2f}")
