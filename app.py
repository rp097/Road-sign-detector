from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import io

app = Flask(__name__)
model = tf.keras.models.load_model('road_sign_detector_model_1.h5')

class_names = [
    'Bus stop', 'Give way', 'Horn Prohibited', 'Hotel',
    'Maximum speed limit (90km:h)', 'Narrow road', 'No entry',
    'No entry for goods vehicles', 'No entry for motor vehicles',
    'No left turn', 'No overtaking', 'No parking', 'No right turn', 'No stopping',
    'No vehicles in both directions', 'One-way traffic', 'Parking', 'Road Hump',
    'Turn left', 'Turn right'
]

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            try:
                # Convert the FileStorage object to a byte stream
                file_stream = io.BytesIO(file.read())
                # Load the image from the byte stream
                image = load_img(file_stream, target_size=(32, 32))
                image = img_to_array(image)
                image = np.expand_dims(image, axis=0) / 255.0
                prediction = model.predict(image)
                class_idx = np.argmax(prediction, axis=1)[0]
                class_name = class_names[class_idx]
                return f'Predicted Class: {class_name}'
            except Exception as e:
                return f"An error occurred: {str(e)}"
    return '''
    <!doctype html>
    <title>Upload an Image</title>
    <h1>Upload a Road Sign Image</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
