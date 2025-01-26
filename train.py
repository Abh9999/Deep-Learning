from sigmoid_perceptron import SigmoidPerceptron
from data_processing import load_data, preprocess_data, split_data

# Load and preprocess data
x, y = load_data("diabetes.csv")
x = preprocess_data(x)
x_train, x_test, y_train, y_test = split_data(x, y)

# Initialize the model
input_size = x_train.shape[1]
model = SigmoidPerceptron(input_size)

# Train the model
learning_rate = 0.01
epochs = 1000
model.train(x_train, y_train, learning_rate, epochs)

#evaluate the model for traning data
accuracy = perceptron.evaluate(x_train, y_train)
accuracy =round(accuracy*100, 2)
print(f"Accuracy on training data: {accuracy} %")

#evaluate the model for test data
accuracy = perceptron.evaluate(x_test, y_test)
accuracy =round(accuracy*100, 2)
print(f"Accuracy on test data: {accuracy} %")