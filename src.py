# src.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def train_and_predict(degree: int = 2) -> None:
    df = pd.read_csv('data/data.csv')
    X = df[['base', 'height']]
    y = df['hypotenuse']

    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X, y)

    df['predicted_hypotenuse'] = model.predict(X)
    df.to_csv('data/data.csv', index=False)
    print("Model trained and predictions saved to data/data.csv")

if __name__ == "__main__":
    train_and_predict()
