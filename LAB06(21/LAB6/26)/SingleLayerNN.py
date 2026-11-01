import numpy as np

# Input data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Target output for AND gate
y = np.array([0, 0, 0, 1])

# Initialize weights and bias
weights = np.zeros(2)
bias = 0

# Learning rate
learning_rate = 0.1

# Number of epochs
epochs = 10


# Step activation function
def activation(z):
    if z >= 0:
        return 1
    else:
        return 0


# Training the neural network
for epoch in range(epochs):

    print("Epoch:", epoch + 1)

    for i in range(len(X)):

        # Calculate weighted sum
        z = np.dot(X[i], weights) + bias

        # Predict output
        prediction = activation(z)

        # Calculate error
        error = y[i] - prediction

        # Update weights
        weights = weights + learning_rate * error * X[i]

        # Update bias
        bias = bias + learning_rate * error

    print("Weights:", weights)
    print("Bias:", bias)


# Testing
print("\nFinal Predictions:")

for i in range(len(X)):

    z = np.dot(X[i], weights) + bias

    prediction = activation(z)

    print(
        "Input:", X[i],
        "Actual:", y[i],
        "Predicted:", prediction
    )