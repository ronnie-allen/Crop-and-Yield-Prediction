import joblib
import numpy as np

# Load models and encoders only once
clf = joblib.load("models/crop_recommendation_model.pkl")
crop_encoder = joblib.load("models/crop_label_encoder.pkl")
reg = joblib.load("models/crop_yield_model.pkl")
region_enc = joblib.load("models/region_encoder.pkl")
soil_enc = joblib.load("models/soil_encoder.pkl")
crop_enc = joblib.load("models/crop_encoder.pkl")
weather_enc = joblib.load("models/weather_encoder.pkl")

def safe_label_encode(encoder, label, field_name):
    if label in encoder.classes_:
        return encoder.transform([label])[0]
    return encoder.transform([encoder.classes_[0]])[0]

def recommend_crop(data):
    test_crop_input = [[
        data['N'], data['P'], data['K'], data['temperature'],
        data['humidity'], data['ph'], data['rainfall']
    ]]
    pred_index = clf.predict(test_crop_input)[0]
    pred_label = crop_encoder.inverse_transform([pred_index])[0]
    return pred_label

def predict_yield(data):
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
    return reg.predict(encoded_input)[0]
