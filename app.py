from flask import Flask,request,jsonify
import pickle
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return "Welcome to the movie revenue and popularity predictor API"
@app.route('/predict',methods=['POST'])
def predict():
    data=request.get_json()
    runtime=data['runtime']
    budget=data['budget']
    vote_count=data['vote_count']
    prediction=model.predict([[runtime,budget,vote_count]])
    return jsonify({"predicted revenue ":float(prediction[0][0])})
if __name__=='__main__':
    app.run(debug=True)
