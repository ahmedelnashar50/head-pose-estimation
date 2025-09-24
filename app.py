from flask import Flask, request, jsonify, send_file, render_template
import os
import shutil
import pickle
from processing import process_image, process_video

# Create Flask app
app = Flask(__name__)

# Load trained model
with open('svr_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template("upload.html")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty filename"})

    temp_file = f"temp_{file.filename}"
    file.save(temp_file)

    filename = file.filename.lower()

    try:
        if filename.endswith((".jpg", ".jpeg", ".png")):
            output_path = "output_image.jpg"
            processed_path, _ = process_image(temp_file, model, output_path)

        elif filename.endswith((".mp4", ".avi", ".mov", ".mkv")):
            output_path = "output_video.mp4"
            processed_path = process_video(temp_file, model, output_path)

        else:
            os.remove(temp_file)
            return jsonify({"error": "Unsupported file type"})

        os.remove(temp_file)

        return send_file(processed_path, as_attachment=True)

    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
