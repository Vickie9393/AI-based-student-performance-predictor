import streamlit as st
import pandas as pd
import joblib
import numpy as np
import shap
import plotly.express as px
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import apply_custom_css

model = joblib.load("models/model.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")
target_encoder = joblib.load("models/target_encoder.pkl")

df = pd.read_csv("data/student_performance_realistic_5000.csv")

st.set_page_config(page_title="Prediction", layout="wide")
apply_custom_css()

st.title("🤖 Student Performance Prediction")

st.write("Enter the student details below.")

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox("Gender", df["Gender"].unique())

        age = st.number_input(
            "Age",
            min_value=10,
            max_value=25,
            value=18
        )

        grade = st.selectbox(
            "Grade Level",
            df["Grade_Level"].unique()
        )

        attendance = st.slider(
            "Attendance %",
            0,
            100,
            80
        )

        study_hours = st.slider(
            "Study Hours / Day",
            0.0,
            12.0,
            4.0
        )

        previous_gpa = st.slider(
            "Previous GPA",
            0.0,
            4.0,
            3.0
        )

        midterm = st.slider(
            "Midterm Score",
            0,
            100,
            70
        )

        assignment = st.slider(
            "Assignment Score",
            0,
            100,
            75
        )

    with col2:

        quiz = st.slider(
            "Quiz Score",
            0,
            100,
            70
        )

        participation = st.selectbox(
            "Class Participation",
            df["Class_Participation"].unique()
        )

        extracurricular = st.selectbox(
            "Extracurricular",
            df["Extracurricular"].unique()
        )

        internet = st.selectbox(
            "Internet Access",
            df["Internet_Access"].unique()
        )

        parent = st.selectbox(
            "Parent Education",
            df["Parent_Education"].unique()
        )

        income = st.selectbox(
            "Family Income",
            df["Family_Income"].unique()
        )

        sleep = st.slider(
            "Sleep Hours",
            0.0,
            12.0,
            7.0
        )

        screen = st.slider(
            "Screen Time",
            0.0,
            12.0,
            4.0
        )

        stress = st.selectbox(
            "Stress Level",
            df["Stress_Level"].unique()
        )

        feedback = st.selectbox(
            "Teacher Feedback",
            df["Teacher_Feedback"].unique()
        )

        absences = st.slider(
            "Absences",
            0,
            50,
            5
        )

    predict = st.form_submit_button("🚀 Predict")




if predict:

    input_data = pd.DataFrame({

        "Gender": [gender],
        "Age": [age],
        "Grade_Level": [grade],
        "Attendance": [attendance],
        "Study_Hours_Per_Day": [study_hours],
        "Previous_GPA": [previous_gpa],
        "Midterm_Score": [midterm],
        "Assignment_Score": [assignment],
        "Quiz_Score": [quiz],
        "Class_Participation": [participation],
        "Extracurricular": [extracurricular],
        "Internet_Access": [internet],
        "Parent_Education": [parent],
        "Family_Income": [income],
        "Sleep_Hours": [sleep],
        "Screen_Time": [screen],
        "Stress_Level": [stress],
        "Teacher_Feedback": [feedback],
        "Absences": [absences]

    })

    for col in label_encoders:
        input_data[col] = label_encoders[col].transform(input_data[col])

   

    prediction = model.predict(input_data)

    result = target_encoder.inverse_transform(prediction)

    st.success(f"🎯 Predicted Performance : {result[0]}")

    probability = model.predict_proba(input_data)

    confidence = np.max(probability) * 100

    st.info(f"Confidence : {confidence:.2f}%")

    if result[0] == "Excellent":
        st.success("🌟 Outstanding performance. Keep it up!")

    elif result[0] == "Good":
        st.info("📚 Good work. A little more effort can lead to excellent performance.")

    elif result[0] == "Average":
        st.warning("⚠ Improve attendance and study hours to boost performance.")

    else:
        st.error("❌ High risk detected. Focus on regular study, attendance, and seek academic support.")

    # ---- SHAP Explainability ----
    st.divider()
    st.subheader("🧠 Why this prediction?")
    st.write("The chart below shows how each factor influenced this specific prediction. Features in **green** pushed the prediction towards this outcome, while features in **red** pushed against it.")

    try:
        # Create Linear Explainer (Model is LogisticRegression, not Random Forest)
        explainer = shap.LinearExplainer(model, np.zeros((1, input_data.shape[1])))
        
        # Calculate SHAP values for the single instance
        shap_values = explainer.shap_values(input_data)
        
        # Get the predicted class index
        predicted_class_idx = int(prediction[0])
        
        # Extract SHAP values for the predicted class
        if isinstance(shap_values, list):
            sv = shap_values[predicted_class_idx][0]
        elif len(shap_values.shape) == 3:
            sv = shap_values[0, :, predicted_class_idx]
        else:
            sv = shap_values[0]
            
        # Create a DataFrame for Plotly
        shap_df = pd.DataFrame({
            "Feature": input_data.columns,
            "SHAP Value": sv
        })
        
        shap_df["Absolute Impact"] = shap_df["SHAP Value"].abs()
        shap_df = shap_df.sort_values(by="Absolute Impact", ascending=False).head(10) # Top 10 features
        
        shap_df["Impact"] = shap_df["SHAP Value"].apply(lambda x: "Positive" if x > 0 else "Negative")
        
        fig_shap = px.bar(
            shap_df, 
            x="SHAP Value", 
            y="Feature", 
            orientation='h',
            color="Impact",
            color_discrete_map={"Positive": "#2EA043", "Negative": "#F85149"},
            title=f"Top 10 Factors Impacting the '{result[0]}' Prediction"
        )
        
        # Improve layout
        fig_shap.update_layout(
            yaxis={'categoryorder':'total ascending'},
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#FAFAFA')
        )
        
        st.plotly_chart(fig_shap, use_container_width=True)
        
    except Exception as e:
        st.error(f"Could not generate SHAP explanation: {e}")
    