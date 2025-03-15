import streamlit as st
import pickle as pkl
import numpy as np
from streamlit_option_menu import option_menu
import time  # For animations

# Configure Streamlit Page
st.set_page_config(page_title="Diabetes Prediction App", layout="wide", page_icon="🩺")

# Load trained model
diabetes_model = pkl.load(open('diabetes_model.sav', 'rb'))

# Sidebar with Animation
with st.sidebar:
    #st.image("https://media.giphy.com/media/fhAwk4DnqNgw8/giphy.gif", use_container_width=True)
    selected = option_menu(
        "Disease Prediction System",
        ["Diabetes Prediction"],
        menu_icon="hospital-fill",
        icons=["activity"],
        default_index=0
    )

# Main Page
if selected == "Diabetes Prediction":
    st.markdown("<h1 style='text-align: center; color: #FF5733;'>🔬 Diabetes Prediction using ML</h1>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Getting User Input
    st.markdown("### **📥 Enter Patient Details**", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("🤰 Number of Pregnancies", min_value=0, step=1)
    with col2:
        Glucose = st.number_input("🩸 Glucose Level", min_value=0)
    with col3:
        BloodPressure = st.number_input("💗 Blood Pressure", min_value=0)
    with col1:
        SkinThickness = st.number_input("🩹 Skin Thickness", min_value=0)
    with col2:
        Insulin = st.number_input("💉 Insulin Level", min_value=0)
    with col3:
        BMI = st.number_input("⚖️ BMI", min_value=0.0)
    with col1:
        DiabetesPedigreeFunction = st.number_input("🧬 Diabetes Pedigree Function", min_value=0.0)
    with col2:
        Age = st.number_input("🎂 Age", min_value=0, step=1)

    # Prediction Button with Animation
    diab_diagnosis = ""

    if st.button("🚀 Get Diabetes Test Result"):
        with st.spinner("🔍 Analyzing... Please wait..."):
            time.sleep(2)  # Simulate processing time

        # Convert Input into a NumPy Array
        user_input = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                Insulin, BMI, DiabetesPedigreeFunction, Age]])

        # Prediction
        diab_prediction = diabetes_model.predict(user_input)

        # Progress Bar Animation
        progress_text = "🛠️ Running Machine Learning Model..."
        progress_bar = st.progress(0)
        for percent in range(100):
            time.sleep(0.02)
            progress_bar.progress(percent + 1)

        # Display Result
        if diab_prediction[0] == 1:
            diab_diagnosis = "⚠️ **The person is DIABETIC. Please consult a doctor.**"
            st.error(diab_diagnosis)
            #st.image("https://media.giphy.com/media/Z9fL3wRjUkkFu/giphy.gif", width=300)
        else:
            diab_diagnosis = "✅ **The person is NOT diabetic. Stay healthy!**"
            st.success(diab_diagnosis)
            #st.image("https://media.giphy.com/media/3ohs4pBpeA4uaIGvxW/giphy.gif", width=300)

    # Footer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; color: grey;'>Made by @Brijkishor Soni with ❤️ using Machine Learning & Streamlit</p>",
        unsafe_allow_html=True
    )

