## 5. Generating Regression Data ##

# from sklearn.datasets import make_regression
# import pandas as pd

from sklearn.datasets import make_regression
import pandas as pd

data = make_regression(n_samples=100, n_features=3, random_state=1)

features = pd.DataFrame(data[0])
labels = pd.Series(data[1])

print(labels.head())
features.head()

## 6. Fitting A Linear Regression Neural Network ##

from sklearn.datasets import make_regression
import numpy as np
data = make_regression(n_samples=100, n_features=3, random_state=1)
features = pd.DataFrame(data[0])
labels = pd.Series(data[1])

# Uncomment after you've implemented train() and feedforward()
# train_weights = train(features, labels)
# linear_predictions = feedforward(features, train_weights)



###################3

from sklearn.linear_model import SGDRegressor
import numpy as np

features['bias'] = 1

def train(X, y):    
    lr = SGDRegressor()
    lr.fit(X,y)
    
    return lr.coef_

def feedforward(X, w):
    return np.dot(X, w)

train_weights = train(features, labels)
linear_predictions = feedforward(features, train_weights)

print(train_weights[:5])
linear_predictions[:5]

## 7. Generating Classification Data ##

from sklearn.datasets import make_classification

class_data = make_classification(n_samples=100, n_features=4, random_state=1)

class_features = pd.DataFrame(class_data[0])
class_labels = pd.Series(class_data[1])

print(class_labels.head())
class_features.head()

## 8. Implementing A Neural Network That Performs Classification ##

from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_classification

class_data = make_classification(n_samples=100, n_features=4, random_state=1)
class_features = pd.DataFrame(class_data[0])
class_labels = pd.Series(class_data[1])

class_features['bias'] = 1

def log_train(X, y):
    clf = SGDClassifier()
    clf.fit(X, y)
    
    return clf.coef_

def sigmoid(z):
    return 1/(1 + np.exp(-z))

def log_feedforward(X, w):
    linear_combination = np.dot(X, w.T)
    log_predictions = sigmoid(linear_combination)
    
    log_predictions[log_predictions <= 0.5] = 0
    log_predictions[log_predictions > 0.5] = 1
    
    return log_predictions

# Uncomment this code when you're ready to test your functions.
log_train_weights = log_train(class_features, class_labels)
log_predictions = log_feedforward(class_features, log_train_weights)

print(log_train_weights.shape)
log_predictions[:5]