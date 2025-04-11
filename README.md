
# 🌾 CropAI - Crop Recommendation & Yield Prediction System

CropAI is a machine learning-powered web API that provides:
- **Crop Recommendation** based on soil and environmental features.
- **Yield Prediction** using regional, environmental, and crop-related inputs.

This project is designed for agricultural enhancement, helping farmers make data-driven decisions.

---

## 🚀 Features

- Recommend suitable crops based on soil nutrients, pH, rainfall, temperature, etc.
- Predict crop yield based on location, crop type, climate, and irrigation/fertilizer usage.
- Simple and responsive frontend using HTML, CSS, and JavaScript.
- RESTful API built with Django and integrated with trained ML models.
- CORS enabled for cross-origin frontend interaction.

---

## 🛠️ Tech Stack

- **Backend**: Python, Django, joblib
- **Machine Learning**: Scikit-learn
- **Frontend**: HTML, CSS, JavaScript (vanilla)
- **Model Files**: `joblib` serialized models for crop recommendation and yield prediction

---

## 📂 Directory Structure



---

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/CropAI.git
   cd CropAI
`

2.  **Create and Activate Virtual Environment**
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows
    
    ```
    
3.  **Install Dependencies**
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
4.  **Run the Server**
    
    ```bash
    python manage.py runserver
    
    ```
    

----------

## 🌐 API Endpoints

### 1. `POST /api/recommend-crop/`

Recommends a suitable crop based on soil and climate data.

**Request JSON**

```json
{
  "N": 90,
  "P": 40,
  "K": 40,
  "temperature": 22.0,
  "humidity": 80.0,
  "ph": 6.5,
  "rainfall": 200.0
}

```

**Response**

```json
{
  "recommended_crop": "Wheat"
}

```

----------

### 2. `POST /api/yield-predict/`

Predicts expected yield (in tons) based on agricultural inputs.

**Request JSON**

```json
{
  "Region": "North",
  "Soil_Type": "Clay",
  "Crop": "Wheat",
  "Rainfall_mm": 210.0,
  "Temperature_Celsius": 22.5,
  "Fertilizer_Used": true,
  "Irrigation_Used": false,
  "Weather_Condition": "Cloudy",
  "Days_to_Harvest": 130
}

```

**Response**

```json
{
  "predicted_yield": 2.85
}

```

----------

## 🔧 Enabling CORS

CORS is handled using `django-cors-headers`.

To enable CORS:

1.  Install:
    
    ```bash
    pip install django-cors-headers
    
    ```
    
2.  Add to `INSTALLED_APPS` and `MIDDLEWARE` in `settings.py`:
    
    ```python
    INSTALLED_APPS = [
        ...
        'corsheaders',
    ]
    
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        ...
    ]
    
    CORS_ALLOW_ALL_ORIGINS = True  # Or specify allowed origins
    
    ```
    

----------

## 📄 License

This project is for educational and research purposes.

----------

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

----------
