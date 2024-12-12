import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(movie_id):
    """Generate recommendations based on movie ID."""
    # Fetch recommendations using TMDB API
    from tmdb_utils import fetch_recommendations
    movies = fetch_recommendations(movie_id)
    if not movies:
        return []
    
    # Process data
    movies_df = pd.DataFrame(movies)
    movies_df['overview'] = movies_df['overview'].fillna('')
    
    # Vectorize using TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies_df['overview'])
    
    # Compute similarity
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix).flatten()
    movies_df['similarity_score'] = similarity_scores
    
    # Sort by similarity score
    movies_df = movies_df.sort_values(by='similarity_score', ascending=False)
    return movies_df[['title', 'overview', 'similarity_score']].to_dict(orient='records')
