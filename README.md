# 🎬 TMDB Movie Revenue Predictor API

A Flask-based Machine Learning API that predicts movie popularity using budget, runtime, and vote count.

## 🚀 Tech Stack
- Python
- Flask
- Pandas
- Scikit-learn

## 📊 Model
Linear Regression trained on TMDB 5000 Movies dataset.

Features used:
- Runtime
- Budget
- Vote Count

Target:
- Popularity

## 🛠 How to Run

1. Clone repo
2. Create virtual environment
3. Install dependencies

pip install -r requirements.txt

4. Run training (if needed)

python training.py

5. Start server

python app.py

## 📌 API Endpoint

POST /predict

Example JSON:

{
  "runtime": 120,
  "budget": 100000000,
  "vote_count": 5000
}

Response:

{
  "predicted_revenue":504847445.6513789
}
