README

An AI project used to predict wins and losses given quarterback data.
Uses a neural network for classification.
Python script is for filtering data from the given CSV file.

A combination of linear transformations and ReLU activation functions are applied to the data in the forward function.
A smoth L1 loss function is applied as the criterion which uses a squared term if the absolute element-wise error falls below 1 and an L1 term otherwise. This loss function may be changed in the future.
There is a total of 200 iterations (epochs) through the neural network.
The amount of loss shrinks as the data travels through the neural network; the loss is printed out every 10 iterations.
The neural network is only roughly 48% accurate. Changing the loss function might make it more accurate.
