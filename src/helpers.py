#Function to assign age of a passenger to 1 of 6 available categories
def categorize_age(age):
    if age <= 19:
        return 1
    if age <= 26:
        return 2
    if age <= 33:
        return 3
    if age <= 45:
        return 4
    if age <= 81:
        return 5
    else:
        return 0

#Function to assign fare of a passenger to 1 of 5 available categories
def categorize_fare(fare):
    if fare <= 7.9:
        return 1
    if fare <= 13.0:
        return 2
    if fare <= 26.3:
        return 3
    if fare <= 73.5:
        return 4
    else:
        return 5

#Clean the DataFrame object to contain only attributes used during training
def delete_unnecessary_attributes(df):
    del (df["Name"])
    del (df["Ticket"])
    del (df["Cabin"])
    del (df["PassengerId"])
    del (df["Embarked"])
    del (df["Sex"])
    del (df["Age"])
    del (df["SibSp"])
    del (df["Parch"])
    del (df["Fare"])
    del (df["Survived"])
