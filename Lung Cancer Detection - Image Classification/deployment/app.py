# Import libraries
import eda, prediction
import streamlit as st

# Add sidebar
navigation = st.sidebar.selectbox('Navigation', ['Home', 'Exploratory Data Analysis', 'Lung Cancer Prediction'])

st.sidebar.markdown('# About')

# Introduction
st.sidebar.write('''
This tool is designed to explore and predict lung cancer cases. It uses advanced data analysis and machine learning models to provide insights and predictions that can help medical professionals and researchers in understanding and addressing lung cancer effectively.
''')

# Features
st.sidebar.write('''### Key Features:
- **Exploratory Data Analysis**: Analyze the data to uncover patterns and insights related to lung cancer.
- **Lung Cancer Predictor**: Use predictive models to forecast the likelihood of lung cancer in patients.''')

# Target Audience
st.sidebar.write('''### Who can benefit?
- **Medical Professionals**: Enhance understanding and manage risks associated with lung cancer.
- **Researchers**: Analyze and model lung cancer datasets for better predictive accuracy.
- **Data Scientists**: Develop and evaluate machine learning models for lung cancer prediction.''')

# Tools
st.sidebar.write('''### Tools Utilized:
- `Python`: For backend operations and model computations.
- `Streamlit`: For creating this interactive web application.
- `Scikit-learn`: For implementing machine learning models.
- `Tensorflow`: For creating and training the Convolutional Neural Network (CNN) model used to classify the lung X-ray images.''')

# Define the Home Page
def show_home():
    
    st.image('./logo.png')
    
    st.markdown('---')
     
    st.write('''
    This tool provides functionalities for Exploratory Data Analysis and Prediction regarding lung cancer occurrences. 
    Use the navigation pane on the left to select the module you wish to utilize.
    ''')
    
    # Dataset
    st.write('#### 📈 Dataset')
    st.markdown('''
    The dataset is sourced reliably and contains pertinent information on lung cancer occurrences. For additional details or to download the dataset, visit
    [Lung Cancer Dataset](https://www.kaggle.com/datasets/adityamahimkar/iqothnccd-lung-cancer-dataset/data).
    ''')
    
    # Problem Statement
    st.write('#### ⚠️ Problem Statement')
    st.markdown('''
    The hospital faces a major difficulty in accurately diagnosing lung conditions from patient X-ray images. Specifically, it is difficult to predict whether a patient has a malignant, benign, or normal lung case based solely on the X-ray images. This diagnostic uncertainty can lead to delays in treatment, increased patient anxiety, and potentially inappropriate medical interventions. Addressing this issue is crucial to improving patient outcomes and ensuring timely and accurate diagnosis of lung conditions.
    ''')    
    
    # Objective
    st.write('#### 💡 Objective')
    st.markdown('''
    The goal of this project is to create a `Convolutional Neural Network (CNN)` model that accurately predicts lung conditions from X-ray images. It will distinguish between **malignant**, **benign**, and **normal** cases, primarily using `accuracy` as the evaluation metric. This aims to improve diagnostics, patient outcomes, and reduce uncertainties in clinical settings.
    ''')
    
# Create condition to access different pages
if navigation == 'Home':
    show_home()
elif navigation == 'Exploratory Data Analysis':
    eda.run()
elif navigation == 'Lung Cancer Prediction':
    prediction.run()
