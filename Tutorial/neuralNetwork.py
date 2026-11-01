
import numpy as np


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


class NeuralNetwork:
    def __init__(
        self, input_size, hidden_size, output_size,
        learning_rate=0.01, seed=42
    ):
        rng = np.random.default_rng(seed)

        self.W1 = rng.normal(
            0, np.sqrt(2 / input_size),
            (input_size, hidden_size)
        )
        self.b1 = np.zeros((1, hidden_size))

        self.W2 = rng.normal(
            0, np.sqrt(1 / hidden_size),
            (hidden_size, output_size)
        )
        self.b2 = np.zeros((1, output_size))

        self.learning_rate = learning_rate
        self.loss_history = []

    def relu(self, z):
        return np.maximum(0, z)

    def softmax(self, z):
        z = z - np.max(z, axis=1, keepdims=True)
        exp_z = np.exp(z)
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)

    def forward(self, X):
        self.Z1 = X @ self.W1 + self.b1
        self.A1 = self.relu(self.Z1)

        self.Z2 = self.A1 @ self.W2 + self.b2
        self.A2 = self.softmax(self.Z2)

        return self.A2

    def fit(self, X, y, epochs=1000):
        m = X.shape[0]
        output_size = self.W2.shape[1]

        # One-hot encoding of the target classes
        Y = np.eye(output_size)[y]

        for epoch in range(epochs):
            probabilities = self.forward(X)

            eps = 1e-12
            loss = -np.mean(
                np.sum(Y * np.log(probabilities + eps), axis=1)
            )
            self.loss_history.append(loss)

            # Backpropagation: output layer
            dZ2 = (probabilities - Y) / m
            dW2 = self.A1.T @ dZ2
            db2 = np.sum(dZ2, axis=0, keepdims=True)

            # Backpropagation: hidden layer
            dA1 = dZ2 @ self.W2.T
            dZ1 = dA1 * (self.Z1 > 0)

            dW1 = X.T @ dZ1
            db1 = np.sum(dZ1, axis=0, keepdims=True)

            # Gradient descent updates
            self.W2 -= self.learning_rate * dW2
            self.b2 -= self.learning_rate * db2
            self.W1 -= self.learning_rate * dW1
            self.b1 -= self.learning_rate * db1

        return self

    def predict_proba(self, X):
        return self.forward(X)

    def predict(self, X):
        return np.argmax(self.predict_proba(X), axis=1)


def evaluate(model, X, y, title):
    predictions = model.predict(X)

    print("\n", title)
    print("Accuracy:", round(accuracy_score(y, predictions), 4))
    print("Precision:", round(
        precision_score(
            y, predictions, average="macro", zero_division=0
        ), 4
    ))
    print("Recall:", round(
        recall_score(
            y, predictions, average="macro", zero_division=0
        ), 4
    ))
    print("F1-score:", round(
        f1_score(
            y, predictions, average="macro", zero_division=0
        ), 4
    ))
    print("Confusion matrix:\n", confusion_matrix(y, predictions))


def main():
    data = load_iris()
    X, y = data.data, data.target

    X_train_full, X_test, y_train_full, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Hold out part of training data for validation
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_full, y_train_full,
        test_size=0.2,
        random_state=42,
        stratify=y_train_full
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_val = scaler.transform(X_val)
    X_test = scaler.transform(X_test)

    configurations = [
        {"hidden_size": 8, "learning_rate": 0.01, "epochs": 1000},
        {"hidden_size": 16, "learning_rate": 0.01, "epochs": 1000}
    ]

    for index, config in enumerate(configurations, start=1):
        model = NeuralNetwork(
            input_size=X_train.shape[1],
            hidden_size=config["hidden_size"],
            output_size=3,
            learning_rate=config["learning_rate"],
            seed=42
        )

        model.fit(
            X_train, y_train,
            epochs=config["epochs"]
        )

        val_predictions = model.predict(X_val)
        val_accuracy = accuracy_score(y_val, val_predictions)

        print("\nConfiguration", index)
        print("Hidden neurons:", config["hidden_size"])
        print("Learning rate:", config["learning_rate"])
        print("Epochs:", config["epochs"])
        print("Final training loss:", round(model.loss_history[-1], 6))
        print("Validation accuracy:", round(val_accuracy, 4))

        evaluate(
            model, X_test, y_test,
            "Test results for configuration " + str(index)
        )


if __name__ == "__main__":
    main()
