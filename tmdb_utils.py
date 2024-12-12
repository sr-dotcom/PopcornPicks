import requests
import streamlit as st

# Securely access the TMDB API key
API_KEY = st.secrets("TMDB_API_KEY")

if not API_KEY:
    raise ValueError("API Key not found. Please set TMDB_API_KEY in your .env file.")

@st.cache_data
def fetch_movie_data(movie_name):
    """Fetch movie details from TMDB."""
    try:
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
        response = requests.get(search_url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        if data.get('results'):
            return data['results'][0]  # Return the first result
        else:
            return None  # No movies found
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching movie data: {e}")
        return None

@st.cache_data
def fetch_recommendations(movie_id):
    """Fetch recommendations for a movie."""
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for movie in data.get("results", []):
            movie["poster_url"] = f"https://image.tmdb.org/t/p/w200{movie['poster_path']}" if movie.get("poster_path") else None
        return data.get("results", [])
    except requests.exceptions.RequestException as e:
        return []

@st.cache_data
def fetch_movie_suggestions(query):
    """Fetch movie suggestions dynamically based on user input."""
    try:
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}"
        response = requests.get(search_url)
        response.raise_for_status()
        data = response.json()
        # Extract movie titles and IDs
        suggestions = [{"title": movie["title"], "id": movie["id"]} for movie in data.get("results", [])]
        return suggestions
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching suggestions: {e}")
        return []

@st.cache_data
def fetch_trending_movies():
    """Fetch trending movies from TMDB."""
    try:
        trending_url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={API_KEY}"
        response = requests.get(trending_url)
        response.raise_for_status()
        data = response.json()
        # Add poster URL for each movie
        for movie in data.get("results", []):
            movie["poster_url"] = f"https://image.tmdb.org/t/p/w200{movie['poster_path']}" if movie.get("poster_path") else None
        return data.get("results", [])
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching trending movies: {e}")
        return []