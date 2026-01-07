from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# --- Load Model ---
model_path = 'model.pkl'

if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
else:
    model = None
    print("⚠️ WARNING: model.pkl not found. Please run train_model.py first.")

class_names = ['Setosa', 'Versicolor', 'Virginica']

@app.route('/')
def home():
    # Renders templates/first.html
    return render_template('first.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model not loaded. Run train_model.py!'}), 500

    try:
        # Get data from the form
        val = [float(request.form[k]) for k in ['sl', 'sw', 'pl', 'pw']]
        features = np.array([val])
        
        # Predict
        pred_idx = model.predict(features)[0]
        result_class = class_names[pred_idx]
        
        # Return JSON
        return jsonify({'class': result_class})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5002)