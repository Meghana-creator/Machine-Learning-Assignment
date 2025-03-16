#  Step 3: Build a Flask API for Model Deployment
# Let's create an API that accepts new spectral data and returns DON concentration predictions.


from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Load Model
model = joblib.load("random_forest_model.pkl")

# Initialize Flask App
app = Flask(__name__)

@app.route('/')
def home():
    return "DON Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON Data
        data = request.get_json()
        input_features = pd.DataFrame(data['features'])  # Expecting a dictionary with key 'features'

        # Ensure Data Matches Model Format
        if input_features.shape[1] != model.n_features_in_:
            return jsonify({"error": "Invalid input dimensions"}), 400

        # Predict
        prediction = model.predict(input_features)

        # Return Response
        return jsonify({"predicted_DON_concentration": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)



# The above program produces the output  Your API is now live at http://127.0.0.1:5000/

# The API accepts JSON data with a key named 'features' containing the input data. The API returns
# the predicted DON concentration as a list.
