# data.py

import numpy as np
import pandas as pd
import os

def generate_triangle_data(samples: int = 100, seed: int = 42) -> None:
    np.random.seed(seed)
    base = np.random.uniform(1, 30, samples)
    height = np.random.uniform(1, 30, samples)
    hypotenuse = np.sqrt(base**2 + height**2)

    df = pd.DataFrame({
        'base': base,
        'height': height,
        'hypotenuse': hypotenuse
    })

    os.makedirs('data', exist_ok=True)
    df.to_csv('data/data.csv', index=False)
    print("Synthetic triangle data saved to data/data.csv")

if __name__ == "__main__":
    generate_triangle_data()
