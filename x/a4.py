import numpy as np

def sigmoid_function(x):
    return 1 / ( 1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * ( 1 - x )

input = np.array([[0,0],[0,1],[1,0],[1,1]])
expected_output = np.array([[0],[1],[1],[0]])

epochs=3
lr=0.1

input_layer_neuron,hidden_layer_neuron,output_layer_neuron=2,2,1

hidden_weights=np.array([[7.1,0.9],[7.1,0.9]])
output_weights=np.array([[25.5],[-30.5]])

print("Initial hidden weights:")
print(*hidden_weights)
print("Initial output weights:")
print(*output_weights)

for _ in range(epochs):

    hidden_layer_activation=np.dot(input,hidden_weights)
    hidden_layer_output=sigmoid_function(hidden_layer_activation)

    output_layer_activation=np.dot(hidden_layer_output,output_weights)
    predicted_output=sigmoid_function(output_layer_activation)
    
    error=expected_output-predicted_output
    d_predicted_output=error*sigmoid_derivative(predicted_output)

    error_hidden_layer=d_predicted_output.dot(output_weights.T)
    d_hidden_layer=error_hidden_layer*sigmoid_derivative(hidden_layer_output)

    output_weights+=hidden_layer_output.T.dot(d_predicted_output)*lr
    hidden_weights+=input.T.dot(d_hidden_layer)*lr

print("Final hidden weights : ")
print(*hidden_weights)

print("Final output weights : ")
print(*output_weights)
