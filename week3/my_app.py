import streamlit as st 

st.title("Hello, streamlit!") 
st.write("this is my first Streamlit app.") 

if st.button("Click me!"): 
    st.write("You clicked the button! Nice Work!")

else: 
    st.write("Click the button to see what happens....")


import pandas as pd 

st.subheader("Exploring Our Dataset")

df = pd.read_csv("data/sample_data.csv")

# if in Week_2

pd.read_csv("data/sample_data.csv")

st.write("Here's our Data")
st.dataframe(df)


city = st. selectbox("Select a city" , df["City"].unique())
st.write(f"People in {city}")
st.dataframe(df[df["City"] == city])

st.bar_chart(df["Salary"])

