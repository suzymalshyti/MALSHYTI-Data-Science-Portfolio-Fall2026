import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error



# App title
st.title("Starbucks Nutrition Machine Learning App")

st.write(
    "Explore Starbucks nutritional information and use machine learning to make predictions."
)

st.write(
    "This app uses Starbucks drink nutrition data to explore relationships, between calories, sugar, fat, and other nutritional values.You can select a variable to predict, train a machine learning model,and evaluate how accurately it predicts the nutritional content of drinks."
)

# 1. Choose your data 
st.header("1. Choose your data")

data_option = st.selectbox(
    "How would you like to provide your data?",
    ["Use Starbucks sample dataset", "Upload my own CSV file"]

)
if data_option == "Use Starbucks sample dataset":
    sample_data = pd.read_csv("MLStreamltApp/starbucks.csv")
    st.write("Starbucks sample dataset selected")

else:
    uploaded_file = st.file_uploader("Upload your CSV file", type = "csv")

    if uploaded_file:
        sample_data = pd.read_csv(uploaded_file)
    else:
        st.write("Please upload a CSV file.")
        st.stop()

# Remove unnamed columns
for column in sample_data.columns:
    if "Unnamed" in column:
        sample_data = sample_data.drop(columns=column)


# 2. Explore your Data 
st.header("2. Explore Your Data")

st.write("Here is your dataset:")
st.dataframe(sample_data)

st.write("Number of rows and columns:", sample_data.shape)


# 3. Choose what to predict

st.header("3. Choose your target variable")

target_column = st.selectbox(
    "What would you like to predict?",
    sample_data.columns
)

st.write("Your selected target:", target_column)

# 4. Preparing Data

st.header("4. Prepare your data")

data = sample_data.dropna()

X = data.drop(columns=[target_column])
y = data[target_column]

#Check target variable

if y.dtype == "int64" or y.dtype == "float64":
    st.write("Your target is numerical.")

else:
    st.error("Please choose a numerical target variable.")
    st.stop()

X = pd.get_dummies(X, drop_first=True) 

#5 Machine Learning Model 

st.header("5. Machine Learning Model")

model_option = st.selectbox(
    "Choose your model:",
    ["Linear Regression", "K-Nearest Neighbors Regression"]
)

# 6. Adjust Hyperparameters

st.header("6. Adjust Hyperparameters")

if model_option == "Linear Regression":
    st.write("Linear Regression predicts numerical values using relationships between variables.")

    fit_intercept = st.selectbox(
        "Include an intercept?",
        [True, False]
    )

    model = LinearRegression(fit_intercept=fit_intercept)

elif model_option == "K-Nearest Neighbors Regression":

    st.write(
        "K-Nearest Neighbors Regression predicts numerical values based on similar observations."
    )

    neighbors = st.selectbox(
    "Choose the number of neighbors:",
    [3, 5, 7]
)

    model = KNeighborsRegressor(n_neighbors=neighbors)

   


# 7. Train your machine learning model
st.header("7. Train Your Model")

if st.button("Train Model"):

    if len(data) < 10:
        st.error("Please use a dataset with more rows.")
        st.stop()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    if model_option == "K-Nearest Neighbors Regression":

        if neighbors > len(X_train):
            st.error("Choose a smaller number of neighbors.")
            st.stop()

    model.fit(X_train, y_train)

    st.success("Your model has been trained!")

    predictions = model.predict(X_test)


        # 8. Evaluate your model
    st.header("8. Evaluate Your Model")

    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)

    st.metric("R² Score", r2)

    st.write(
        "R² measures how well the model explains differences in the target variable. "
        "A score closer to 1 is generally better."
    )

    st.metric("Mean Absolute Error", mae)

    st.write(
       "Mean Absolute Error measures how far the predictions are from the actual target values on average. Lower values are better."
    )

    # 9. Display your graph
    plt.title("Actual vs. Predicted " + target_column)

    plt.scatter(y_test, predictions)

    plt.xlabel("Actual " + target_column)
    plt.ylabel("Predicted " + target_column)
    plt.title("Actual vs. Predicted " + target_column)

    plt.show()
    st.pyplot(plt)

