from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    runtime = float(request.form["runtime"])
    budget = float(request.form["budget"])
    vote_count = float(request.form["vote_count"])

    features = np.array([[runtime, budget, vote_count]])

    prediction = model.predict(features)

    revenue = round(prediction[0][0],2)
    popularity = round(prediction[0][1],2)

    return render_template(
        "index.html",
        revenue=revenue,
        popularity=popularity
    )

if __name__ == "__main__":
    app.run(debug=True)