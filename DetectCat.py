import numpy as np

import tensorflow as tf

from tensorflow.keras.preprocessing import image
from tensorflow import keras
from IPython.display import Image
from tensorflow.keras.applications import imagenet_utils
from PIL import Image


mobileNetModel = tf.keras.applications.mobilenet.MobileNet()


image_path = 'dataSamples/'

def prepare_image(file):
    img = Image.open(image_path + file)
    img = img.resize((224, 224))  # Resize the image to (224, 224)
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

image_file_name = 'Sample11.JPG'

preprocessed_image = prepare_image(image_file_name)

results = mobileNetModel.predict(preprocessed_image)

result = imagenet_utils.decode_predictions(results)[0][0][1]

print(result)

