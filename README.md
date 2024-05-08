# MNIST-experiments
This repository examines the performance a various approaches to classifying digits from the MNIST data set.


## Introducing the Models
**Nearest Centroid** is the simplest model. It is a useful baseline. However, it makes a simplistic assumption that does not often bear out in practice: that the classes form a tight group in the feature space and the groups are distant from one another. Training time and classifation time is very fast, as it works with one centroid per class.

**k-Nearest Neighbors** doesn't require training, as the training data set is used to classify new instances. However, classification is slow because of the need to look at every training sample. It performs well if the number of training samples is large relative to the dimensionality of the feature space.

**Naive Bayes** does reasonably well, even when the core assumption of feature independence is not met. It is fast to train and classify. 

One useful aspect of **Decision Trees** is that you can see the steps it takes to reach a decision. However, they are prone to over-fitting, and performance degrades as the tree grows in size. That being said, it is fast for both training and classifying.

**Random Forests** are essentially a more powerful form of Decision Tree. They use randomness to overcome the over-fitting issue. The inference runtime scales lineraly with the number of trees. Because it is a stochastic model, performance will vary across executions.

**Support Vector Machines** show excellent performance when the hyperparemeters are properly tuned. Normalization and other scaling methods are often necessary to get good performance.

A **Perceptron** is a single-layer neural network that uses no regularization, a linear loss function, and Stochastic Gradient Descent. There are no hidden nodes, with the input nodes being connected directly to the output nodes. When the hyperparameters are tuned, it can provide good accuracy with fast training and very fast classification.

A **Feed Forward Neural Network** is a multi-layer neural network. I experiment with different node configurations, activation functions, and back propagation approaches. When the hyperparameters are tuned, it can provide very good accuracy with very fast classification, but training time can be quite slow.

Note that the scikit-learn library does not include Convolutional Neural Networks, otherwise I would have included them.


## Accuracy

|                        | Raw Images | Scaled Images | Normalized Images | 32 PCA Components |
|------------------------| :--------: | :-----------: | :---------------: | :---------------: |
| Nearest Centroid       | 90.44%     | 90.44%        | 88.67%            | 88.67%            |
| k-NN classifier (k=3)  | 98.67%     | 98.67%        | 96.67%            | 96.67%            |
| k-NN classifier (k=7)  | **99.33%**     | **99.33%**        | 97.78%            | 96.67%            |
| Naive Bayes (Gaussian) | 85.56%     | 85.56%        | 77.56%            | 91.56%            |
| Decision Tree          | 86.22%     | 85.56%        | 86.22%            | 84.22%            |
| Random Forest (t=5)    | 92.00%     | 91.33%        | 93.11%            | 87.56%            |
| Random Forest (t=50)   | 97.33%     | 97.11%        | 98.00%            | 96.67%            |
| Random Forest (t=500)  | 97.56%     | 97.56%        | 97.56%            | 96.44%            |
| Random Forest (t=1000) | 97.56%     | 97.56%        | 97.56%            | 96.44%            |
| LinearSVM (C=0.01)     | 96.89%     | 74.67%        | 96.00%            | 94.67%            |
| LinearSVM (C=0.1)      | 97.11%     | 88.67%        | 96.67%            | 96.00%            |
| LinearSVM (C=1.0)      | 96.00%     | 93.11%        | 96.22%            | 95.11%            |
| LinearSVM (C=10.0)     | 96.67%     | 96.22%        | 95.78%            | 94.89%            |
| Perceptron             | 96.22%     | 90.89%        | 96.00%            | 92.67%            |
| Feed Forward (64,ReLU) | 96.67%     | 90.44%        | 98.00%            | 98.00%            |
| Feed Forward (256,ReLU)| 97.11%     | 94.00%        | 97.33%            | 97.33%            |
| Feed Forward (256,Sigm)| 97.33%     | 75.11%        | 95.78%            | 96.44%            |
| Feed Forward (256,SGD) | 93.56%     | _15.11%_      | 95.78%            | 95.56%            |
| Feed Forward (512,ReLU)| 96.67%     | 88.67%        | 98.44%            | 98.00%            |

Nearest Centroid shows an accuracy of 90.44% for both the raw images and the scaled images. This makes sense, as scaling the values by a constant will not change the relationship between the per class centroids. However, normalizing does change the centroid's relationship to one another, bringing the accuracy down to 88.67%.

The 3-Nearest Neighbor classifier shows an accuracy of 98.67% on raw and scaled images. Across the input types, we see a similar pattern to Nearest Centroid, which is not surprising given the approaches are so similar. The 7-Nearest Neighbor classifier produces the best results across the board.

The Gaussian Naive Bayes classifier performs poorly across the board. However, it's performance improves significantly when working with the PCA inputs. This is the only model to improve after using PCA. This is because a Gaussian Naive Bayes classifier assumes the data is independent and forms a normal distribution (where we can estimate the mean and standard deviation from the feature values themselves). PCA is the equivalent of rotating the feature vectors to align with the largest orthogonal directions derived from the data set, thereby ensuring the data is independent. And the gaussian aspect of the classifier implies a normal distribution. This is why the Gaussian Naive Bayes classifier performs so well with PCA data.

