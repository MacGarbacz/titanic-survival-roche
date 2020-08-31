# Titanic - data science project 

## INTRODUCTION
This is simple data science project designed to predict whether a given person would survive the Titanic crash. It comes with a full script for feature expansion as well as a training script with multiple candidate architectures.
The best performing model is saved into a file and exposed via an API which accepts records in json format and returns predictions in json as well. A Dockerfile is included for ease of containerisation.

### IMPLEMENTATION

The project is implemented fully in Python and it was developed with the use of the PyCharm IDE. Throughout the development, standard Data Science packages were used - NumPy, Sklearn, Pandas, etc. The API functionality was implemented using Flask.

### HOW TO RUN

1. In order to run the feature expansion and training of the candidate models, execute the train.py script within the src package. Data visualisation and selection details available further in the README.md as well as a Jupyter notebook "Feature Visualisation and Selection" available in the notebooks package.

2. In order to run the API, execute the app.py script. The endpoint defaults to localhost, port 5000.

### Notes regarding TASKS:

#### TASK1 - organizational instructions

The repository was set up on GitHub as a public repository. The work for each of the subsequent tasks (with the exception for task 1) has been completed on a separate branch - one per task - and merged back onto the master branch. The branches have not been deleted post-merging and the state of the project at the completion of each task can be investigated by viewing a corresponding branch.

#### TASK2 - sense of humour

The joke was carefully selected and uploaded in a .txt file. Note: the joke is subject to change in an event of an even funnier joke being found. :)

#### TASK3 - good practices

Since making the existing code easier to read, run and reuse requires changes to the files concerned in tasks 4-6, I decided to split work on task 3 into two phases to be merged in separately - creating an alternate version of the README.md file, and making sure the code adheres to the good practices listed once the subsequent tasks are completed. Hence, two pull requests of the task 3 branch, one before work on the task 4 has been completed, and one at the end of the project.  

#### TASK4 - feature engineering

My approach to feature engineering was to investigate each of the attributes separately and decide on whether to include it in the final DataFrame object, and if so, what transformations were necessary to make sure the attribute will be useful to the model.
Along with the work done in the build_features.py, I decided to make use of a Jupyter Notebook for rapid experimentation and visualisation of the attributes, their values and their split among the two available classes. Therefore, the notebook offers a deeper look into the analysis and creation of functions applied to the datasets.

Breakdown by attribute:

