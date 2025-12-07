# Air-Quality-Project
.

🌫️ Air Quality Prediction Web App
🚀 Machine Learning | Streamlit Deployment | End-to-End Project

This project is an end-to-end Air Quality Prediction System built using Machine Learning models and deployed through Streamlit Cloud.
It predicts pollution levels based on pollutant values and provides an interactive UI with visual feedback.

🔗 Live Demo

Streamlit App:
👉 https://air-quality-project-nqfq3yqv7h93tgerd9kezy.streamlit.app/

📁 GitHub Repository

👉 https://github.com/rohitkumar142004/Air-Quality-Project

📌 Project Overview

This project predicts air quality using pollutant values such as:

Pollutant Min

Pollutant Max

Pollutant Average

Multiple machine learning models were trained and evaluated:

Linear Regression

Random Forest Regressor

K-Nearest Neighbors (KNN)

The best-performing model was saved using joblib and deployed inside a Streamlit dashboard with animations (balloons on prediction 🎈).

🧠 Features

✔ ML Model Training & Evaluation
✔ Prediction of Air Quality Level
✔ Interactive Streamlit UI
✔ Balloons animation after prediction
✔ Exported model (model.pkl)
✔ Clean visualizations & UX

📊 Tech Stack
Languages & Libraries

Python

NumPy, Pandas

Matplotlib, Seaborn

scikit-learn

joblib

Deployment

Streamlit

Streamlit Cloud

🏗️ Project Architecture
📦 Air-Quality-Project/
├── app.py               # Streamlit web app
├── model.pkl            # Trained ML model
├── air_quality.csv      # Dataset
├── notebook.ipynb       # Training & evaluation notebook
├── requirements.txt     # Project dependencies
└── README.md            # Documentation

⚙️ How to Run the Project Locally
1️⃣ Clone the repository
git clone https://github.com/rohitkumar142004/Air-Quality-Project.git
cd Air-Quality-Project

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run Streamlit app
streamlit run app.py

📐 Model Evaluation Metrics Used

MAE (Mean Absolute Error)

MSE (Mean Squared Error)

RMSE (Root Mean Squared Error)

R² Score

Each model was compared, and the best-performing model was deployed using joblib:

joblib.dump(rf, "model.pkl")

🖼️ Screenshots

(Add your app screenshots here)

Example:

🖥️ Dashboard View  
📌 Prediction Output  
📈 Model Performance Graphs

👨‍💻 Author

Rohit Kumar
Data Science | Machine Learning | Python
🔗 LinkedIn: https://www.linkedin.com/in/rohitkumar142004/

⭐ Support

If you find this project helpful, please ⭐ star the repository and share it!
Your support motivates me to build more real-world ML projects 🚀
