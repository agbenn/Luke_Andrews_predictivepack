import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score


def load_data(file_path='/Users/andrewbennett/Documents/bse/computing_for_data_science/hw3/sample_diabetes_mellitus_data.csv'): 
    if os.path.exists(file_path) and '.csv' in file_path: 
        return pd.read_csv(file_path)
    else:
        print('file does not exist')
        return None
    
def get_training_data(df): 
    X = df[['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']]
    y = df['diabetes_mellitus']
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.4, random_state=42)
    return X_train, X_test, y_train, y_test

def drop_na_rows_diabetes(df):
    df = df.dropna(subset=['age', 'gender', 'ethnicity'])
    return df

def fillna_subset_diabetes(df):
    df[['height', 'weight']] = df[['height', 'weight']].fillna(df[['height', 'weight']].mean())
    return df

def generate_dummy_ethnicity_variables(df): 
    encoder = LabelEncoder()
    df['ethnicity'] = encoder.fit_transform(df['ethnicity'])
    return df

def convert_gender_to_binary(df): 
    df['is_male'] = ''
    df['is_male'].loc[df['gender'] == 'M'] = True
    df['is_male'].loc[df['gender'] == 'F'] = False
    return df

def get_trained_model(x_train, y_train): 
    logisticRegr = LogisticRegression()
    logisticRegr.fit(x_train, y_train)
    return logisticRegr

def get_predictions(logisticRegr, x_train, x_test):
    
    x_train['predictions'] = logisticRegr.predict(x_train)
    x_train['prediction_probability'] = logisticRegr.predict_proba

    x_test['predictions'] = logisticRegr.predict(x_test)
    x_test['prediction_probability'] = logisticRegr.predict_proba

    return x_train, x_test

def get_accuracy(y_predict, y_actual):
    return roc_auc_score(y_actual, y_predict)




