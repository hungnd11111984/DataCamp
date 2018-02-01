# Library 
# scikit-learn / sklearn
# Tensor Flow 
# keras 

# EDA - Explore Data Analyst 
pd.scatter_matrix (df, c =y , figsize = = [0,0], s = 150, marker='D')

# 1. k-Nearest Neighbors: Fit 
# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors = 6)

# Fit the classifier to the data
knn.fit(X,y)
# Out 
# KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
#           metric_params=None, n_jobs=1, n_neighbors=6, p=2,
#           weights='uniform') 

# 2 k-Nearest Neighbors: Predict
# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier 

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X, y)

# Predict the labels for the training data X: y_pred
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction)) 
# Prediction: ['democrat']

# 3 Measuring model performance
# Split training and test set. 
# Fit/Train the classifer on the training set 
# Make predictionn on the test set 
# Compare prediction with the know label. 
