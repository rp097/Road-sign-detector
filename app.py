from flask import Flask, request, render_template, redirect, url_for
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import io

app = Flask(__name__)
model = tf.keras.models.load_model('road_sign_detector_model_1.h5')

class_names = [
    'Bus stop', 'Give way', 'Horn Prohibited', 'Hotel',
    'Maximum speed limit (90km/h)', 'Narrow road', 'No entry',
    'No entry for goods vehicles', 'No entry for motor vehicles',
    'No left turn', 'No overtaking', 'No parking', 'No right turn', 'No stopping',
    'No vehicles in both directions', 'One-way traffic', 'Parking', 'Road Hump',
    'Turn left', 'Turn right'
]

@app.route('/')
def upload_image():
    return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             try:
#                 # Convert the FileStorage object to a byte stream
#                 file_stream = io.BytesIO(file.read())
#                 # Load the image from the byte stream
#                 image = load_img(file_stream, target_size=(32, 32))
#                 image = img_to_array(image)
#                 image = np.expand_dims(image, axis=0) / 255.0
#                 prediction = model.predict(image)
#                 class_idx = np.argmax(prediction, axis=1)[0]
#                 class_name = class_names[class_idx]
#                 return redirect(url_for('show_prediction', prediction=class_name))
#             except Exception as e:
#                 return redirect(url_for('show_prediction', error=str(e)))

# @app.route('/prediction')
# def show_prediction():
#     prediction = request.args.get('prediction')
#     error = request.args.get('error')
#     return render_template('prediction.html', prediction=prediction, error=error)

if __name__ == '__main__':
    app.run(debug=True)
