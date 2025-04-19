import streamlit as st
import pickle
import pandas as pd

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Custom CSS for background and styling
page_bg_img = '''
<style>
body {
background-size: cover;
}
.stApp {
background-color: rgba(0, 0, 0, 0);
padding: 2rem;
border-radius: 10px;
}
h1 {
color: #FFD700;
text-align: center;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# App title with emoji
st.markdown("## 🍿 **Movie Recommender System**")

# Movie selection dropdown
selected_movie_name = st.selectbox('🎬 Choose a movie you like:', movies['title'].values)

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in movie_list[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

# Recommend button
if st.button('🔍 Recommend'):
    st.markdown("### 🎯 Recommended Movies:")
    recommended_movie_names = recommend(selected_movie_name)
    for name in recommended_movie_names:
        st.write(f"👉 {name}")
