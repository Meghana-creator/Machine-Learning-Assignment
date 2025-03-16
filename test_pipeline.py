# Step 2: Write Unit Tests for Core Functionalities
# Use pytest to ensure everything works as expected.

import pytest
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

# Load Cleaned Data
df = pd.read_csv("Cleaned_MLE_Assignment.csv")
X = df.drop(columns=['DON_Concentration'])
y = df['DON_Concentration']

# Load Model
model = joblib.load("random_forest_model.pkl")

def test_data_shape():
    """Ensure dataset has enough samples and features."""
    assert X.shape[0] > 100, "Not enough training samples"
    assert X.shape[1] > 5, "Not enough features"

def test_model_prediction():
    """Ensure model predicts a valid output."""
    sample_input = X.iloc[:1]
    prediction = model.predict(sample_input)
    assert prediction.shape == (1,), "Prediction shape is incorrect"
    assert prediction[0] >= 0, "Prediction should be non-negative"

