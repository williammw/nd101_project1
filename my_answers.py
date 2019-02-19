import numpy as np


class NeuralNetwork(object):
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # Set number of nodes in input, hidden and output layers.
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # Initialize weights
        self.weights_input_to_hidden = np.random.normal(0.0, self.input_nodes**-0.5, 
                                       (self.input_nodes, self.hidden_nodes))

        self.weights_hidden_to_output = np.random.normal(0.0, self.hidden_nodes**-0.5, 
                                       (self.hidden_nodes, self.output_nodes))
        self.lr = learning_rate
        
        #### TODO: Set self.activation_function to your implemented sigmoid function ####
        #
        # Note: in Python, you can define a function with a lambda expression,
        # as shown below.
        self.activation_function = lambda x : 1 / (1 + np.exp(-x)) 
        # Replace 0 with your sigmoid calculation.
        
        ### If the lambda code above is not something you're familiar with,
        # You can uncomment out the following three lines and put your 
        # implementation there instead.
        #
        #def sigmoid(x):
        #    return 0  # Replace 0 with your sigmoid calculation here
        #self.activation_function = sigmoid
                    

    def train(self, features, targets):
        ''' Train the network on batch of features and targets. 
        
            Arguments
            ---------
            
            features: 2D array, each row is one data record, each column is a feature
            targets: 1D array of target values
        
        '''
        n_records = features.shape[0]
        delta_weights_i_h = np.zeros(self.weights_input_to_hidden.shape)
        delta_weights_h_o = np.zeros(self.weights_hidden_to_output.shape)
        for X, y in zip(features, targets):
            
            final_outputs, hidden_outputs = self.forward_pass_train(X)  # Implement the forward pass function below
            # Implement the backproagation function below
            delta_weights_i_h, delta_weights_h_o = self.backpropagation(final_outputs, hidden_outputs, X, y, delta_weights_i_h, delta_weights_h_o)
            
        self.update_weights(delta_weights_i_h, delta_weights_h_o, n_records)


    def forward_pass_train(self, X):
        ''' Implement forward pass here 
         
            Arguments
            ---------
            X: features batch

        '''
        #### Implement the forward pass here ####
        ### Forward pass ###
        # TODO: Hidden layer - Replace these values with your calculations.
        hidden_inputs = np.matmul(X, self.weights_input_to_hidden) # signals into hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # TODO: Output layer - Replace these values with your calculations.
        final_inputs = np.matmul(hidden_outputs, self.weights_hidden_to_output)  # signals into final output layer
        final_outputs = final_inputs # signals from final output layer
        
        return final_outputs, hidden_outputs

    def backpropagation(self, final_outputs, hidden_outputs, X, y, delta_weights_i_h, delta_weights_h_o):
        ''' Implement backpropagation
         
            Arguments
            ---------
            final_outputs: output from forward pass
            y: target (i.e. label) batch
            delta_weights_i_h: change in weights from input to hidden layers
            delta_weights_h_o: change in weights from hidden to output layers

        '''
        #### Implement the backward pass here ####
        ### Backward pass ###
        # print(final_outputs)
        # TODO: Output error - Replace this value with your calculations.
        error =  y - final_outputs # Output layer error is the difference between desired target and actual output.
        
        # TODO: Backpropagated error terms - Replace these values with your calculations.
        output_error_term = error
        # print(output_error_term)
        # TODO: Calculate the hidden layer's contribution to the error
        hidden_error = np.dot(self.weights_hidden_to_output, output_error_term.T)
        
        
        
        hidden_error_term = hidden_error*hidden_outputs*(1-hidden_outputs)
        
        # Weight step (input to hidden)
        delta_weights_i_h += hidden_error_term*np.array([X]).T
        # Weight step (hidden to output)
        delta_weights_h_o += output_error_term*np.array([hidden_outputs]).T
        return delta_weights_i_h, delta_weights_h_o

    def update_weights(self, delta_weights_i_h, delta_weights_h_o, n_records):
        ''' Update weights on gradient descent step
         
            Arguments
            ---------
            delta_weights_i_h: change in weights from input to hidden layers
            delta_weights_h_o: change in weights from hidden to output layers
            n_records: number of records

        '''
        self.weights_input_to_hidden += self.lr*delta_weights_i_h / n_records
        self.weights_hidden_to_output += self.lr*delta_weights_h_o / n_records

    def run(self, features):
        ''' Run a forward pass through the network with input features 
        
            Arguments
            ---------
            features: 1D array of feature values
        '''
        
        #### Implement the forward pass here ####
        # TODO: Hidden layer - replace these values with the appropriate calculations.
        hidden_inputs = np.matmul(features, self.weights_input_to_hidden) # signals into hidden layer
        hidden_outputs = self.activation_function(hidden_inputs) # signals from hidden layer
        
        # TODO: Output layer - Replace these values with the appropriate calculations.
        final_inputs = np.matmul(hidden_outputs, self.weights_hidden_to_output) # signals into final output layer
        final_outputs = final_inputs # signals from final output layer 
        
        return final_outputs

# Progress: 99.9% ... Training loss: 0.311 ... Validation loss: 0.493 (1000,0.1,24)
# Progress: 100.0% ... Training loss: 0.310 ... Validation loss: 0.493 (10000,0.01,18)
# Progress: 100.0% ... Training loss: 0.315 ... Validation loss: 0.504 (10000, 0.01,20)
# Progress: 100.0% ... Training loss: 0.305 ... Validation loss: 0.478 (10000,0.01,24)
# Progress: 100.0% ... Training loss: 0.194 ... Validation loss: 0.385 (10000,0.1,22)
# Progress: 100.0% ... Training loss: 0.136 ... Validation loss: 0.298 (10000,0.1,23)
# Progress: 100.0% ... Training loss: 0.149 ... Validation loss: 0.284 (10000,0.1,24)
# Progress: 100.0% ... Training loss: 0.170 ... Validation loss: 0.309 (10000,0.1,25)
# Progress: 100.0% ... Training loss: 0.306 ... Validation loss: 0.484 (10000,0.01,28)
# Progress: 100.0% ... Training loss: 0.306 ... Validation loss: 0.475 (10000,0.01,30)
# Progress: 100.0% ... Training loss: 0.307 ... Validation loss: 0.483 (10000,0.01,48)

#########################################################
# Set your hyperparameters here
##########################################################
iterations = 4000
learning_rate = 0.5
hidden_nodes = 23
output_nodes = 1