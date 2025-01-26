class SigmoidPerceptron:
    import numpy as np

    def __init__(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand(1)

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def predict(self, inputs):
        z = np.dot(inputs, self.weights) + self.bias
        return self.sigmoid(z)

    def train(self, inputs, targets, learning_rate, epochs):
        num_examples = inputs.shape[0]

        for epoch in range(epochs):
            for i in range(num_examples):
                input_vector = inputs[i]
                target = targets[i]

                prediction = self.predict(input_vector)
                error = target - prediction

                # Update weights
                gradient_weights = error * prediction * (1 - prediction) * input_vector
                self.weights += learning_rate * error * gradient_weights
                # Update bias
                gradient_bias = error * prediction * (1 - prediction)
                self.bias += learning_rate * gradient_bias

    def evaluate(self, inputs, targets):
        correct = 0
        for input_vector, target in zip(inputs, targets):
            prediction = self.predict(input_vector)
            predicted_class = 1 if prediction >= 0.5 else 0
            if predicted_class == target:
                correct += 1
        accuracy = correct / len(inputs)
        return accuracy
