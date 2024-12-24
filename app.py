import pickle
import streamlit as st

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    for i in distances[1:6]:  # Top 5 recommendations (excluding the selected movie)
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

# Custom CSS styling to improve UI with modern AI-inspired colors
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #4b6cb7, #182848); /* AI-inspired gradient */
            font-family: 'Arial', sans-serif;
            color: #ffffff;
        }
        .stButton>button {
            background-color: #8e44ad;  /* Neon Purple */
            color: white;
            font-weight: bold;
            border-radius: 12px;
            padding: 12px 24px;
            border: none;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #9b59b6; /* Lighter Purple */
        }
        .stSelectbox>div>div>div>input {
            background-color: rgba(0, 0, 0, 0.6);
            color: white;
            border: 1px solid #8e44ad; /* Neon Purple border */
            border-radius: 8px;
            padding: 8px;
            transition: background-color 0.3s ease;
        }
        .stSelectbox>div>div>div>input:focus {
            background-color: rgba(0, 0, 0, 0.8);
        }
        .stText {
            font-size: 18px;
            margin-top: 5px;
        }
        .recommendation {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 12px;
            margin-top: 12px;
            text-align: center;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }
        .recommendation:hover {
            background-color: rgba(255, 255, 255, 0.2);
            transform: scale(1.05); /* Slight scaling effect on hover */
        }
        .recommendation:active {
            background-color: rgba(255, 255, 255, 0.3);
        }
    </style>
    """, unsafe_allow_html=True
)

# Streamlit app header
st.header('Movie Recommender System')
st.markdown("### Discover Movies You Might Love!")

# Load movie data and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown for selecting a movie
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Search or Select a Movie",
    movie_list
)

# Display recommendations when button is clicked
if st.button('Show Recommendations'):
    recommended_movie_names = recommend(selected_movie)

    # Display recommendations with custom styling
    st.subheader("Recommended Movies:")
    for name in recommended_movie_names:
        st.markdown(f'<div class="recommendation">{name}</div>', unsafe_allow_html=True)
