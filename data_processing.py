import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import joblib

# Load the dataset
df = pd.read_csv('data/housing_data.csv')

# Define features and target
X = df.drop('price', axis=1)
y = df['price']

# Define categorical and numerical columns
categorical_cols = ['mainroad', 'guestroom', 'basement',
                    'hotwaterheating', 'airconditioning', 'prefarea', 'furnishingstatus']
numerical_cols = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']

# Create a preprocessing pipeline
preprocessing = ColumnTransformer(
    transformers=[
        # Pass through numerical columns as they are
        ('num', 'passthrough', numerical_cols),
        # One-hot encode categorical columns
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

# Create a modeling pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessing),
    ('regressor', LinearRegression())  # Linear regression model
])

# Split data into training and testing set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'house_price_model.pkl')

print("Model trained and saved successfully.")