* `PassengerId' - Used as an index only. Not used in the final DataFrame.

* `Survived` - Used as the target variable during training.

* `Pclass`  - As it is an categorical, ordinal variable with integer values, it was included in the final DataFrame without changes.

* `Name` - The attribute was used to extract titles like "Mr.", "Miss." etc. from names of passengers. It was deemed to be the only useful part of the attribute value.
The five most common titles were identified and a value in range 0-5 was assigned based on the title of each given passenger. Passengers without a title among the 5 most common one were put into the same class.

* `Sex` - This attribute was expanded into two one-hot encoded features since the sex is a non-ordinal categorical feature.

* `Age` - Since there were many various values for the attribute, a bucketization was performed where the value would be assigned to one of 5 age categories. The total age range was split so that the resulting categories would be of roughly the same size.
The new attribute with the category was created - `Age_cat`.

* `SibSp` -Used along the `SibSp` to create the `FamilySize` and `IsAlone` attributes just as in the starter code.

* `Parch` - Used along the `SibSp` to create the `FamilySize` and `IsAlone` attributes just as in the starter code.

* `Ticket` - Dropped from the DataFrame as there were too many unique values and there didn't seem to be a viable strategy to leverage the information.

* `Fare` - Similarly to the Age attribute, the Fare was bucketized into one of several categories. The resulting attribute was `Fare_cat`.

* `Cabin` - Dropped from the DataFrame as there were too many entries with NaN values (600+ in a set of 802 samples)

* `Embarked` - Expanded into 3 one-hot encoded features - `C`, `Q` and `S`.


The final set of attributes used during training was as follows:

*['Pclass', 'FamilySize', 'IsAlone', 'C', 'Q', 'S', 'female', 'male', 'Age_cat','Fare_cat', 'Title_value']*

The DataFrame didn't need any normalization or dealing with NaN values as the functions used to expand the features dealt with that automatically.

#### TASK5 - models

Given that the selection of a machine learning model might be very depended on the structure and the size of the dataset at hand, the approach to candidate model selection I've taken was to pick several different models which might have different strengths and weaknesses.
Then, once the training has been completed, the performance of each could be evaluated and the best performing model could be persisted in a file form.

The models I've chosen were:

* LinearRegression - since it's proven to work well for binary classification problems as well as relatively small datasets.

* RandomForestClassifier - as it was already provided as a candidate architecture.

* LinearSVC - since it's making use of the support vectors and provides wide support for penalty functions and has proven to be flexible for both dense and sparse datasets.

* KNeighbors - to include a classifier which makes direct use of distances between the samples.

#### TASK6 - measures

The overall strategy for determining the best performing model was to perform a grid search for each of the classifiers and their corresponding hyperparameters and then compare them using several different metrics. This way, we can perform some basic hyperparamter optimisation for each of the models and make sure that the results for each of the candidate models will be closer to optimal.

Once each of the models, along with the set of best hyperparameters, was fit to the training data, the validation data was used to evaluate their performance when presented with previously unseen records. This way the true accuracy of each of the models could be recorded.

The metrics used to make the final decision about the best performing model were : accuracy over training set, accuracy over validation set, and a full classification report containing precision, recall and f1 scores for each of the two available classes. Given the imbalance between the classes (50 vs 39 samples), the full classification report was necessary to determine the best model.
In the end, the best performing model was found to be the LinearSVC although the LogisticRegression classifier was a very close second.

Full results of the comparison generated by the train.py script can be found below.

******
`Logistic Regression`

`Best score in the training set:  0.81`

`Best score in the validation set:  0.81`

`Full Classification report:`

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.82      | 0.84   | 0.83     | 50      |
| 1            | 0.79      | 0.77   | 0.78     | 39      |
| accuracy     |           |        | 0.81     | 89      |
| macro avg    | 0.81      | 0.89   | 0.81     | 89      |
| weighted avg | 0.81      | 0.81   | 0.81     | 89      |

******
`Random Forest Classifier`

`Best score in the training set:  0.82`

`Best score in the validation set:  0.74`

`Full Classification report:`

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.75      | 0.82   | 0.78     | 50      |
| 1            | 0.74      | 0.64   | 0.68     | 39      |
| accuracy     |           |        | 0.74     | 89      |
| macro avg    | 0.74      | 0.73   | 0.73     | 89      |
| weighted avg | 0.74      | 0.74   | 0.74     | 89      |

******
`LinearSVC`

`Best score in the training set:  0.82`

`Best score in the validation set:  0.83`

`Full Classification report:`

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.83      | 0.88   | 0.85     | 50      |
| 1            | 0.83      | 0.77   | 0.80     | 39      |
| accuracy     |           |        | 0.83     | 89      |
| macro avg    | 0.83      | 0.82   | 0.83     | 89      |
| weighted avg | 0.83      | 0.83   | 0.83     | 89      |

******
`KNeighbors`

`Best score in the training set:  0.82`

`Best score in the validation set:  0.79`

`Full Classification report:`

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.79      | 0.84   | 0.82     | 50      |
| 1            | 0.78      | 0.72   | 0.75     | 39      |
| accuracy     |           |        | 0.79     | 89      |
| macro avg    | 0.79      | 0.78   | 0.78     | 89      |
| weighted avg | 0.79      | 0.79   | 0.79     | 89      |

**********
`Best model: LinearSVC`

`Accuracy over validation set: 0.83`

#### TASK7 - docker

The Dockerfile has been included along with the requirements.txt file. It specifies the Python version to be used, navigates to the working directory with the code (/src), installs necessary packages and runs the API via the app.py script.
Requirements.txt details packages used throughout development, mostly standard Data Science packages and Flask.

#### TASK8 - tests

The unit tests covering the code were split across two files. One covering the helper functions of the helpers.py and one for the build_fatures.py script. In each case, all functions present within the file were tested with a variety of inputs covering various edge cases and the overall behaviour of the functions was investigated.

Although not a test file per se, the test_request.py allows to verify proper behaviour of the API as it allows to send a sample request to the API and displays the result.

#### TASK9 - prediction api

The prediction API was implemented using Flask given the ease of set up of lightweight web services. In the app.py file, the best performing model is loaded in from the .pkl file and one endpoint was made available - /api which accepts POST messages containing the data record in the .json format. The record is then passed through the feature expansion script and used in the model to make a prediction. Finally, the prediction is returned as a json response.


