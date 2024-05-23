import streamlit as st
import pandas as pd
import os
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px

# Create the main program
def run():
    
    # Load the data from the CSV file
    cases_df = pd.read_csv('class_distribution.csv')

    # Add a title for the Streamlit app
    st.title("Exploratory Data Analysis")
    
    # Add subtitle
    st.write('''Choose what to visualize:''')
    
    # Create a multi-select dropdown for choosing visualization type
    visualization_type = st.multiselect('Select Visualization:', ('Class Distribution', 'Images'))

    if 'Class Distribution' in visualization_type:
        # Create an interactive bar chart with Plotly
        st.subheader('Number of Images in Each Case Category')
        fig = px.bar(cases_df, x='Case Category', y='Number of Images',
                     color='Case Category',
                     labels={'Number of Images': 'Number of Images', 'Case Category': 'Case Category'},
                     height=400,
                     color_discrete_sequence=['lightsteelblue', 'navajowhite', 'lightsalmon'])
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig)

        # Add additional information if necessary
        st.write('''The bar chart shows the distribution of images for three classes of lung conditions.''')
        st.write('''1. **Malignant Cases**: Most numerous with 561 images, indicating a significant focus on capturing cancerous lung conditions, likely due to their complexity and severity.''')
        st.write('''2. **Normal Cases**: There are 416 images, indicating a similar focus on capturing what healthy lungs look like for comparison and analysis.''')
        st.write('''3. **Benign Cases**: Least represented with 120 images, possibly because these conditions are less critical or variable than malignant cases.''')
        st.write('''The large number of malignant and normal images might improve diagnostics for these conditions while limiting understanding of benign ones.''')
    
    if 'Images' in visualization_type:
        
        # Add title
        st.markdown('''### **Image Visualization**''')
        
        # Define the directories for each class
        class_dirs = {'Benign': './samples/Benign',
                      'Malignant': './samples/Malignant',
                      'Normal': './samples/Normal'}

        # Display images and descriptions for each category in separate sections
        for class_name, folder in class_dirs.items():
            st.subheader(f'{class_name} Images')
            image_files = [f for f in os.listdir(folder) if f.endswith(('png', 'jpg', 'jpeg'))][:5]
            fig, axes = plt.subplots(1, len(image_files), figsize=(20, 4))  # Adjust subplot layout as needed

            for idx, image_file in enumerate(image_files):
                img_path = os.path.join(folder, image_file)
                img = Image.open(img_path)
                if len(image_files) > 1:
                    axes[idx].imshow(img)
                    axes[idx].axis('off')
                    axes[idx].set_title(image_file)
                else:
                    axes.imshow(img)
                    axes.axis('off')
                    axes.set_title(image_file)

            plt.tight_layout()
            st.pyplot(fig)

            # Add description for each class after displaying images
            if class_name == 'Benign':
                st.write('''The X-ray images reveal lungs with clear and evenly distributed small spots, devoid of any severe damage or irregular growth. These spots exhibit slow growth and have smooth edges, which sets them apart from harmful irregularities typically found in malignant cases.''')
            elif class_name == 'Malignant':
                st.write('''In contrast, the X-ray images of malignant cases show irregular, damaging spots with rough edges. These spots significantly affect lung structure and can spread rapidly into nearby areas due to their aggressive and irregular growth patterns.''')
            elif class_name == 'Normal':
                st.write('''The X-ray images of normal cases depict clear lungs without any unusual spots or blockages. They showcase healthy tissue and blood vessels, indicating a good air-tissue mix and normal blood flow, and are free from infections or obstructions commonly seen in abnormal lung conditions.''')

# Run the app
if __name__ == '__main__':
    run()
