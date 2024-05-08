import time
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestCentroid
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn import decomposition

# To ignore the runtime warnings that appear in the console
import warnings
warnings.simplefilter('ignore')


def run(x_train, y_train, x_test, y_test, clf):
    # This function performs a training and test run for a particular model (passed via clf). It
    # also records the time for each run.
    start_time = time.time()
    clf.fit(x_train, y_train)
    train_time = time.time() - start_time 
    start_time = time.time()
    score = clf.score(x_test, y_test)
    test_time = time.time() - start_time 
    print("score = %0.4f (trainimg time=%8.3f, testing time=%8.3f)" % (score, train_time, test_time))


def train(x_train, y_train, x_test, y_test):
    # For each of the models that we want to try out, this function calls the "run" function.
    print("    Nearest centroid          : ", end='')
    run(x_train, y_train, x_test, y_test, NearestCentroid())
    print("    k-NN classifier (k=3)     : ", end='')
    run(x_train, y_train, x_test, y_test, KNeighborsClassifier(n_neighbors=3))
    print("    k-NN classifier (k=7)     : ", end='')
    run(x_train, y_train, x_test, y_test, KNeighborsClassifier(n_neighbors=7))
    print("    Naive Bayes (Gaussian)    : ", end='')
    run(x_train, y_train, x_test, y_test, GaussianNB())
    print("    Decision Tree             : ", end='')
    run(x_train, y_train, x_test, y_test, DecisionTreeClassifier())
    print("    Random Forest (trees=  5) : ", end='')
    run(x_train, y_train, x_test, y_test, RandomForestClassifier(n_estimators=5))
    print("    Random Forest (trees= 50) : ", end='')
    run(x_train, y_train, x_test, y_test, RandomForestClassifier(n_estimators=50))
    print("    Random Forest (trees=500) : ", end='')
    run(x_train, y_train, x_test, y_test, RandomForestClassifier(n_estimators=500))
    print("    Random Forest (trees=1000): ", end='')
    run(x_train, y_train, x_test, y_test, RandomForestClassifier(n_estimators=1000))
    print("    LinearSVM (C=0.01)        : ", end='')
    run(x_train, y_train, x_test, y_test, LinearSVC(C=0.01))
    print("    LinearSVM (C=0.1)         : ", end='')
    run(x_train, y_train, x_test, y_test, LinearSVC(C=0.1))
    print("    LinearSVM (C=1.0)         : ", end='')
    run(x_train, y_train, x_test, y_test, LinearSVC(C=1.0))
    print("    LinearSVM (C=10.0)        : ", end='')
    run(x_train, y_train, x_test, y_test, LinearSVC(C=10.0))


def main():
    # Load the MNIST data from the sklearn dataset
    mnist = load_digits()
    # Split the data into training and test sets
    x_train, x_test, y_train, y_test = train_test_split(mnist.data, mnist.target, test_size=0.25, random_state=42)

    # First, let's work with the raw image data. That is, the raw pixel values (between 0 and 255).
    print("Models trained on raw [0,255] images:")
    train(x_train, y_train, x_test, y_test)

    # Next, let's work with the scaled pixel values. To do this, divide each pixel valueby 255.
    print("Models trained on raw [0,1) images:")
    train(x_train/255.0, y_train, x_test/256.0, y_test)

    # Next, let's try normalized values. To normalize, we subtract the mean value of a pixel across the dataset and
    # then divide by the standard deviation. We choose to get the mean and standard deviations from the testing set 
    # (because it's a larger data set). We are fortunate that the training and testing datasets come from the same 
    # distribution, so the means and standard deviations will be transferrable. Normalizing will change the appearance 
    # of the pixels, but not the shape of the objects in each image. This allows us to see if the range of feature 
    # values (i.e. the range of pixel values) is important. We add a tiny value to the standard deviation to cater 
    # for situations where the standard deviation is zero (because we cannot later divide by zero).
    feature_mean = x_train.mean(axis=0)
    feature_std_dev = x_train.std(axis=0) + 1e-8
    x_norm_train = (x_train - feature_mean) / feature_std_dev
    x_norm_test  = (x_test - feature_mean) / feature_std_dev
    print("Models trained on normalized images:")
    train(x_norm_train, y_train, x_norm_test, y_test)

    # Finally, we apply PCA (principle component analysis), keeping the first 32 components. This reduces the feature 
    # vector from 784 features (the pixels) to 32. We apply PCA to the normalized values from the previous step.
    pca = decomposition.PCA(n_components=32)
    pca.fit(x_norm_train)
    x_pca_train = pca.transform(x_norm_train)
    x_pca_test = pca.transform(x_norm_test)
    print("Models trained on first 15 PCA components of normalized images:")
    train(x_pca_train, y_train, x_pca_test, y_test)


main()