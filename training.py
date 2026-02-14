import pandas as pd
df = pd.read_csv('tbdb2.csv')
df=df[[ 'runtime','budget','revenue','vote_average','vote_count','popularity']]
df= df.dropna()
print(df.columns)
from sklearn.linear_model import LinearRegression
import pickle
X=df[['runtime','budget','vote_count']]
Y=df[['revenue','popularity']]
model =LinearRegression()
model.fit(X,Y)
pickle.dump(model,open('model.pkl','wb'))
print("model trained and saved")