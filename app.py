import streamlit as st
import pickle
import pandas as pd
import requests

#Creating recommend Function for recommend button
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    for i in movie_list[1:6]:
        movie_id = movies.iloc[i[0]].id

        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl' ,'rb'))
movies = pd.DataFrame(movies_dict)

similarity =pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox (
'Select a Movie ',
movies['title'].values)

if st.button('Recommend'):
    recommendations =recommend(selected_movie_name)
    for i in recommendations :
        st.write(i)



