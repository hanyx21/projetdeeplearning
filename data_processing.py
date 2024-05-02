import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def load_data():
    data = pd.read_csv('C:/Users/amine/Desktop/dl-prjt/water_potability_paris2.csv')
    return data

def preprocess_data(data):
    features_to_impute = data.columns.drop('Potability')
    imputer = SimpleImputer(strategy='mean')
    data[features_to_impute] = imputer.fit_transform(data[features_to_impute])
    
    features_to_scale = data.columns.drop('Potability')
    scaler = StandardScaler()
    data[features_to_scale] = scaler.fit_transform(data[features_to_scale])
    
    return data
#######################

# def preprocess_data(data_path):
#     # Charger les données
#     data = pd.read_csv(data_path)
    
#     # Sélectionner les colonnes à normaliser
#     features = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
#                 'Organic_carbon', 'Trihalomethanes', 'Turbidity', 'Latitude', 'Longitude']
    
#     # Initialiser et appliquer le StandardScaler
#     scaler = StandardScaler()
#     data[features] = scaler.fit_transform(data[features])
    
#     # Retourner les données normalisées
#     return data

# # Exemple d'utilisation de la fonction
# if __name__ == '__main__':
#     data_path = 'C:/Users/amine/Desktop/dl-prjt/water_potability_paris.csv'  # Remplacez par le chemin réel
#     normalized_data = preprocess_data(data_path)
#     print(normalized_data.head())