Traffic Sign Recognition - Experiment Report
This report details an investigation into improving the accuracy of a machine learning model for traffic sign recognition. The initial model achieved an accuracy of only 0.0544.

Experimentation
Activation Functions:
No activation function: Achieved an accuracy of 0.9379 (loss: 2.6342).
Sigmoid activation function: Achieved an accuracy of 0.9813 (loss: 0.0846). This suggests sigmoid's ability to calculate confidence values between 0 and 1 is beneficial.
Softmax activation function: Achieved an accuracy of 0.4111 (loss: 1.9982). This indicates the network performs better with distributed probabilities compared to binary outputs.
Output Activation Function:
No output activation function: Achieved an accuracy of 0.0301 (loss: 8.2058).
ReLu activation function: Achieved an accuracy of 0.0061 (loss: nan). This suggests ReLu's binary output hinders learning.
Sigmoid activation function: Achieved an accuracy of 0.0556 (loss: 3.4927). The results are similar to the initial setup, likely due to the unchanged hidden and convolution layers.
Number of Nodes: Doubling the number of nodes increased accuracy to 0.4242 (loss: 1.9518), suggesting more nodes improve training precision.
Number of Filters:
Doubling filters: Achieved an accuracy of 0.0538 (loss: 3.5008).
Halving filters: Achieved an accuracy of 0.0547 (loss: 3.5019). Neither significantly affected the outcome.
Pool Size: Increasing pool size to (4, 4) resulted in a slight improvement to 0.0570 (loss: 3.4928).
Dropout: Varying dropout rate (0.75 and 0.25) had minimal impact, suggesting the model was not overfitting.
Additional Layer: Adding another hidden layer yielded minimal change (accuracy: 0.0545, loss: 3.5040).
Conclusion
The experiments demonstrate that activation functions and the number of nodes significantly impact the model's performance. Sigmoid and softmax activation functions, due to their non-binary outputs, were most effective. Other parameters, like dropout and additional layers, provided less significant improvements.

Final Model
A final model using sigmoid activation in both the convolution and hidden layers, and softmax in the output layer, achieved an accuracy of >0.098 with a loss of <0.05.
