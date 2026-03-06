🎬 TMDB Movie Performance Predictor

A machine learning web application that predicts movie revenue and popularity using key features from the TMDB dataset. The model is trained using Linear Regression and deployed through a Flask-based interface for real-time predictions.

🚀 Features

-Predicts movie revenue and popularity score

-Uses important features such as:

-Runtime

-Budget

-Vote Count

-Interactive Flask web interface

-Trained using scikit-learn Linear Regression

-Model saved using Pickle for deployment

🧠 Machine Learning Workflow

-Data preprocessing and feature selection

-Training a Linear Regression model

-Model evaluation using R² score

-Saving the trained model with Pickle

-Deploying predictions via Flask web app

🛠️ Tech Stack

-Python

-Pandas

-Scikit-learn

-Flask

-NumPy

-HTML / CSS

📊 Dataset

The project uses a processed version of the TMDB movie dataset, containing information such as:

Runtime

Budget

Vote Count

Revenue

Popularity

These features are used to train the regression model.

▶️ Running the Project

1️⃣ Clone the repository

git clone https://github.com/Anushka-learns/TMDB-popularity-predictor.git

cd TMDB-popularity-predictor

2️⃣ Install dependencies

pip install pandas scikit-learn flask numpy

3️⃣ Train the model

python training.py

4️⃣ Run the web app

python app.py

Then open:

http://127.0.0.1:5000/

📌 Example Prediction Inputs

Feature	Example

Runtime	120

Budget	50000000

Vote Count	1500

Output:

Predicted Revenue

Predicted Popularity Score

📈 Future Improvements

Add more predictive features

Try advanced models like Random Forest or XGBoost

Improve UI/UX for the web application

Deploy the project on Railway / Render

👩‍💻 Author

Anushka
B.Tech CSE (AI/ML) Student
Passionate about AI, Data Science, and ML-powered applications


If you want, I can also show you 3 small GitHub improvements that will make your profile look MUCH stronger to internship recruiters (based on the repos you showed).
  "predicted_revenue":504847445.6513789
}
