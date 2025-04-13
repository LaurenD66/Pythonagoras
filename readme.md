# Overview
## This project uses a shallow learning regression model and CSV data set to predict the hypotenuse of a right triangle.   

## MRAC01(24/25): Software III - Machine Learning for Robotic Fabrication
This project aims to demonstrate a shallow learning regression model using a CSV data set based on the Pythagorian Theorem to predict other hypotenuse outcomes given any combination of base and height dimensions.  This project is a part of the first year Masters in Robotics and Advanced Construction Software (level III) Coursework in Machine Learning for Robotic Fabrication.


## Prerequisites
Ensure that you fulfill the following criteria to replicate this project.
* Ubuntu LTS 20.04 
* Python 3.10 

## Libraries
### data:
* numpy as np
* pandas as pd
* os
### src:
* from sklearn.linear_model, LinearRegression
* from sklearn.preprocessing, PolynomialFeatures
* from sklearn.pipeline, make_pipeline
### plot:
* pandas
* matplotlib.pyplot
* os

## DATASET DESCRIPTION
The DATA code generates synthetic data representing right-angled triangles by randomly sampling base and height values, then computing the corresponding hypotenuse using the Pythagorean theorem. It organizes this data into a pandas DataFrame and exports it to a CSV file named data.csv in a data/ directory, creating the folder if it doesn't already exist. When executed, it saves 100 triangle samples by default and confirms the file's creation with a print message.

## MODEL DETAILS
The SRC code trains a polynomial regression model to predict the hypotenuse of right-angled triangles based on the base and height values from a CSV file. It fits the model using the provided data, then generates predictions for the hypotenuse and adds them to the same CSV file under the column predicted_hypotenuse. When run, it saves the updated dataset and prints a confirmation message.

## EVALUATION RESULTS
This PLOTS code reads a CSV file containing true and predicted hypotenuse values and calculates the differences between them. Because the variables were mathmatically correlated, there was no need for scaling. 

### Error Metrics
The mean squared error (MSE) indicates how far off the predictions are from the true value and the R² score indicates the correlation between the base and height inputs and the target.

### Graphs
It then generates two plots: a scatterplot comparing true vs. predicted hypotenuse values, and a histogram of the residuals, which help visualize the model's accuracy. Both plots are saved as .jpg files in the results/ directory, and a confirmation message is printed.

### Observations

That MSE means your predictions are very close (0.05) to the actual hypotenuse values. The R² score is 99.8% of the variance in the hypotenuse, whihc is very accurate.

## HOW TO RUN PROGRAM
01. Create virtual environment.
02. Ensure you have prerequisites and libraries (above).
03. In the terminal, run the python scripts sequnentially: (1) data.py to generate random data set of pythagorian variables; (2) src.py to create predictions using polynomial linear regression; (3) plots.py to plot and interpret predicted targets against true values.
04. Interpret results.


## Authors
  - [Lauren Deming](linkedin.com/in/laurendemingconstructs) 

## References
- [Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825–2830. Retrieved April 13, 2025, from ](https://scikit-learn.org/stable/auto_examples/index.html)

<!--  DO NOT REMOVE
-->
#### Acknowledgements

- Creation of GitHub template: [Marita Georganta](https://www.linkedin.com/in/marita-georganta/) - Robotic Sensing Expert
- Creation of MRAC-IAAC GitHub Structure: [Huanyu Li](https://www.linkedin.com/in/huanyu-li-457590268/) - Robotic Researcher