from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import joblib
import numpy as np
import os
# Get the base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_DIR = os.path.join(BASE_DIR, 'cropai/models')

# Load models and encoders
clf = joblib.load(os.path.join(MODEL_DIR, "crop_recommendation_model.pkl"))
crop_encoder = joblib.load(os.path.join(MODEL_DIR, "crop_label_encoder.pkl"))

reg = joblib.load(os.path.join(MODEL_DIR, "crop_yield_model.pkl"))
region_enc = joblib.load(os.path.join(MODEL_DIR, "region_encoder.pkl"))
soil_enc = joblib.load(os.path.join(MODEL_DIR, "soil_encoder.pkl"))
crop_enc = joblib.load(os.path.join(MODEL_DIR, "crop_encoder.pkl"))
weather_enc = joblib.load(os.path.join(MODEL_DIR, "weather_encoder.pkl"))

def safe_label_encode(encoder, label, field_name):
    if label in encoder.classes_:
        return encoder.transform([label])[0]
    else:
        return encoder.transform([encoder.classes_[0]])[0]

@csrf_exempt
def crop_recommendation_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        test_input = [
            data["N"], data["P"], data["K"],
            data["temperature"], data["humidity"],
            data["ph"], data["rainfall"]
        ]
        prediction = clf.predict([test_input])[0]
        crop_name = crop_encoder.inverse_transform([prediction])[0]
        return JsonResponse({"recommended_crop": crop_name})
    return JsonResponse({"error": "Only POST method allowed"}, status=405)

@csrf_exempt
def yield_prediction_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        encoded_input = [
            safe_label_encode(region_enc, data["Region"], "Region"),
            safe_label_encode(soil_enc, data["Soil_Type"], "Soil_Type"),
            safe_label_encode(crop_enc, data["Crop"], "Crop"),
            data["Rainfall_mm"],
            data["Temperature_Celsius"],
            int(data["Fertilizer_Used"]),
            int(data["Irrigation_Used"]),
            safe_label_encode(weather_enc, data["Weather_Condition"], "Weather_Condition"),
            data["Days_to_Harvest"]
        ]
        encoded_input = np.array(encoded_input).reshape(1, -1)
        yield_prediction = reg.predict(encoded_input)[0]
        return JsonResponse({"predicted_yield": round(float(yield_prediction), 2)})
    return JsonResponse({"error": "Only POST method allowed"}, status=405)
