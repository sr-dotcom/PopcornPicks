import streamlit as st
from tmdb_utils import fetch_movie_data, fetch_recommendations, fetch_movie_suggestions, fetch_trending_movies
from recommendation_engine import get_recommendations
from tmdb_utils import fetch_movie_suggestions

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Project","Home","Trending Movies","Movie Recommendations","Source"])

# "About Project" Page
if page == "About Project":
    st.title("🎓 About Popcorn Picks")
    st.markdown("""
    ## **Popcorn Picks: Movie Recommendation System**
    Popcorn Picks is a movie recommendation system built as the final project for the course 
    **5122 Visual Analytics and Storytelling** at the **University of North Carolina at Charlotte**.

    ### Course Details
    - **Course Name**: 5122 Visual Analytics and Storytelling
    - **Professor**: Chase Romano
    - **Institution**: University of North Carolina at Charlotte
    - **Student**: Naga Sathwik Reddy Gona

    ### Project Objectives
    - **Educational Purpose**: This project demonstrates the use of content-based filtering to provide movie recommendations.
    - **Trending Movies**: Utilizes TMDB API to showcase currently trending movies.
    - **Visualization and Interaction**: Built with Streamlit to deliver an interactive, user-friendly interface.

    ### Acknowledgments
    - Special thanks to **Professor Chase Romano** for guidance and support during the course.
    - This project was made possible by the **TMDB API**.

    ---
    ### Contact
    For inquiries, you can reach me at:
    - **Email**: ngona@charlotte.edu
    - **GitHub Repository**: [Popcorn Picks](https://github.com/your-username/Popcorn_Picks)
    """)

# "Home" Page
elif page == "Home":
    st.title("🍿 Popcorn Picks")
    st.markdown("""
    ## Welcome to Popcorn Picks!
    Discover your next favorite movie with our personalized recommendation system. 
    Dive into trending movies or explore recommendations based on your favorites!
    
    ### Features:
    - **Search Movies**: Enter a movie name to get recommendations for similar movies.
    - **Trending Movies**: View a list of currently trending movies worldwide.
    - **Search History**: Quickly revisit previously searched movies.

    ### How It Works:
    - We use the [TMDB API](https://www.themoviedb.org/documentation/api) to fetch movie details, posters, and recommendations.
    - Recommendations are based on movie similarity (Heuristic-based Content-Based Filtering).
    
    ### Explore the Features:
    Use the sidebar to navigate between the Home, Trending Movies, Movie Recommendations, and Source pages.

    ---
    **Developer Notes**: 
    - This is a demo project showcasing the integration of TMDB API with a recommendation system.
    - Built with [Streamlit](https://streamlit.io/) for simplicity and interactivity.
    """)

# "Trending Movies" Page
elif page == "Trending Movies":
    st.title("🔥 Trending Movies")
    with st.spinner("Fetching trending movies..."):
        trending_movies = fetch_trending_movies()
        if trending_movies:
            num_columns = 4  # Fixed number of columns
            for row_start in range(0, len(trending_movies), num_columns):
                # Create a row with `num_columns` columns
                row = st.columns(num_columns)
                for col, movie in zip(row, trending_movies[row_start:row_start + num_columns]):
                    with col:
                        # Display the movie poster
                        if movie['poster_url']:
                            st.image(movie['poster_url'], use_container_width=True)
                        else:
                            st.text("No Image")

                        # Display the movie title
                        st.write(f"**{movie['title']}**")

                        # Add "More Info" link
                        more_info_url = f"https://www.themoviedb.org/movie/{movie['id']}"
                        st.markdown(f"[More Info]({more_info_url})", unsafe_allow_html=True)
        else:
            st.warning("No trending movies found.")


# "Search Movies" Page
elif page == "Movie Recommendations":
    # Title
    st.title("🎥 Movie Recommendation System")

    # Initialize search history in session state
    if "search_history" not in st.session_state:
        st.session_state.search_history = []

    # Sidebar: Limit history size and add a clear button
    st.sidebar.header("Search History")
    max_history = 10  # Maximum number of searches to keep

    # Display search history in the sidebar
    if st.session_state.search_history:
        for idx, movie in enumerate(st.session_state.search_history):
            if st.sidebar.button(f"{movie}", key=f"history_{idx}"):
                st.session_state.query = movie  # Populate the input box when clicked

        # Add a button to clear search history
        if st.sidebar.button("Clear Search History"):
            st.session_state.search_history = []  # Clear the history
            st.session_state.query = ""  # Reset the search box value
            st.sidebar.info("Search history cleared.")
    else:
        st.sidebar.info("No search history yet.")

    # Input box for movie name
    query = st.text_input("Search for a movie:", value=st.session_state.get("query", ""))


    if query:
        # Store the query in search history if it's not already there
        if query not in st.session_state.search_history:
            st.session_state.search_history.append(query)
            # Limit the history size
            if len(st.session_state.search_history) > max_history:
                st.session_state.search_history = st.session_state.search_history[-max_history:]

        # Fetch movie suggestions based on the input query
        suggestions = fetch_movie_suggestions(query)

        if suggestions:
            # Display suggestions in a dropdown
            selected_movie = st.selectbox(
                "Select a movie from the suggestions:",
                suggestions,
                format_func=lambda movie: movie["title"],  # Display only the title
            )

            if selected_movie:
                with st.spinner('Fetching recommendations...'):
                    recommendations = fetch_recommendations(selected_movie["id"])
                    if recommendations:
                        # Display recommendations in a grid layout
                        st.subheader(f"Top recommendations for '{selected_movie['title']}'")

                        num_columns = 4  # Fixed number of columns
                        for row_start in range(0, len(recommendations), num_columns):
                            # Create a row with `num_columns` columns
                            row = st.columns(num_columns)
                            for col, rec in zip(row, recommendations[row_start:row_start + num_columns]):
                                with col:
                                    # Display the movie poster
                                    if rec['poster_url']:
                                        st.image(rec['poster_url'], use_container_width=True)
                                    else:
                                        st.text("No Image")

                                    # Display the movie title
                                    st.write(f"**{rec['title']}**")

                                    # Add "More Info" link
                                    more_info_url = f"https://www.themoviedb.org/movie/{rec['id']}"
                                    st.markdown(f"[More Info]({more_info_url})", unsafe_allow_html=True)
                            
                            # Add margin between rows
                            st.write("")  # Adds spacing between rows
                    else:
                        st.warning(f"No recommendations found for '{selected_movie['title']}'.")
        else:
            st.warning("No suggestions found. Try another search term.")
    else:
        st.info("Start typing a movie name to see suggestions.")

# "Source" Page
elif page == "Source":
    st.title("📚 Source")
    st.markdown("""
    ## Acknowledgment
    "This product uses the TMDB API but is not endorsed or certified by TMDB."
    
    ---
                
    ### About TMDB:
    TMDB (The Movie Database) is a popular, user-driven database for movies and TV shows. It provides an extensive API for fetching movie details, posters, recommendations, and more.

    ---

    ### Resources:
    - [TMDB Website](https://www.themoviedb.org)
    - [TMDB API Documentation](https://www.themoviedb.org/api-terms-of-use)
    
    ---

    ### Terms of Use:
    Please note that this application is for educational and non-commercial use. All movie data and images are sourced from TMDB.
    
    ---

    ### Disclaimer:
    - All data fetched from TMDB is presented "as-is" without modifications.  
    - This application does not store, alter, or redistribute TMDB's data in any form.  
    - The recommendations and functionality provided by this application are solely for educational purposes and are based on TMDB's publicly available metadata.
    ---
    **Credits**: The Movie Database (TMDB).
    """)