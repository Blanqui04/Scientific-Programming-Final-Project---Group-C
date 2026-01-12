# Breast Cancer Diagnosis API 🔬

This repository contains a **REST API** built with **FastAPI** that exposes a trained **K-Nearest Neighbors (KNN)** model for breast cancer diagnosis.
The API allows users to input clinical features extracted from medical data and returns:
- the predicted diagnosis (malignant or benign)
- the associated class probabilities

The FastAPI implementation is located in the `api` folder, with the main application script named `main.py`.

## Table of contents 📋
1. [Requirements](#requirements-)
2. [Running the API](#running-the-api-)
3. [API documentation (Swagger)](#api-documentation-swagger-)
4. [API endpoint](#api-endpoint-)
5. [Testing the API](#testing-the-api-)
6. [Notes](#notes-)

## Requirements 🛠️

Make sure you have Python 3.9 or later installed.
Install the required dependencies with:

```bash
pip install -r requirements.txt
```
Main dependences:
- fastapi
- uvicorn
- scikit-learn
- pandas
- joblib

## Running the API 🚀
From the root directory of the project, run:

```bash
uvicorn api.main:app --reload
```
If the API starts correctly, you should see:
Uvicorn running on http://127.0.0.1:8000

## API documentation (Swagger) 📖
FastAPI automatically generates interactive documentation.
To acess it, open your browser and go to: http://127.0.0.1:8000/docs

From there, you can:
- view available endpoints
- fill in feature values
- execute predictions directly from the browser

## API endpoint 🔌
### `POST /predict`
This endpoint predicts breast cancer diagnosis based on clinical features.
**Input**
- Each feature is provided as a separate input field (query parameter)
- All features must be numeric (`float` values)
- This design facilitates manual testing and improves interpretability of the model inputs
**Output**
The API returns:
- `diagnosis`: numerical prediction (`0`= Malignant, `1` = Benign)
- `label`: human-readable diagnosis.
- `probability_malignant`
- `probability_benign`

Example response:

{ 
  
  "diagnosis": 0,  
  "label": "Malignant",  
  "probability_malignant": 1.0,  
  "probability_benign": 0.0  
  
}
## Testing the API 🎯
The API was tested manually using the Swagger interface.

Testing procedure:
1. Start the API locally.
2. Open `http://127.0.0.1:8000/docs`.
3. Use the `/predict` endpoint.
4. Fill in the feature values.
5. Execute the request and verify the returned prediction and probabilities.

## Notes ⚠️
- The KNN model was trained using cleaned data.
- Feature order is enforced during interface to match the training phase.
- Class probabilities are derived from the proportion of nearest neighbors.
- Extreme probability values (0 or 1) may occur due to the nature of KNN.




