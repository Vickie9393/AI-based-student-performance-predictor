# 🎓 AI-Powered Student Performance Predictor

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

An interactive, machine-learning-driven web application designed to predict and analyze student academic performance.

---

## 📖 Project Synopsis

### Problem Statement

Educators and institutions often struggle to identify students at risk of underperforming early enough to intervene effectively. Traditional methods of evaluation are reactive, relying on final grades rather than proactive behavioral and academic indicators.

### Proposed Solution

This project introduces an AI-powered Student Performance Predictor. By analyzing 19 key features—ranging from academic scores (midterms, assignments, quizzes) to behavioral patterns (attendance, study hours, sleep, screen time)—the application uses a **Random Forest Classifier** to predict the final performance category of a student. This enables educators to provide timely interventions, ultimately fostering a better learning environment.

---

## 🌟 Key Features

1. **📊 Interactive Dashboard**: High-level overview of student metrics, attendance, and study hours with dynamic filtering.
2. **🤖 Real-time Prediction**: Input custom student parameters to instantly predict their performance category (Excellent, Good, Average, Poor) with confidence percentages.
3. **📈 Data Analytics**: Deep dive into the data using interactive Plotly charts, correlation heatmaps, and distribution plots.
4. **📂 Dataset Explorer**: Search, filter, and download the underlying dataset for independent research.
5. **ℹ️ About Page**: Project details, tech stack, and model accuracy information.
6. **✨ Unique UI**: A premium, glassmorphism-inspired, custom-styled interface for an exceptional user experience.

---

## 🧠 Model Report Card

| Metric | Details |
| :--- | :--- |
| **Model Architecture** | Random Forest Classifier |
| **Accuracy** | 85.7% |
| **Total Features** | 19 Input Variables |
| **Dataset Size** | 5,000 Student Records |
| **Target Classes** | Excellent, Good, Average, Poor |
| **Encoding Methods** | Label Encoding (Categorical), Target Encoding |

**Feature Importance Highlights:**

- *High Impact*: Attendance, Study Hours per Day, Previous GPA, Midterm Score
- *Medium Impact*: Sleep Hours, Assignment Scores, Quiz Scores
- *Low Impact*: Screen Time, Internet Access, Extracurriculars

---

## 🛠️ Technology Stack

- **Frontend/UI**: Streamlit, Custom CSS (Glassmorphism & Gradients)
- **Data Manipulation**: Pandas, NumPy
- **Machine Learning**: Scikit-Learn
- **Data Visualization**: Plotly Express
- **Model Serialization**: Joblib

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-score-prediction.git
cd student-score-prediction
```

### 2. Install Dependencies

Make sure you have Python 3.8+ installed.

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
python -m streamlit run app.py
```

### 4. Open in Browser

Navigate to `http://localhost:8501` to view the application.

---

## 📂 Project Structure

```text
📦 student-score-prediction-2-main
 ┣ 📂 data
 ┃ ┗ 📜 student_performance_realistic_5000.csv
 ┣ 📂 models
 ┃ ┣ 📜 label_encoders.pkl
 ┃ ┣ 📜 model.pkl
 ┃ ┗ 📜 target_encoder.pkl
 ┣ 📂 pages
 ┃ ┣ 📜 1_📊_Dashboard.py
 ┃ ┣ 📜 2_🤖_Prediction.py
 ┃ ┣ 📜 3_📈_Analytics.py
 ┃ ┣ 📜 4_📂_Dataset.py
 ┃ ┗ 📜 5_ℹ️_About.py
 ┣ 📜 app.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

---

## 📌 Conclusion

This AI-Powered Student Performance Predictor serves as a comprehensive tool for educational data mining. By bridging the gap between raw data and actionable insights, it empowers educators to make informed, data-driven decisions to support student success.
