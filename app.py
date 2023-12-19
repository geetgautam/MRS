import pickle
import streamlit as st
import requests
import pandas as pd
import time

#def fetch_poster(movie_id):
#   url = "https://api.themoviedb.org/3/movie/{}?api_key=3695ead202b2e3fc24f2dedada30979a&language=en-US".format(movie_id)
#    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3695ead202b2e3fc24f2dedada30979a&language=en-US'.format(movie_id), verify = False)
#    data = response.json()
    #st.text('https://api.themoviedb.org/3/movie/{}?api_key=3695ead202b2e3fc24f2dedada30979a&language=en-US".format(movie_id)')
#    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    recommended_movies = []
#    recommended_movie_posters = []
    for i in movie_list:
#        movie_id = movies.iloc[i[0]].movie_id

        # fetch the movie poster
#        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies #,recommended_movie_posters


st.title('Movie Recommender System')
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values

selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',
    movies['title'].values
)

if st.button('Show Recommendation'):
    names = recommend(selected_movie_name)

#    col1,col2,col3,col4,col5 = st.beta_coulmn(5)
#    with col1:
    st.text(names[0])
#        st.image(posters[0])
#    with col2:
    st.text(names[1])
#        st.image(posters[1])
#     with col3:
    st.text(names[2])
#        st.image(posters[2])
#    with col4:
    st.text(names[3])
#        st.image(posters[3])
#    with col5:
    st.text(names[4])
#        st.image(posters[4])
