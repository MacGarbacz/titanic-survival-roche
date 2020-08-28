import pandas as pd
from src import helpers as h


# A function to expand the existing columns of non-ordinal categorical features
# into one-hot encoded features and perfom bucketization on those feature that permit it.
# Returns the expanded, cleaned DataFrame object containing the attributes and the target variable
def feature_expansion(dataset):
    # Read in the data into a DataFrame
    df = pd.read_csv("../data/" + dataset + ".csv", sep=";")

    # Record the target variable
    target = df["Survived"]

    # Introduce two new variables - total family size and a binary flag for solo travellers
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df["IsAlone"] = 0
    df.loc[df["FamilySize"] == 1, "IsAlone"] = 1

    # Expand the Embarked variable into one-hot encoded features
    embarked_onehot_features = pd.get_dummies(df['Embarked'])
    df = pd.concat([df, embarked_onehot_features], axis=1)

    # Expand the Sex variable into one-hot encoded features
    sex_onehot_features = pd.get_dummies(df['Sex'])
    df = pd.concat([df, sex_onehot_features], axis=1)

    # Perform bucketization on the Age attribute
    df['Age_cat'] = df['Age'].apply(h.categorize_age)

    # Perform bucketization on the Fare attribute
    df['Fare_cat'] = df['Fare'].apply(h.categorize_fare)

    # Drop attributes which won't be used for the training
    h.delete_unnecessary_attributes(df)

    return df, target

feature_expansion('train')