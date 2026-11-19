
# Starbucks Nutrition Machine Learning App

## 1. Project Overview

The Starbucks Nutrition Machine Learning App is an interactive application built using Python and Streamlit. It allows users to explore Starbucks drink nutritional information and use machine learning to predict nutritional values.

Users can:
- Explore the Starbucks nutrition dataset.
- Upload their own CSV file or use the Starbucks sample dataset.
- Choose which numerical variable they want to predict.
- Select between two machine learning models.
- Adjust model hyperparameters.
- Train and test their selected model.
- Evaluate model performance using R² Score and Mean Absolute Error.
- View a graph comparing actual and predicted values.

## 2. Dataset Source

The Starbucks nutrition dataset used in this project was obtained from Kaggle.

**Dataset:** [Starbucks Nutrition Dataset on Kaggle](PASTE YOUR KAGGLE DATASET LINK HERE)

## 3. Deployed Application

**Streamlit App:** Add your deployed Streamlit application link here.

## 4. Running the App Locally

Follow these steps to run the application on your computer.

### Step 1: Clone the GitHub repository

```
git clone YOUR-GITHUB-REPOSITORY-LINK
```

### Step 2: Navigate to the project folder

```
cd MALSHYTI-Data-Science-Portfolio-Fall2026/MLStreamlitApp
```

### Step 3: Install the required libraries

```
pip install -r requirements.txt
```

### Step 4: Run the Streamlit application

```
streamlit run app.py
```

The application will open in your web browser.

**Note:** Make sure the `starbucks.csv` sample dataset is saved in the MLStreamlitApp folder.

## 5. Required Libraries

| Library | Purpose |
|---|---|
| pandas | Loading and organizing datasets |
| streamlit | Creating the interactive application |
| matplotlib | Creating data visualizations |
| scikit-learn | Building and evaluating machine learning models |

The required library versions are listed in `requirements.txt`.

## 6. Machine Learning Models

The application uses two supervised machine learning regression models.

### Linear Regression

Linear Regression predicts numerical values by identifying relationships between input variables and the selected target variable.

**Adjustable hyperparameter:**
- `fit_intercept`: Allows users to choose whether the model includes an intercept.

### K-Nearest Neighbors Regression

K-Nearest Neighbors Regression predicts numerical values based on similar observations in the dataset.

**Adjustable hyperparameter:**
- `n_neighbors`: Allows users to select how many neighboring observations the model uses to make predictions.

Users can adjust these hyperparameters in the application before training their model.

## 7. Model Evaluation

The application evaluates model performance using two metrics.

### R² Score

Measures how well the model explains variation in the target variable. A score closer to 1 generally indicates a better fit.

### Mean Absolute Error (MAE)

Measures the average difference between predicted and actual values. Lower values indicate more accurate predictions.

### Actual vs. Predicted Values

The application also displays a scatterplot comparing actual values with predicted values to help users visualize model performance.

## 8. References

1. [Kaggle](https://www.kaggle.com/) – Source of the Starbucks nutrition dataset used in this project.
2. [Streamlit Documentation](https://docs.streamlit.io/) – Used as a reference for building the interactive application.
3. [Scikit-learn Documentation](https://scikit-learn.org/stable/) – Used as a reference for implementing machine learning models and evaluating model performance.
4. [Pandas Documentation](https://pandas.pydata.org/docs/) – Used as a reference for loading, cleaning, and organizing the dataset.



