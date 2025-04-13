# plots.py

import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.metrics import mean_squared_error, r2_score


def generate_plots() -> None:
    df = pd.read_csv('data/data.csv')
    y_true = df['hypotenuse']
    y_pred = df['predicted_hypotenuse']
    residuals = y_true - y_pred

    os.makedirs('data', exist_ok=True)

    # Calculate Mean Squared Error and R² Score
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    os.makedirs('results', exist_ok=True)
  
    # Scatterplot: True vs Predicted
    plt.figure(figsize=(8, 6))
    plt.scatter(y_true, y_pred, alpha=0.7, color='blue', label='Predictions')
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', label='Ideal (y = x)')
    plt.xlabel('True Hypotenuse')
    plt.ylabel('Predicted Hypotenuse')
    plt.title('Prediction vs. True Hypotenuse')
    plt.text(0.05, 0.95, f'MSE: {mse:.2f}\nR²: {r2:.2f}',
             transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('results/scatterplot.jpg')
    plt.close()

    # Histogram: Residuals
    plt.figure(figsize=(8, 6))
    plt.hist(residuals, bins=20, color='purple', edgecolor='black')
    plt.xlabel('Residual (True - Predicted)')
    plt.ylabel('Frequency')
    plt.title('Residuals Histogram')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('results/residuals_histogram.jpg')
    plt.close()


    df = pd.read_csv('data/data.csv')
    y_true = df['hypotenuse']
    y_pred = df['predicted_hypotenuse']
    residuals = y_true - y_pred


   
print("Plots and metrics saved in results")

if __name__ == "__main__":
    generate_plots()