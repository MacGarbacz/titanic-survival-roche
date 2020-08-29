# Titanic - data science project 

## INTRODUCTION
This is simple data science project designed to predict whether a given person would survive the Titanic crash.


### IMPLEMENTATION



### Notes regarding TASKS:

#### TASK1 - organizational instructions

The repository was set up on GitHub as a public repository. The work for each of the subsequent tasks (with the exception for task 1) has been completed on a separate branch - one per task - and merged back onto the master branch. The branches have not been deleted post-merging and the state of the project at the completion of each task can be investigated by viewing a corresponding branch.

#### TASK2 - sense of humour

The joke was carefully selected and uploaded in a .txt file. Note: the joke is subject to change in an event of an even funnier joke being found. :)

#### TASK3 - good practices

Since making the existing code easier to read, run and reuse requires changes to the files concerned in tasks 4-6, I decided to split work on task 3 into two phases to be merged in separately - creating an alternate version of the README.md file, and making sure the code adheres to the good practices listed once the subsequent tasks are completed. Hence, two pull requests of the task 3 branch, one before work on the task 4 has been completed, and one at the end of the project.  

#### TASK4 - feature engineering

#### TASK5 - models

#### TASK6 - measures

******
Logistic Regression
Best score in the training set:  0.8129813664596274
Best score in the validation set:  0.8089887640449438

Full Classification report:

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.82      | 0.84   | 0.83     | 50      |
| 1            | 0.79      | 0.77   | 0.78     | 39      |
| accuracy     |           |        | 0.81     | 89      |
| macro avg    | 0.81      | 0.89   | 0.81     | 89      |
| weighted avg | 0.81      | 0.81   | 0.81     | 89      |

******
Random Forest Classifier
Best score in the training set:  0.8155046583850931
Best score in the validation set:  0.7415730337078652

Full Classification report:

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.75      | 0.82   | 0.78     | 50      |
| 1            | 0.74      | 0.64   | 0.68     | 39      |
| accuracy     |           |        | 0.74     | 89      |
| macro avg    | 0.74      | 0.73   | 0.73     | 89      |
| weighted avg | 0.74      | 0.74   | 0.74     | 89      |

******
LinearSVC
Best score in the training set:  0.8204503105590062
Best score in the validation set:  0.8314606741573034

Full Classification report:

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.83      | 0.88   | 0.85     | 50      |
| 1            | 0.83      | 0.77   | 0.80     | 39      |
| accuracy     |           |        | 0.83     | 89      |
| macro avg    | 0.83      | 0.82   | 0.83     | 89      |
| weighted avg | 0.83      | 0.83   | 0.83     | 89      |

******
KNeighbors
Best score in the training set:  0.8242003105590061
Best score in the validation set:  0.7865168539325843

Full Classification report:

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.79      | 0.84   | 0.82     | 50      |
| 1            | 0.78      | 0.72   | 0.75     | 39      |
| accuracy     |           |        | 0.79     | 89      |
| macro avg    | 0.79      | 0.78   | 0.78     | 89      |
| weighted avg | 0.79      | 0.79   | 0.79     | 89      |

**********
Best model: LinearSVC
Accuracy over validation set: 0.8314606741573034

#### TASK7 - docker

#### TASK8 - tests

### TASK9 - prediction api



