# MNIST-experiments

## Accuracy

|                        | Raw Images | Scaled Images | Normalized Images | 32 PCA Components |
| :--------------------: | :--------: | :-----------: | :---------------: | :---------------: |
| Nearest centroid       | 90.44%     | 90.44%        | 88.67%            | 88.67%            |
| k-NN classifier (k=3)  | 98.67%     | 98.67%        | 96.67%            | 96.67%            |
| k-NN classifier (k=7)  | **99.33%**     | **99.33%**        | 97.78%            | 96.67%            |
| Naive Bayes (Gaussian) | 85.56%     | 85.56%        | 77.56%            | 91.56%            |
| Decision Tree          | 86.22%     | 85.56%        | 86.22%            | 84.22%            |
| Random Forest (t=  5)  | 92.00%     | 91.33%        | 93.11%            | 87.56%            |
| Random Forest (t= 50)  | 97.33%     | 97.11%        | 98.00%            | 96.67%            |
| Random Forest (t=500)  | 97.56%     | 97.56%        | 97.56%            | 96.44%            |
| Random Forest (t=1000) | 97.56%     | 97.56%        | 97.56%            | 96.44%            |
| LinearSVM (C=0.01)     | 96.89%     | 74.67%        | 96.00%            | 94.67%            |
| LinearSVM (C=0.1)      | 97.11%     | 88.67%        | 96.67%            | 96.00%            |
| LinearSVM (C=1.0)      | 96.00%     | 93.11%        | 96.22%            | 95.11%            |
| LinearSVM (C=10.0)     | 96.67%     | 96.22%        | 95.78%            | 94.89%            |

## Training Time

Models trained on raw [0,255] images:
    Nearest centroid          : score = 0.9044 (trainimg time=   0.001, testing time=   0.006)
    k-NN classifier (k=3)     : score = 0.9867 (trainimg time=   0.000, testing time=   0.021)
    k-NN classifier (k=7)     : score = 0.9933 (trainimg time=   0.001, testing time=   0.021)
    Naive Bayes (Gaussian)    : score = 0.8556 (trainimg time=   0.003, testing time=   0.001)
    Decision Tree             : score = 0.8622 (trainimg time=   0.014, testing time=   0.000)
    Random Forest (trees=  5) : score = 0.9200 (trainimg time=   0.011, testing time=   0.001)
    Random Forest (trees= 50) : score = 0.9733 (trainimg time=   0.099, testing time=   0.005)
    Random Forest (trees=500) : score = 0.9756 (trainimg time=   0.912, testing time=   0.044)
    Random Forest (trees=1000): score = 0.9756 (trainimg time=   1.818, testing time=   0.087)
    LinearSVM (C=0.01)        : score = 0.9689 (trainimg time=   0.063, testing time=   0.001)
    LinearSVM (C=0.1)         : score = 0.9711 (trainimg time=   0.065, testing time=   0.000)
    LinearSVM (C=1.0)         : score = 0.9600 (trainimg time=   0.062, testing time=   0.000)
    LinearSVM (C=10.0)        : score = 0.9667 (trainimg time=   0.063, testing time=   0.000)
Models trained on raw [0,1) images:
    Nearest centroid          : score = 0.9044 (trainimg time=   0.001, testing time=   0.000)
    k-NN classifier (k=3)     : score = 0.9867 (trainimg time=   0.000, testing time=   0.016)
    k-NN classifier (k=7)     : score = 0.9933 (trainimg time=   0.000, testing time=   0.017)
    Naive Bayes (Gaussian)    : score = 0.8556 (trainimg time=   0.002, testing time=   0.001)
    Decision Tree             : score = 0.8556 (trainimg time=   0.012, testing time=   0.000)
    Random Forest (trees=  5) : score = 0.9133 (trainimg time=   0.010, testing time=   0.001)
    Random Forest (trees= 50) : score = 0.9711 (trainimg time=   0.098, testing time=   0.005)
    Random Forest (trees=500) : score = 0.9756 (trainimg time=   0.903, testing time=   0.042)
    Random Forest (trees=1000): score = 0.9756 (trainimg time=   1.795, testing time=   0.085)
    LinearSVM (C=0.01)        : score = 0.7467 (trainimg time=   0.008, testing time=   0.001)
    LinearSVM (C=0.1)         : score = 0.8867 (trainimg time=   0.012, testing time=   0.000)
    LinearSVM (C=1.0)         : score = 0.9311 (trainimg time=   0.022, testing time=   0.001)
    LinearSVM (C=10.0)        : score = 0.9622 (trainimg time=   0.065, testing time=   0.000)
