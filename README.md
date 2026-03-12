🚗 Car Price Prediction using Machine Learning
📌 Project Overview

This project focuses on predicting the price of cars based on their features using Machine Learning algorithms. The model analyzes various attributes such as engine volume, mileage, fuel type, car age, and other specifications to estimate the car price.

Car price prediction is a common regression problem in machine learning and helps buyers and sellers determine a fair market value for vehicles. Machine learning models can analyze historical data and identify patterns that influence pricing.

🎯 Problem Statement

The price of a car depends on many factors such as:

Manufacturer

Model

Engine volume

Mileage

Fuel type

Gearbox type

Car age

Safety features

Manually estimating a car's price can be difficult.
The objective of this project is to build machine learning models that accurately predict car prices based on these features.

📊 Dataset

The dataset contains information about different cars and their attributes.

Important Features
Feature	Description
Manufacturer	Brand of the car
Category	Type of vehicle
Fuel type	Petrol, Diesel, Hybrid
Engine volume	Engine capacity
Mileage	Distance travelled
Cylinders	Number of cylinders
Gear box type	Transmission type
Drive wheels	FWD, RWD, AWD
Airbags	Safety feature
Car_Age	Age of the vehicle
Price	Target variable
⚙️ Project Workflow
1️⃣ Data Preprocessing

Handling missing values

Data type conversion

Outlier detection and capping

Feature engineering (Car Age, Turbo)

Encoding categorical variables

2️⃣ Feature Scaling

Continuous numerical features were scaled using RobustScaler to handle outliers.

3️⃣ Model Training

Several machine learning regression models were trained and evaluated.

4️⃣ Model Evaluation

Models were evaluated using the following metrics:

R² Score

MAE (Mean Absolute Error)

MSE (Mean Squared Error)

RMSE (Root Mean Squared Error)

🤖 Machine Learning Models Used

The following algorithms were implemented:

Model	Purpose
Linear Regression	Baseline model
Lasso Regression	Regularization
Ridge Regression	Regularization
Elastic Net	Combined regularization
Decision Tree	Tree-based model
KNN Regressor	Distance-based model
Random Forest	Ensemble tree model
AdaBoost	Boosting ensemble
Gradient Boosting	Boosting algorithm
XGBoost	Advanced gradient boosting
Voting Ensemble	Combination of multiple models
Stacking Ensemble	Meta-model learning
📈 Model Performance
Algorithm	Test R² Score
Gradient Boosting	0.79 (Best)
XGBoost	0.78
AdaBoost	0.77
Voting Ensemble	0.75
Random Forest	0.74
Stacking Ensemble	0.73
KNN	0.72
Decision Tree	0.65
Linear / Ridge / Lasso	~0.30
Elastic Net	~0.23
🏆 Best Model

The Gradient Boosting model achieved the highest accuracy with:

R² Score ≈ 0.79

Lowest RMSE

🧰 Technologies Used

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn

XGBoost

Google Colab / Jupyter Notebook

📂 Project Structure
Car_Price_Prediction/
│
├── Car_Price_Prediction.ipynb
├── dataset/
│   └── car_data.csv
├── README.md
└── requirements.txt
🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/Venky-eelaprolu/Car_Price_Prediction.git
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Notebook

Open the notebook using:

Jupyter Notebook

Google Colab

Run all cells sequentially.

📌 Key Insights

Ensemble models performed better than linear models.

Boosting algorithms gave the highest accuracy.

Gradient Boosting achieved the best performance for this dataset.

🔮 Future Improvements

Hyperparameter tuning for better accuracy

Feature selection optimization

Deploy model using Flask / Streamlit

Build a web application for price prediction

👨‍💻 Author

Venky Eelaprolu

GitHub:
https://github.com/Venky-eelaprolu
