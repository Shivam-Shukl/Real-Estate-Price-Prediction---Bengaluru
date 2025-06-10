#flask -cors
import pandas as pd
import numpy as np
import sklearn
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
# Load the cleaned data (assuming Cleaned_data.csv exists in the same directory)
data = pd.read_csv("Cleaned_data.csv")
# Load the trained Ridge model (assuming RidgeModel.pkl exists in the same directory)
pipe = pickle.load(open("RidgeModel.pkl",'rb'))

@app.route('/')
def index():
    # Get unique sorted locations from the data to populate the dropdown
    locations = sorted(data['location'].unique())
    # Render the index.html template, passing the locations data
    return render_template("index.html", locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data from the POST request
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')

    # Print the received data for debugging purposes
    print(f"Received data: Location={location}, BHK={bhk}, Bath={bath}, SqFt={sqft}")

    try:
        # Convert numerical inputs to appropriate types
        # Using float for sqft for consistency with typical real estate data
        total_sqft = float(sqft)
        # Using int for bhk and bath as they are counts
        num_bhk = int(bhk)
        num_bath = int(bath)

        # Create a DataFrame for prediction.
        # Ensure the column names match what your model was trained on.
        # The order of columns in the DataFrame must match the order expected by your model.
        # Corrected: input DataFrame creation to use `num_bhk` for 'bhk' column.
        input_data = pd.DataFrame([[location, total_sqft, num_bath, num_bhk]],
                                  columns=['location', 'total_sqft', 'bath', 'bhk'])

        # Make the prediction using the loaded pipeline
        prediction = pipe.predict(input_data)[0] * 1e5 # Multiply by 1e5 as per your latest code

        # Return the prediction as a string
        # Round the prediction to two decimal places for better readability
        return str(round(prediction, 2))

    except ValueError:
        # Handle cases where input conversion fails (e.g., non-numeric input for BHK, Bath, SqFt)
        print("Error: Invalid input for numerical fields. Please enter valid numbers.")
        return "Error: Invalid numerical input.", 400 # Return a bad request status code
    except Exception as e:
        # Catch any other unexpected errors during prediction
        print(f"An error occurred during prediction: {e}")
        return "Error: Could not predict price.", 500 # Return an internal server error status code


if __name__ == "__main__":
    # In a production environment like Render, Gunicorn will handle running the app.
    # The app.run() part below is primarily for local development.
    app.run(debug=True, port=5001)
