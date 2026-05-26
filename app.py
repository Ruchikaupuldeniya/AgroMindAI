from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('model/crop_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    features = [
        float(request.form['N']),
        float(request.form['P']),
        float(request.form['K']),
        float(request.form['temperature']),
        float(request.form['humidity']),
        float(request.form['ph']),
        float(request.form['rainfall'])
    ]

    final_features = [np.array(features)]

    prediction = model.predict(final_features)

    return render_template(
        'result.html',
        prediction_text=prediction[0]
    )

if __name__ == "__main__":
    app.run(debug=True)