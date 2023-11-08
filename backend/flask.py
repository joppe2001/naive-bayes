from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Load the trained model and scaler
with open('model_and_scaler.pkl', 'rb') as file:
    scaler, model = pickle.load(file)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Assuming the data is a list of features: [age, salary]
    features = [data['age'], data['salary']]
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