Models trained on normalized images:
    Nearest centroid          : score = 0.8867 (trainimg time=   0.001, testing time=   0.000)
    k-NN classifier (k=3)     : score = 0.9667 (trainimg time=   0.000, testing time=   0.014)
    k-NN classifier (k=7)     : score = 0.9778 (trainimg time=   0.000, testing time=   0.018)
    Naive Bayes (Gaussian)    : score = 0.7756 (trainimg time=   0.001, testing time=   0.001)
    Decision Tree             : score = 0.8622 (trainimg time=   0.012, testing time=   0.000)
    Random Forest (trees=  5) : score = 0.9311 (trainimg time=   0.010, testing time=   0.001)
    Random Forest (trees= 50) : score = 0.9800 (trainimg time=   0.097, testing time=   0.005)
    Random Forest (trees=500) : score = 0.9756 (trainimg time=   0.900, testing time=   0.042)
    Random Forest (trees=1000): score = 0.9756 (trainimg time=   1.808, testing time=   0.085)
    LinearSVM (C=0.01)        : score = 0.9600 (trainimg time=   0.040, testing time=   0.000)
    LinearSVM (C=0.1)         : score = 0.9667 (trainimg time=   0.085, testing time=   0.000)
    LinearSVM (C=1.0)         : score = 0.9622 (trainimg time=   0.118, testing time=   0.000)
    LinearSVM (C=10.0)        : score = 0.9578 (trainimg time=   0.107, testing time=   0.000)
Models trained on first 15 PCA components of normalized images:
    Nearest centroid          : score = 0.8867 (trainimg time=   0.001, testing time=   0.001)
    k-NN classifier (k=3)     : score = 0.9667 (trainimg time=   0.000, testing time=   0.014)
    k-NN classifier (k=7)     : score = 0.9667 (trainimg time=   0.000, testing time=   0.017)
    Naive Bayes (Gaussian)    : score = 0.9156 (trainimg time=   0.001, testing time=   0.001)
    Decision Tree             : score = 0.8422 (trainimg time=   0.029, testing time=   0.000)
    Random Forest (trees=  5) : score = 0.8756 (trainimg time=   0.019, testing time=   0.001)
    Random Forest (trees= 50) : score = 0.9667 (trainimg time=   0.210, testing time=   0.005)
    Random Forest (trees=500) : score = 0.9644 (trainimg time=   1.776, testing time=   0.044)
    Random Forest (trees=1000): score = 0.9644 (trainimg time=   3.401, testing time=   0.087)
    LinearSVM (C=0.01)        : score = 0.9467 (trainimg time=   0.024, testing time=   0.001)
    LinearSVM (C=0.1)         : score = 0.9600 (trainimg time=   0.062, testing time=   0.000)
    LinearSVM (C=1.0)         : score = 0.9511 (trainimg time=   0.083, testing time=   0.000)
    LinearSVM (C=10.0)        : score = 0.9489 (trainimg time=   0.077, testing time=   0.000)

Accuracy

Models trained on raw [0,255] images:
    Nearest centroid          : score = 0.9044 (trainimg time=   0.001, testing time=   0.006)
    k-NN classifier (k=3)     : score = 0.9867 (trainimg time=   0.000, testing time=   0.021)
    k-NN classifier (k=7)     : score = 0.9933 (trainimg time=   0.001, testing time=   0.021)
    Naive Bayes (Gaussian)    : score = 0.8556 (trainimg time=   0.003, testing time=   0.001)
    Decision Tree             : score = 0.8622 (trainimg time=   0.014, testing time=   0.000)
    Random Forest (trees=  5) : score = 0.9200 (trainimg time=   0.011, testing time=   0.001)
    Random Forest (trees= 50) : score = 0.9733 (trainimg time=   0.099, testing time=   0.005)
    Random Forest (trees=500) : score = 0.9756 (trainimg time=   0.912, testing time=   0.044)
    Random Forest (trees=1000): score = 0.9756 (trainimg time=   1.818, testing time=   0.087)
    LinearSVM (C=0.01)        : score = 0.9689 (trainimg time=   0.063, testing time=   0.001)
    LinearSVM (C=0.1)         : score = 0.9711 (trainimg time=   0.065, testing time=   0.000)
    LinearSVM (C=1.0)         : score = 0.9600 (trainimg time=   0.062, testing time=   0.000)
    LinearSVM (C=10.0)        : score = 0.9667 (trainimg time=   0.063, testing time=   0.000)
