import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("tbdb2.csv")

# Select relevant columns
df = df[['runtime','budget','vote_count','revenue','popularity']]
df = df.dropna()

# Features and targets
X = df[['runtime','budget','vote_count']]
y = df[['revenue','popularity']]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl","wb"))

print("Model trained and saved successfully")