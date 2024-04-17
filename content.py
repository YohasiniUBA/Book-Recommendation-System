# content.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the dataset
df_books = pd.read_csv('updated_dataset.csv')

# Combine relevant columns to create a textual representation for each book
df_books['combined_features'] = df_books['title'].fillna('') + ' ' + df_books['authors'].fillna('') + ' ' + df_books['genre'].fillna('')

# Initialize TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Drop rows with missing values in the combined_features column
df_books.dropna(subset=['combined_features'], inplace=True)

# Construct the TF-IDF matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(df_books['combined_features'])

# Function to recommend books based on input preferences
# Function to recommend books based on input preferences
def recommend_books(title, author, genre, top_n=10):
    # Create a feature vector for the input
    input_features = tfidf_vectorizer.transform([f'{title} {author} {genre}'])

    # Compute the cosine similarity between the input and all books
    cosine_similarities = linear_kernel(input_features, tfidf_matrix).flatten()

    # Get the indices of top similar books
    top_indices = cosine_similarities.argsort()[-top_n-1:-1][::-1]

    # Return the top recommended books
    recommended_books = df_books.iloc[top_indices][['title', 'authors', 'genre']]
    return recommended_books

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommendations():
    # Get input from the form
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    
    # Call the recommendation function
    recommended_books_df = recommend_books(title, author, genre)
    
    # Convert DataFrame to list of dictionaries
    recommended_books = recommended_books_df.to_dict(orient='records')
    
    # Render the template with the recommended books
    return render_template('recommendations.html', recommended_books=recommended_books)

if __name__ == '__main__':
    app.run(debug=True)
