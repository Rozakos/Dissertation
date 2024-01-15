from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import json
import psycopg2  # Ensure psycopg2 or psycopg2-binary is imported
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize Flask application
application = Flask(__name__)
app = application

@app.route('/')
def index():
    # Render the index page
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        # Render the home page for GET requests
        return render_template('home_page.html')
    else:
        # Handle POST request for data prediction
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),  # Corrected field name
            writing_score=float(request.form.get('writing_score'))   # Corrected field name
        )

        # Convert the data to a DataFrame for processing
        pred_df = data.get_data_as_data_frame()
        print("Data for prediction:", pred_df)

        # Predicting using the pipeline
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        print("Prediction results:", results)

        # Render the home page with prediction results
        return render_template('home_page.html', results=results[0])

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
