# Heart Disease Prediction Web App

This project is a Machine Learning web application that predicts the likelihood of heart disease based on patient medical data.

The model was trained using the UCI Heart Disease dataset and deployed through a simple web interface where users can enter medical parameters and receive a prediction.

## Features

* Machine Learning model built with Python and Scikit-learn
* Random Forest classifier for prediction
* Web interface using Flask
* User inputs medical data through a web form
* Automatic preprocessing and encoding of categorical features
* Real-time prediction results

## Technologies Used

* Python
* Scikit-learn
* Flask
* Pandas
* NumPy

## Dataset

The model was trained on the UCI Heart Disease dataset which includes clinical parameters such as:

* Age
* Sex
* Chest pain type
* Resting blood pressure
* Cholesterol
* Fasting blood sugar
* ECG results
* Maximum heart rate
* Exercise-induced angina
* ST depression
* Slope of ST segment
* Number of major vessels
* Thalassemia

## How It Works

1. The dataset is preprocessed and cleaned.
2. Categorical features are encoded.
3. A Random Forest model is trained.
4. A Flask server hosts the prediction API.
5. Users enter patient information through the web form.
6. The model returns a prediction for heart disease risk.

## Future Improvements

* Improve model accuracy with feature engineering
* Add better UI for the web interface
* Deploy the application online
* Add probability prediction

## Author

Ahmed Abdelsattar
