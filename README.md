# Naive Bayes Classification

This document outlines the process of using the Naive Bayes classification method to predict user purchases from social network ads. The dataset `Social_Network_Ads.csv` contains user information such as age and estimated salary, along with a purchase decision.

## Steps Involved:

### 1. Import Libraries
First, import the required libraries:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
```

### 2. Load the Dataset
Load the data and separate features and the target variable:

```python
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
```

### 3. Split the Dataset
Divide the data into training and test sets:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
```

### 4. Feature Scaling
Apply feature scaling to normalize the feature values:

```python
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
```

### 5. Train the Model
Train the Naive Bayes model using the training set:

```python
classifier = GaussianNB()
classifier.fit(X_train, y_train)
```

### 6. Predict Results
Make a prediction for a new data point:

```python
new_prediction = classifier.predict(sc.transform([[30,87000]]))
```

### 7. Test Set Prediction
Predict the outcomes for the test set:

```python
y_pred = classifier.predict(X_test)
```

### 8. Evaluate the Model
Create a confusion matrix to evaluate the model's performance:

```python
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
```

The confusion matrix and the accuracy score give us insight into the number of correct and incorrect predictions.

## Conclusion

Naive Bayes is a simple yet powerful algorithm for classification based on Bayes' theorem with an assumption of independence among predictors. In this case, it is used to predict whether users purchased based on their age and estimated salary.

The Python code provided walks through the process of preparing the data, training the model, and evaluating its performance with a confusion matrix and accuracy score.
