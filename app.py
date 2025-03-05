from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('house_price_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    area = float(request.form['area'])
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    stories = float(request.form['stories'])
    parking = float(request.form['parking'])
    mainroad = request.form['mainroad']
    guestroom = request.form['guestroom']
    basement = request.form['basement']
    hotwaterheating = request.form['hotwaterheating']
    airconditioning = request.form['airconditioning']
    prefarea = request.form['prefarea']
    furnishingstatus = request.form['furnishingstatus']

    # Prepare feature vector, format it as DataFrame
    input_data = pd.DataFrame(
        {
            'area': [area],
            'bedrooms': [bedrooms],
            'bathrooms': [bathrooms],
            'stories': [stories],
            'parking': [parking],
            'mainroad': [mainroad],
            'guestroom': [guestroom],
            'basement': [basement],
            'hotwaterheating': [hotwaterheating],
            'airconditioning': [airconditioning],
            'prefarea': [prefarea],
            'furnishingstatus': [furnishingstatus],
        }
    )

    # Make prediction
    predicted_price = model.predict(input_data)[0]

    return render_template('index.html', prediction=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)