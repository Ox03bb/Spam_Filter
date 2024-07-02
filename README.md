# Spam Filter Project



<div align="center">
    <img src="./img/sklearn.png" style="height: 80px; margin-right: 25px;">
    <img src="./img/fastapi.png" style="height: 80px;">
</div>

<br>

This project implements a spam classification system using machine learning and web technologies. The main objective is to classify email messages as either spam or non-spam (ham) with high accuracy.

## Features

- **Machine Learning Model**: Utilizes the Logistic Regression model from the `scikit-learn` library.
- **Web Framework**: Implements a RESTful API using `FastAPI` for easy integration and deployment.
- **High Accuracy**: Achieved an impressive accuracy of 95.6% on the test dataset.

## Project Structure
```
.
├── src
│ ├── data # Contains the dataset and the preprocessed data
| ├── model # Contains the trained model
| ├── test # Contains the test files
| ├── main.ipynb # Jupyter notebook for data analysis and model training
| ├── user.py # normaize the input data and predict the output
│ └── api.py # FastAPI application
├── img
│ ├── fastapi.png
│ └── sklearn.png
├── words.txt # important file for the model 
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Ox03bb/Spam_Filter.git
    cd spam-Spam_Filter
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the API**:
    Start the FastAPI server to serve the spam classification model:
    ```sh
    py src/api.py
    ```

2. **Make Predictions**:
    Send a POST request to the `/predict` endpoint with the email content to classify it as spam or non-spam. Example:
    ```sh
    curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'accept: application/json' -H 'Content-Type: application/json'  -d '{ "data": "Congratulations! You ve won a free $1000 Walmart gift card. Click here to claim your prize: http://example.com/winner. Offer expires soon!"}'
    ```
2. **Docs Endoint**:
    To see the documentation of the API, use this enpoint: /docs, and you can also use a swagger UI to test the API.

## Model Performance

- **Accuracy**: 95.6%
- The model was evaluated on a diverse dataset of spam and non-spam emails, demonstrating robust performance across different types of email content.
> **Note:** This project is still under development and is currently available in English.

