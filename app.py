from flask import Flask, request, render_template
from model import predict_price, model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Gather fields from the form
        area = request.form.get('area')
        bedrooms = request.form.get('bedrooms')
        bathrooms = request.form.get('bathrooms')
        stories = request.form.get('stories')
        parking = request.form.get('parking')
        mainroad = request.form.get('mainroad')
        guestroom = request.form.get('guestroom')
        basement = request.form.get('basement')
        hotwaterheating = request.form.get('hotwaterheating')
        airconditioning = request.form.get('airconditioning')
        prefarea = request.form.get('prefarea')
        furnishingstatus = request.form.get('furnishingstatus')

        # Validate that all inputs are filled and valid
        if (area and bedrooms and bathrooms and stories and parking and 
            mainroad and guestroom and basement and hotwaterheating and 
            airconditioning and prefarea and furnishingstatus):

            try:
                # Convert completed fields to the appropriate types
                area = float(area)
                bedrooms = int(bedrooms)
                bathrooms = int(bathrooms)
                stories = int(stories)
                parking = int(parking)

                # Call the prediction function using the trained model
                predicted_price_value = predict_price(model, area, bedrooms, bathrooms, stories,
                                                      parking, mainroad, guestroom, basement,
                                                      hotwaterheating, airconditioning, prefarea,
                                                      furnishingstatus)

                return render_template('index.html', predicted_price=predicted_price_value)

            except ValueError:
                # If conversion fails, return to the original form with empty prediction
                return render_template('index.html', predicted_price=None)

        # If any field is empty, set predicted_price to None
        return render_template('index.html', predicted_price=None)

    return render_template('index.html', predicted_price=None)

if __name__ == '__main__':
    app.run(debug=True)