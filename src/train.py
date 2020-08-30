import pickle as pkl
from src import build_features as bf
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Prepare the training data
x_train = bf.feature_expansion("train", "train")
y_train = x_train['Survived']
del (x_train["Survived"])

# Prepare the test data
x_val = bf.feature_expansion("val", "val")
y_val = y_train['Survived']
del (x_val["Survived"])

# Create pipelines to perform grid search on multiple candidate models

# Logistic Regression
pipe_lr = Pipeline([('classifier', LogisticRegression())])
param_grid_lr = [{
    'classifier__penalty': ['l1', 'l2'],
    'classifier__C': np.logspace(-4, 4, 20),
    'classifier__solver': ['liblinear'],
    'classifier__max_iter': [10000]
}]
clf_lr = GridSearchCV(pipe_lr, param_grid=param_grid_lr, cv=5, verbose=True, n_jobs=8)
clf_lr.fit(x_train, y_train)

# Random Forest Classifier
pipe_rf = Pipeline([('classifier', RandomForestClassifier())])
param_grid_rf = [{
    'classifier__n_estimators': list(range(50, 150, 5)),
    'classifier__max_features': list(range(2, 10, 1)),
    'classifier__oob_score': [True]
}]
clf_rf = GridSearchCV(pipe_rf, param_grid=param_grid_rf, cv=5, verbose=True, n_jobs=8)
clf_rf.fit(x_train, y_train)

# Linear SVC
pipe_svc = Pipeline([('classifier', LinearSVC())])
param_grid_svc = [{
    'classifier__loss': ['hinge', 'squared_hinge'],
    'classifier__C': np.logspace(-4, 4, 20),
    'classifier__max_iter': [10000]
}]
clf_svc = GridSearchCV(pipe_svc, param_grid=param_grid_svc, cv=5, verbose=True, n_jobs=8)
clf_svc.fit(x_train, y_train)

# KNeighbors Classifier
pipe_knn = Pipeline([('classifier', KNeighborsClassifier())])
param_grid_knn = [{
    'classifier__n_neighbors': range(1, 10)
}]
clf_knn = GridSearchCV(pipe_knn, param_grid=param_grid_knn, cv=5, verbose=True, n_jobs=8)
clf_knn.fit(x_train, y_train)

# Collect all the models
models = [("Logistic Regression", clf_lr),
          ("Random Forest Classifier", clf_rf),
          ("LinearSVC", clf_svc),
          ("KNeighbors", clf_knn)]

# Determine the best model
best_score = 0
best_model_name = ""
best_model = None

for model_tupule in models:

    model = model_tupule[1]
    name = model_tupule[0]

    y_pred = model.predict(x_val)
    score_train = model.best_score_
    score_val = model.score(x_val, y_val)

    if score_val > best_score:
        best_score = score_val
        best_model_name = name
        best_model = model

    report = classification_report(y_val, y_pred)

    print("******")
    print(name)
    print("Best score in the training set: ", score_train)
    print("Best score in the validation set: ", score_val)
    print("Full Classification report:")
    print(report)

print("**********")
print("Best model:", best_model_name)
print("Accuracy over validation set:", best_score)

model_pickle = open("../data/model.pkl", 'wb')
pkl.dump(best_model, model_pickle)
model_pickle.close()
