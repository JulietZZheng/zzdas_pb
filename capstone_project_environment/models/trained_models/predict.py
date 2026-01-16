#!/usr/bin/env python
"""
Prediction script for Random Forest model
Generated automatically
"""

import joblib
import numpy as np
import pandas as pd

def load_model():
    """Load the trained model and scaler"""
    model = joblib.load('best_regression_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

def predict(features_dict):
    """
    Make prediction on new data

    Parameters:
    -----------
    features_dict : dict
        Dictionary with feature names as keys and values
        Required features: ['gdp_per_capita', 'gdp_total', 'population_total', 'urban_population_percent', 'agricultural_land_percent', 'energy_use_per_capita', 'life_expectancy', 'forest_area_percent']

    Returns:
    --------
    float : Predicted value for pm25_air_pollution
    """
    model, scaler = load_model()

    # Create feature array in correct order
    feature_order = ['gdp_per_capita', 'gdp_total', 'population_total', 'urban_population_percent', 'agricultural_land_percent', 'energy_use_per_capita', 'life_expectancy', 'forest_area_percent']
    X = np.array([[features_dict[f] for f in feature_order]])

    # Scale features
    X_scaled = scaler.transform(X)

    # Make prediction
    prediction = model.predict(X_scaled)[0]

    return prediction

def predict_batch(df):
    """
    Make predictions on a DataFrame

    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with required feature columns

    Returns:
    --------
    numpy.array : Array of predictions
    """
    model, scaler = load_model()

    feature_order = ['gdp_per_capita', 'gdp_total', 'population_total', 'urban_population_percent', 'agricultural_land_percent', 'energy_use_per_capita', 'life_expectancy', 'forest_area_percent']
    X = df[feature_order].values

    X_scaled = scaler.transform(X)

    predictions = model.predict(X_scaled)

    return predictions

if __name__ == "__main__":
    # Example usage
    print("Model: Random Forest")
    print("Target: pm25_air_pollution")
    print("Features required: 8")

    # Example prediction (replace with actual values)
    example_features = {
        'gdp_per_capita': 0.0, 'gdp_total': 0.0, 'population_total': 0.0, 'urban_population_percent': 0.0, 'agricultural_land_percent': 0.0, 'energy_use_per_capita': 0.0, 'life_expectancy': 0.0, 'forest_area_percent': 0.0
    }

    try:
        pred = predict(example_features)
        print(f"\nExample prediction: {pred:.4f}")
    except Exception as e:
        print(f"\nError: {e}")
        print("Please provide actual feature values")
