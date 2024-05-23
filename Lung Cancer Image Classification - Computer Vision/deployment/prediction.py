import streamlit as st
import numpy as np
import cv2
from PIL import Image
from keras.models import load_model
from time import sleep

# Load the saved model
model = load_model('model3.h5')

# Define the labels
labels = {0: 'Benign', 1: 'Malignant', 2: 'Normal'}

# Preprocess the image to match the model's input requirements
def preprocess_image(image):
    image = image.resize((299, 299))  # Resize to the correct dimensions
    image = np.array(image)
    image = cv2.medianBlur(image, 5)  # Apply median blur
    image = image / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def run():

    # Streamlit interface
    st.title('Lung X-ray Classification')
    st.write("Upload a lung X-ray image to classify it as benign, malignant, or normal.")

    uploaded_file = st.file_uploader("Choose an X-ray image...", type=["jpg", "jpeg", "png"], help='Allowed file types: .jpg, .jpeg, .png')

    if uploaded_file is not None:

        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded X-ray.', use_column_width=True)

        # Preprocess the image
        processed_image = preprocess_image(image)

        # Make a prediction
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction, axis=1)[0]
        predicted_label = labels[predicted_class]
        probability = np.max(prediction)*100

        # Add progression
        bar = st.progress(0)
        for percent_complete in range(101):
            sleep(0.005)
            bar.progress(percent_complete)
        st.success('Prediction Completed!')

        # Display the prediction and probability
        st.write(f"**Result: {predicted_label}**")
        st.write(f"**Confidence: {probability:.2f}%**")
        
        # Interpret the prediction
        if predicted_label == 'Normal':
            st.write("The patient's lung appears normal, and there is no immediate need for further treatment.")
        elif predicted_label == 'Benign':
            st.write("The patient's lung shows a benign tumor. While this is typically non-cancerous, please consult with a doctor for comprehensive evaluation and advice on potential treatment options.")
        elif predicted_label == 'Malignant':
            st.write("The patient's lung exhibits a malignant tumor, indicating a serious condition that requires immediate medical attention. Please contact the patient and the doctor urgently to initiate appropriate treatment and care.")

if __name__ == "__main__":
    run()