The Decision Tree classifier and the various Random Forest classifiers perform similarily across the Raw Image, Scaled Image, and Normalized Image data sets. However, they all perform less well with the PCA data set, because working with the reduced dimensions of the PCA means that some potentially important information is missing.

Of the tree-based classifiers,the single Decision Tree performs least well. The Random Forest classifiers get a big performance improvement when going from 5 trees to 50 trees, but the performance gains top out somewhere betwee 50 trees and 500 trees, depending on the data set.

We cannot use a Support Vector Machine (SVM), because it is designed for use with binary classification and we have 10 classes. Therefore, we use 10 SVMs, one to classify 0 versus the rest (i.e. 1-9), the next to classift 1 versus the rest (i.e. 0 and 2-9), and so on.

The Perceptron has quite good accuracy, especially when you consider the relative simplicity of the model compared to the multi-layer neural networks. For some reason, there is a significant drop-off for the scaled images.

Like with the Perceptron, the Feed Forward Neural Networks have noticably poorer performance with the Scaled Images. I'm not sure why this is. Also, the Adam optimizer has noticably better performance than Stochastic Gradient Descent, and for the most part the ReLU activation performs better than a Sigmoid activation.


## Training Time

|                        | Raw Images | Scaled Images | Normalized Images | 32 PCA Components |
|------------------------| :--------: | :-----------: | :---------------: | :---------------: |
| Nearest Centroid       | 0.001      | 0.001         | 0.001             | 0.001             |
| k-NN classifier (k=3)  | **0.000**      | **0.000**         | **0.000**             | **0.000**             |
| k-NN classifier (k=7)  | 0.001      | **0.000**         | **0.000**             | **0.000**             |
| Naive Bayes (Gaussian) | 0.003      | 0.002         | 0.001             | 0.001             |
| Decision Tree          | 0.014      | 0.012         | 0.012             | 0.029             |
| Random Forest (t=5)    | 0.011      | 0.010         | 0.010             | 0.019             |
| Random Forest (t=50)   | 0.099      | 0.098         | 0.097             | 0.210             |
| Random Forest (t=500)  | 0.912      | 0.903         | 0.900             | 1.776             |
| Random Forest (t=1000) | 1.818      | 1.795         | 1.808             | 3.401             |
| LinearSVM (C=0.01)     | 0.063      | 0.008         | 0.040             | 0.024             |
| LinearSVM (C=0.1)      | 0.065      | 0.012         | 0.085             | 0.062             |
| LinearSVM (C=1.0)      | 0.062      | 0.022         | 0.118             | 0.083             |
| LinearSVM (C=10.0)     | 0.063      | 0.065         | 0.107             | 0.077             |
| Perceptron             | 0.019      | 0.010         | 0.017             | 0.010             |
| Feed Forward (64,ReLU) | 0.759      | 0.946         | 0.715             | 0.981             |
| Feed Forward (256,ReLU)| 1.352      | 2.297         | 0.989             | 0.952             |
| Feed Forward (256,Sigm)| 2.194      | 2.264         | 2.437             | 1.778             |
| Feed Forward (256,SGD) | 2.229      | 1.615         | 2.043             | 1.565             |
| Feed Forward (512,ReLU)| _3.453_      | 3.146         | 1.470             | 1.240             |

## Testing Time

|                        | Raw Images | Scaled Images | Normalized Images | 32 PCA Components |
|------------------------| :--------: | :-----------: | :---------------: | :---------------: |
| Nearest Centroid       | 0.006      | **0.000**         | **0.000**             | 0.001             |
| k-NN classifier (k=3)  | 0.021      | 0.016         | 0.014             | 0.014             |
| k-NN classifier (k=7)  | 0.021      | 0.017         | 0.018             | 0.017             |
| Naive Bayes (Gaussian) | 0.001      | 0.001         | 0.001             | 0.001             |
| Decision Tree          | **0.000**      | **0.000**         | **0.000**             | **0.000**             |
| Random Forest (t=5)    | 0.001      | 0.001         | 0.001             | 0.001             |
| Random Forest (t=50)   | 0.005      | 0.005         | 0.005             | 0.005             |
| Random Forest (t=500)  | 0.044      | 0.042         | 0.042             | 0.044             |
| Random Forest (t=1000) | 0.087      | 0.085         | 0.085             | 0.087             |
| LinearSVM (C=0.01)     | 0.001      | 0.001         | **0.000**             | 0.001             |
| LinearSVM (C=0.1)      | **0.000**      | **0.000**         | **0.000**             | **0.000**             |
| LinearSVM (C=1.0)      | **0.000**      | 0.001         | **0.000**             | **0.000**             |
| LinearSVM (C=10.0)     | **0.000**      | **0.000**         | **0.000**             | **0.000**             |
| Perceptron             | **0.000**      | **0.000**         | **0.000**            | 0.007            |
| Feed Forward (64,ReLU) | 0.001      | 0.001         | 0.001             | **0.000**             |
| Feed Forward (256,ReLU)| 0.001      | 0.001         | 0.001             | 0.001             |
| Feed Forward (256,Sigm)| 0.002      | 0.002         | 0.002             | 0.001             |
| Feed Forward (256,SGD) | 0.001      | 0.002         | 0.001             | 0.001             |
| Feed Forward (512,ReLU)| 0.002      | 0.002         | 0.002             | 0.002             |

