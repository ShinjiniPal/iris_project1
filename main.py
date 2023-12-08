# Importing necessary libraries
import os
import json
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import GridSearchCV, train_test_split
from joblib import dump
import pandas as pd

# Function to read data from CSV files in a specified directory
def get_data(base_dir):
    data_file_names = [x for x in os.listdir(base_dir) if x.endswith('.csv')]       # Retrieve the list of CSV file names in the directory
    data = {}
    for name in data_file_names:         # Loop through each file name and read its content into a DataFrame
        path_file = os.path.join(base_dir, name)
        data[name] = pd.read_csv("Iris.csv")
    return data

# Function to split the data into training and testing sets
def split_data(data, test_size=0.2, random_state=42):
    df = data['iris.csv']   #Select the DataFrame for the 'iris.csv' file

    # Drop the 'Id' column
    df = df.drop('Id', axis=1, errors='ignore')
    
    # Separate features (X) and target variable (y)
    X = df.drop('Species', axis=1)
    y = df['Species']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return {'X_train': X_train, 'X_test': X_test, 'y_train': y_train, 'y_test': y_test}

# Function to train a logistic regression model
def train_model(X_train, y_train):
    log_reg = LogisticRegression()
    model = log_reg.fit(X_train, y_train)
    return model


# Function to save the trained model to a file
def save_model(model):
    dump(model, "iris_prediction.joblib")        # Save the model using joblib
    print("Model saved")
