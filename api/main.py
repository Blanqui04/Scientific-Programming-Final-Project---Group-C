from fastapi import FastAPI, Query
import joblib
import pandas as pd

# Create FastAPI app
app = FastAPI(
    title="Breast Cancer Diagnosis API",
    description="API for predicting diagnosis using a KNN model",
    version="1.0"
)

# Load model and feature names
knn_model = joblib.load("knn_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# Root endpoint
@app.get("/")
def root():
    return {"status": "API is running"}


# Prediction endpoint
@app.post("/predict")
def predict(
    mean_radius: float = Query(...),
    mean_texture: float = Query(...),
    mean_smoothness: float = Query(...),
    mean_compactness: float = Query(...),
    mean_concavity: float = Query(...),
    mean_symmetry: float = Query(...),
    mean_fractal_dimension: float = Query(...),

    radius_error: float = Query(...),
    texture_error: float = Query(...),
    smoothness_error: float = Query(...),
    compactness_error: float = Query(...),
    concavity_error: float = Query(...),
    concave_points_error: float = Query(...),
    symmetry_error: float = Query(...),
    fractal_dimension_error: float = Query(...),

    worst_smoothness: float = Query(...),
    worst_compactness: float = Query(...),
    worst_concavity: float = Query(...),
    worst_symmetry: float = Query(...),
    worst_fractal_dimension: float = Query(...)
    ):
        data = {
             "mean_radius": mean_radius,
             "mean_texture": mean_texture,
             "mean_smoothness": mean_smoothness,
             "mean_compactness": mean_compactness,
             "mean_concavity": mean_concavity,
             "mean_symmetry": mean_symmetry,
             "mean_fractal_dimension": mean_fractal_dimension,
             "radius_error": radius_error,
             "texture_error": texture_error,
             "smoothness_error": smoothness_error,
             "compactness_error": compactness_error,
             "concavity_error": concavity_error,
             "concave_points_error": concave_points_error,
             "symmetry_error": symmetry_error,
             "fractal_dimension_error": fractal_dimension_error,
             "worst_smoothness": worst_smoothness,
             "worst_compactness": worst_compactness,
             "worst_concavity": worst_concavity,
             "worst_symmetry": worst_symmetry,
             "worst_fractal_dimension": worst_fractal_dimension,
        }

        # Convert input data to DataFrame
        X = pd.DataFrame([data])
        X = X[feature_names]

        # Prediction
        prediction = int(knn_model.predict(X)[0])
        proba = knn_model.predict_proba(X)[0]
        probability_benign = float(proba[1])
        probability_malignant = float(proba[0])
        label = "Benign" if prediction == 1 else "Malignant"

        return {
            "diagnosis": prediction,
            "label": label,
            "probability_benign": probability_benign,
            "probability_malignant": probability_malignant
        }
