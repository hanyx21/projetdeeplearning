import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def load_data():
    data = pd.read_csv('C:/Users/amine/Desktop/dl-prjt/water_potability.csv')
    return data

def preprocess_data(data):
    features_to_impute = data.columns.drop('Potability')
    imputer = SimpleImputer(strategy='mean')
    data[features_to_impute] = imputer.fit_transform(data[features_to_impute])
    
    features_to_scale = data.columns.drop('Potability')
    scaler = StandardScaler()
    data[features_to_scale] = scaler.fit_transform(data[features_to_scale])
    
    return data
