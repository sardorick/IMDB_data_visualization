import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("IMDB best Crime movies")

st.write("Which Crime movie should I watch today?")
# data_select = st.sidebar.selectbox()
df = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Documents\Strive repos\IMDB_data_visualization\Finaldata.csv")
st.dataframe(df)

df_min_max_scaled = df.copy()

column = 'rating'
column1 = 'durations'


df_min_max_scaled[column, column1] = (df_min_max_scaled[column] - df_min_max_scaled[column].min()) / (df_min_max_scaled[column].max() - df_min_max_scaled[column].min()) / (df_min_max_scaled[column1] - df_min_max_scaled[column1].min()) / (df_min_max_scaled[column1].max() - df_min_max_scaled[column1].min())

# df[['Release', 'rating']].groupby('Release').mean().plot(kind='bar', title='Average rating of movies per year', figsize=(10,10))
# plt.xlabel('years')
# plt.ylabel('rating')
# plt.savefig('Average rating of movies per year.png')
st.header("Ratings of movies by year")
st.bar_chart(df[['Release', 'rating']].groupby('Release').mean()) 
 
st.header("Best directors in Crime movies")
st.bar_chart(df['directors'].value_counts().nlargest(10))


actors  = df.stars.str.split(',')

actors_name = []
for i in actors:
    for j in i:
        actors_name.append(j.replace("'"," ").strip("[ ]"))


df_stars = pd.DataFrame(actors_name)

st.header("Best actors in Crime movies")
st.bar_chart(df_stars[0].value_counts().nlargest(10))