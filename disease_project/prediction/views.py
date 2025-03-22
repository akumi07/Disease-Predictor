from django.shortcuts import render
from django.http import JsonResponse
import pickle
import numpy as np
import os

# Get the BASE directory (Health-predictor)
# Get the base directory (Health-predictor)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Get base directory
# model_path = os.path.join(BASE_DIR, "ml_model", "ml_model.pkl")  # Correct path

# if not os.path.exists(model_path):
#     raise FileNotFoundError(f"Model file not found at: {model_path}")

# with open(model_path, "rb") as file:
#     model = pickle.load(file)
# model = pickle.load(open("ml_model.pkl", "rb"))
model_path = r"E:\Health-predictor\ml_model\ml_model.pkl"
model = pickle.load(open(model_path, "rb"))

def predict_disease(request):
    if request.method == "POST":
        data = request.POST

        # Convert input data to a NumPy array
        features = np.array([[float(data['Pregnancies']), float(data['Glucose']), 
                              float(data['BloodPressure']), float(data['SkinThickness']),
                              float(data['Insulin']), float(data['BMI']),
                              float(data['DiabetesPedigreeFunction']), float(data['Age'])]])

        # Make a prediction
        prediction = model.predict(features)
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
        
        return JsonResponse({"prediction": result})

    return render(request, "index.html")
