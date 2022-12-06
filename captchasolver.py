# Import the necessary libraries
import cv2
import numpy as np
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model("captcha_model.h5")

# Read the captcha image
image = cv2.imread("captcha.png")

# Preprocess the image to prepare it for the model
image = cv2.resize(image, (150, 60))
image = image.astype("float32") / 255.0
image = np.expand_dims(image, axis=0)

# Use the trained model to make predictions on the captcha image
predictions = model.predict(image)

# Extract the predicted text from the model's output
predicted_text = "".join([chr(np.argmax(c)) for c in predictions[0]])

# Print the predicted text
print(predicted_text)

# This code uses a trained CNN model to make predictions on a captcha image and extract
# the predicted text. You can modify the code to use different machine learning algorithms or
# different preprocessing methods to improve the accuracy of the predictions.
