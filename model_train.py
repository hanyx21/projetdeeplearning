# Example of model_train.py
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def load_and_preprocess_data():
    data = pd.read_csv("C:/Users/amine/Desktop/dl-prjt/water_potability_paris2.csv")
    # Assume preprocessing is handled by data_processing.py
    return data

def build_model(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(input_shape,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')  # This suggests binary classification
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


def train_model(data):
    features = data.drop('Potability', axis=1)
    labels = data['Potability']
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = build_model(X_train_scaled.shape[1])
    model.fit(X_train_scaled, y_train, epochs=10, validation_data=(X_test_scaled, y_test))

    model.save('C:/Users/amine/Desktop/dl-prjt/model.h5')  # Save the model


if __name__ == '__main__':
    data = load_and_preprocess_data()
    train_model(data)
