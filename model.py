import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load and preprocess the data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Function to train the model
def train_model(data):
    # Define the features and target variable
    X = data.drop('price', axis=1)
    y = data['price']

    # Categorical and numerical feature names
    categorical_features = ['mainroad', 'guestroom', 'basement', 
                            'hotwaterheating', 'airconditioning', 
                            'prefarea', 'furnishingstatus']
    numerical_features = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']

    # Create a column transformer with preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(drop='first'), categorical_features)
        ],
        remainder='drop'  # discard non-specified columns
    )

    # Create a pipeline with preprocessing and model training
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                 ('model', LinearRegression())])

    # Fit the model on the training data
    pipeline.fit(X, y)
    return pipeline

# Function to predict house prices
def predict_price(model, area, bedrooms, bathrooms, stories, parking,
                  mainroad, guestroom, basement, hotwaterheating,
                  airconditioning, prefarea, furnishingstatus):
    
    # Create a DataFrame for the new input
    input_data = pd.DataFrame({
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
    })

    # Use the model to predict the price
    predicted_price = model.predict(input_data)
    return predicted_price[0]

# Load the data and train the model when the script runs
data = load_data('data/housing_data.csv')
model = train_model(data)