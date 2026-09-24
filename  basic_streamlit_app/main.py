import streamlit as st 
import pandas as pd 

st.title ("Palmer's Penguins Explorer")

st.write("This app allows users to explore the Palmer's Penguins dataset by filtering penguin species, island,and body mass")

df = pd.read_csv("/Users/suzymalshyti/Desktop/MALSHYTI-Data-Science-Portfolio-Fall2026/ basic_streamlit_app/penguins.csv")

species = st.selectbox(
    "Select species",
    df["species"].unique()
)

results = df[df["species"] == species]


island = st.selectbox(
    "Select island",
    df["island"].unique()
)

results = results[results["island"] == island]


body_mass = st.slider(
    " Slide Me! Select maximum body mass (grams)",
    min_value=2000,
    max_value=7000
)

results = results[results["body_mass_g"] <= body_mass]

st.dataframe(results) 

