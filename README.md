# PopcornPicks
An educational movie recommendation system using the TMDB API, built with Streamlit.

# PopcornPicks 🍿

An educational movie recommendation system using the TMDB API, built with Streamlit.

## About the Project
PopcornPicks is an intuitive and fun movie recommendation engine that helps users discover new movies based on their interests. Powered by [The Movie Database (TMDB) API](https://www.themoviedb.org/documentation/api), it showcases a seamless integration of Streamlit for an interactive and responsive user experience.

### Features:
- **Search for Movies**: Instantly search for any movie in the TMDB database.
- **Trending Movies**: Discover the most popular movies trending globally.
- **Recommendations**: Get personalized movie recommendations based on selected titles.
- **Auto-suggestions**: Explore movies with dynamic suggestions as you type.

## Live Demo
Try the app here: **[PopcornPicks on Streamlit](https://popcornpicks-sr-dotcom.streamlit.app/)**

## Getting Started
Follow these instructions to set up and run the project locally.

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- [Streamlit](https://streamlit.io/)
- A TMDB API key (get yours from [TMDB](https://www.themoviedb.org/documentation/api))

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sr-dotcom/PopcornPicks.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PopcornPicks
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your `secrets.toml` file for sensitive information:
   - Create a `.streamlit/secrets.toml` file:
     ```bash
     mkdir .streamlit
     touch .streamlit/secrets.toml
     ```
   - Add the following to your `secrets.toml` file:
     ```toml
     [general]
     TMDB_API_KEY = "your_api_key_here"
     ```

### Running the Application
To start the app locally, use the following command:
```bash
streamlit run app.py
```

Access the app at `http://localhost:8501` in your browser.

## Folder Structure
```
PopcornPicks/
├── .devcontainer/         # Development container configuration (optional)
├── .streamlit/            # Configuration folder (for secrets.toml)
├── LICENSE                # Project license
├── README.md              # Project documentation
├── app.py                 # Main Streamlit app file
├── recommendation_engine.py # Recommendation engine logic
├── requirements.txt       # Python dependencies
├── tmdb_utils.py          # Utilities for TMDB API integration
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your commit message"
   ```
4. Push the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