Models trained on raw [0,1) images:
    Nearest centroid          : score = 0.9044 (trainimg time=   0.001, testing time=   0.000)
    k-NN classifier (k=3)     : score = 0.9867 (trainimg time=   0.000, testing time=   0.016)
    k-NN classifier (k=7)     : score = 0.9933 (trainimg time=   0.000, testing time=   0.017)
    Naive Bayes (Gaussian)    : score = 0.8556 (trainimg time=   0.002, testing time=   0.001)
    Decision Tree             : score = 0.8556 (trainimg time=   0.012, testing time=   0.000)
    Random Forest (trees=  5) : score = 0.9133 (trainimg time=   0.010, testing time=   0.001)
    Random Forest (trees= 50) : score = 0.9711 (trainimg time=   0.098, testing time=   0.005)
    Random Forest (trees=500) : score = 0.9756 (trainimg time=   0.903, testing time=   0.042)
    Random Forest (trees=1000): score = 0.9756 (trainimg time=   1.795, testing time=   0.085)
    LinearSVM (C=0.01)        : score = 0.7467 (trainimg time=   0.008, testing time=   0.001)
    LinearSVM (C=0.1)         : score = 0.8867 (trainimg time=   0.012, testing time=   0.000)
    LinearSVM (C=1.0)         : score = 0.9311 (trainimg time=   0.022, testing time=   0.001)
    LinearSVM (C=10.0)        : score = 0.9622 (trainimg time=   0.065, testing time=   0.000)
Models trained on normalized images:
    Nearest centroid          : score = 0.8867 (trainimg time=   0.001, testing time=   0.000)
    k-NN classifier (k=3)     : score = 0.9667 (trainimg time=   0.000, testing time=   0.014)
    k-NN classifier (k=7)     : score = 0.9778 (trainimg time=   0.000, testing time=   0.018)
    Naive Bayes (Gaussian)    : score = 0.7756 (trainimg time=   0.001, testing time=   0.001)
    Decision Tree             : score = 0.8622 (trainimg time=   0.012, testing time=   0.000)
    Random Forest (trees=  5) : score = 0.9311 (trainimg time=   0.010, testing time=   0.001)
    Random Forest (trees= 50) : score = 0.9800 (trainimg time=   0.097, testing time=   0.005)
    Random Forest (trees=500) : score = 0.9756 (trainimg time=   0.900, testing time=   0.042)
    Random Forest (trees=1000): score = 0.9756 (trainimg time=   1.808, testing time=   0.085)
    LinearSVM (C=0.01)        : score = 0.9600 (trainimg time=   0.040, testing time=   0.000)
    LinearSVM (C=0.1)         : score = 0.9667 (trainimg time=   0.085, testing time=   0.000)
    LinearSVM (C=1.0)         : score = 0.9622 (trainimg time=   0.118, testing time=   0.000)
    LinearSVM (C=10.0)        : score = 0.9578 (trainimg time=   0.107, testing time=   0.000)
Models trained on first 15 PCA components of normalized images:
    Nearest centroid          : score = 0.8867 (trainimg time=   0.001, testing time=   0.001)
    k-NN classifier (k=3)     : score = 0.9667 (trainimg time=   0.000, testing time=   0.014)
    k-NN classifier (k=7)     : score = 0.9667 (trainimg time=   0.000, testing time=   0.017)
    Naive Bayes (Gaussian)    : score = 0.9156 (trainimg time=   0.001, testing time=   0.001)
    Decision Tree             : score = 0.8422 (trainimg time=   0.029, testing time=   0.000)
    Random Forest (trees=  5) : score = 0.8756 (trainimg time=   0.019, testing time=   0.001)
    Random Forest (trees= 50) : score = 0.9667 (trainimg time=   0.210, testing time=   0.005)
    Random Forest (trees=500) : score = 0.9644 (trainimg time=   1.776, testing time=   0.044)
    Random Forest (trees=1000): score = 0.9644 (trainimg time=   3.401, testing time=   0.087)
    LinearSVM (C=0.01)        : score = 0.9467 (trainimg time=   0.024, testing time=   0.001)
    LinearSVM (C=0.1)         : score = 0.9600 (trainimg time=   0.062, testing time=   0.000)
    LinearSVM (C=1.0)         : score = 0.9511 (trainimg time=   0.083, testing time=   0.000)
    LinearSVM (C=10.0)        : score = 0.9489 (trainimg time=   0.077, testing time=   0.000)
