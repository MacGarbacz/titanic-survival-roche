import pandas as pd
from src import helpers as h


# A function to expand the existing columns of non-ordinal categorical features
# into one-hot encoded features and perfom bucketization on those feature that permit it.
# Returns the expanded, cleaned DataFrame object containing the attributes and the target variable
def feature_expansion(dataset, mode):
    # Read in the data into a DataFrame
    if mode == 'api':
        df = dataset
    elif mode == 'train' or mode == 'test':
        df = pd.read_csv("../data/" + dataset + ".csv", sep=";")

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

    # Extract titles from names and then convert the titles into title categories
    df['Title'] = df['Name'].apply(h.extract_title)
    df['Title_value'] = df['Title'].apply(h.convert_title)

    # Drop attributes which won't be used for the training
    h.delete_unnecessary_attributes(df)

    # Add columns if record relayed via an api call
    if mode == 'api':
        columns = ['male', 'female', 'C', 'S', 'Q']
        for col in columns:
            if col not in df.columns.values.tolist():
                df[col] = 0

        valid_order = ['Pclass', 'FamilySize', 'IsAlone', 'C', 'Q', 'S', 'female', 'male', 'Age_cat',
                       'Fare_cat', 'Title_value']

        # Reorder the columns
        df = df[valid_order]

    return df
