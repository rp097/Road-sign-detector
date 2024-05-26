from flask import Flask, request, render_template
import tensorflow as tf
#from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import io

app = Flask(__name__)
#model = tf.keras.models.load_model('road_sign_detector_model_1.h5')

# class_names = [
#     'Bus stop', 'Give way', 'Horn Prohibited', 'Hotel',
#     'Maximum speed limit (90km:h)', 'Narrow road', 'No entry',
#     'No entry for goods vehicles', 'No entry for motor vehicles',
#     'No left turn', 'No overtaking', 'No parking', 'No right turn', 'No stopping',
#     'No vehicles in both directions', 'One-way traffic', 'Parking', 'Road Hump',
#     'Turn left', 'Turn right'
# ]

@app.route('/')
def upload_image():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
