# 🧩 Head Pose Estimation (MediaPipe + SVR)

This repository provides a solution for estimating **head pose angles** (pitch, yaw, roll) from human face images and videos.  

The system combines:  
- **MediaPipe FaceMesh** → to extract dense 3D facial landmarks  
- **Support Vector Regression (SVR)** → to predict head orientation from the landmarks  

The implementation supports **both API-based and web-based interfaces**, making it flexible for integration into larger applications or direct usage.

---

## 📂 Repository Layout

head_pose_estimation/

├── app.py          # Flask app (web interface with HTML templates)

├── main.py         # FastAPI app (REST API with Swagger docs)

├── processing.py   # Shared utilities for image & video processing

├── model.ipynb     # Notebook for training & evaluation

├── AFLW2000/       # Dataset folder (see dataset link below)

├── outputs/        # Saved results (images/videos with pose overlay)

├── templates/      # HTML templates for Flask frontend

├── requirements.txt # Required Python packages

├── .gitignore      # Ignored files (venv, dataset, etc.)

└── README.md       # Project documentation

---

## 📊 Dataset Information

This project is based on the **AFLW2000-3D dataset**, which contains **2000 face images** annotated with 3D landmarks and pose angles.  

- **Source:** [AFLW2000-3D on Kaggle](https://www.kaggle.com/datasets)  
- **Annotations:** Pitch, yaw, and roll angles + 68 3D landmarks  
- **Usage:** Suitable for head pose estimation, facial landmark detection, and related tasks  

---

## 🚀 Running the Applications

### Option 1: Flask (with HTML upload form)
```bash
python app.py
```
Visit → http://127.0.0.1:5000/

### Option 2: FastAPI (interactive API docs)
```bash
uvicorn main:app --reload
```
Visit → http://127.0.0.1:8000/docs

---

## 🧠 Model Workflow

### Data Preprocessing (model.ipynb)

Extract landmarks from dataset

Align inputs for regression

### Model Training

Train SVR for each angle (pitch, yaw, roll)

### Prediction

For a new image or video → extract landmarks → pass to trained SVR → get angles

### Visualization

Render 3D orientation axes on face in images/videos

### Model Saving

```bash
import joblib
joblib.dump(model, "svr_model.pkl")
```
---

## 📌 Next Steps

✅ Enable real-time webcam streaming

✅ Extend with deep learning models for improved accuracy

✅ Provide deployment examples (Docker, Hugging Face Spaces, Streamlit)

---

## 👤 Author

Developed by Ahmed Elnashar



Visit → http://127.0.0.1:8000/docs
