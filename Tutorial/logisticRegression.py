
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_auc_score
)
from sklearn.linear_model import LogisticRegression


class MyLogisticRegression:
    def __init__(self, learning_rate=0.01, iterations=3000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = 0
        self.loss_history = []

    def sigmoid(self, z):
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        m, n = X.shape

        self.weights = np.zeros(n)
        self.bias = 0

        for _ in range(self.iterations):
            linear = X @ self.weights + self.bias
            probabilities = self.sigmoid(linear)

            # Binary cross-entropy loss
            eps = 1e-12
            loss = -np.mean(
                y * np.log(probabilities + eps)
                + (1 - y) * np.log(1 - probabilities + eps)
            )
            self.loss_history.append(loss)

            # Gradients
            dw = X.T @ (probabilities - y) / m
            db = np.mean(probabilities - y)

            # Gradient descent
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

        return self

    def predict_proba(self, X):
        return self.sigmoid(X @ self.weights + self.bias)

    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X) >= threshold).astype(int)


def evaluate_model(y_true, probabilities, threshold=0.5):
    predictions = (probabilities >= threshold).astype(int)

    print("Threshold:", threshold)
    print("Accuracy:", round(accuracy_score(y_true, predictions), 4))
    print("Precision:", round(
        precision_score(y_true, predictions, zero_division=0), 4
    ))
    print("Recall:", round(
        recall_score(y_true, predictions, zero_division=0), 4
    ))
    print("F1-score:", round(
        f1_score(y_true, predictions, zero_division=0), 4
    ))
    print("Confusion matrix:\n", confusion_matrix(y_true, predictions))
    print("ROC-AUC:", round(roc_auc_score(y_true, probabilities), 4))


def main():
    data = load_breast_cancer()
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Fit the scaler only on training data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Custom implementation
    model = MyLogisticRegression(
        learning_rate=0.01,
        iterations=3000
    )
    model.fit(X_train, y_train)

    probabilities = model.predict_proba(X_test)

    print("CUSTOM LOGISTIC REGRESSION")
    evaluate_model(y_test, probabilities, threshold=0.5)

    print("\nEffect of classification threshold")
    for threshold in (0.3, 0.5, 0.7):
        evaluate_model(y_test, probabilities, threshold)

    print("\nEffect of learning rate")
    for rate in (0.001, 0.01, 0.1):
        experiment = MyLogisticRegression(
            learning_rate=rate,
            iterations=3000
        )
        experiment.fit(X_train, y_train)

        print(
            "Learning rate:", rate,
            "| Final training loss:",
            round(experiment.loss_history[-1], 6)
        )

    # Standard scikit-learn implementation
    standard_model = LogisticRegression(max_iter=5000)
    standard_model.fit(X_train, y_train)

    standard_probabilities = standard_model.predict_proba(X_test)[:, 1]

    print("\nSCIKIT-LEARN LOGISTIC REGRESSION")
    evaluate_model(y_test, standard_probabilities, threshold=0.5)


if __name__ == "__main__":
    main()
