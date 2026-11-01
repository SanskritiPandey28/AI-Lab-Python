import numpy as np

# -----------------------------
# 1. Training data
# -----------------------------
X = np.array([
    [2, 60],
    [3, 65],
    [4, 70],
    [5, 75],
    [6, 80],
    [7, 85],
    [8, 90],
    [9, 95]
], dtype=float)

y = np.array([0, 0, 0, 1, 1, 1, 1, 1], dtype=float)

# -----------------------------
# 2. Initialize parameters
# -----------------------------
theta0 = 0.0
theta1 = 0.0
theta2 = 0.0

learning_rate = 0.01
iterations = 1000

m = len(y)

# -----------------------------
# 3. Sigmoid function
# -----------------------------
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# -----------------------------
# 4. Gradient Descent
# -----------------------------
for i in range(iterations):

    # Calculate z
    z = theta0 + theta1 * X[:, 0] + theta2 * X[:, 1]

    # Calculate prediction
    y_pred = sigmoid(z)

    # Calculate gradients
    dtheta0 = (1/m) * np.sum(y_pred - y)

    dtheta1 = (1/m) * np.sum((y_pred - y) * X[:, 0])

    dtheta2 = (1/m) * np.sum((y_pred - y) * X[:, 1])

    # Update parameters
    theta0 = theta0 - learning_rate * dtheta0
    theta1 = theta1 - learning_rate * dtheta1
    theta2 = theta2 - learning_rate * dtheta2

# -----------------------------
# 5. Print learned parameters
# -----------------------------
print("Theta 0:", theta0)
print("Theta 1:", theta1)
print("Theta 2:", theta2)

# -----------------------------
# 6. Predict for new student
# -----------------------------
x1 = 6
x2 = 78

z = theta0 + theta1 * x1 + theta2 * x2

probability = sigmoid(z)

print("Probability of passing:", probability)

# -----------------------------
# 7. Apply threshold
# -----------------------------
if probability >= 0.5:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")