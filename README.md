# 🎬 Movie Recommender System

This project is a **content-based movie recommender system** that suggests similar movies based on user input. It includes a **Streamlit web app** (`app.py`) and a **Jupyter Notebook** (`Movie_recommender_system.ipynb`) for training and exporting the recommendation logic.

## 🔧 Features

- Suggests 5 similar movies based on a selected title.
- User-friendly web interface built with **Streamlit**.
- Trained using a **cosine similarity** approach on movie metadata.
- Custom CSS for improved visual appearance.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install streamlit pandas scikit-learn
```

### 3. Prepare the Data

Ensure `movie_dict.pkl` and `similarity.pkl` are present in the root directory. You can generate these by running the notebook:

```bash
jupyter notebook Movie_recommender_system.ipynb
```

### 4. Run the App

```bash
streamlit run app.py
```

## 🧠 How It Works

- The movie data is vectorized using text features like genres, keywords, and cast.
- A **cosine similarity matrix** is computed between all movie vectors.
- Given a selected movie, the app retrieves the top 5 most similar movies using the similarity scores.

## 📦 Requirements

- Python 3.7+
- Streamlit
- Pandas
- Scikit-learn
- Jupyter (for training)

## 🙌 Acknowledgements

- Dataset used from [TMDB](https://www.themoviedb.org/)
- Inspired by multiple movie recommender tutorials
  
