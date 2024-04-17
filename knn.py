import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix

# Load the dataset
df_books = pd.read_csv('updated_dataset.csv')

# 'title' is the column containing book titles
book_pivot = df_books.pivot_table(index='title', columns='authors', values='average_rating').fillna(0)

# Convert to sparse matrix
book_sparse = csr_matrix(book_pivot.values)

# Initialize Nearest Neighbors model
model = NearestNeighbors(algorithm='brute')
model.fit(book_sparse)

def recommend_book(title, author, genre):
    # Combine inputs to search for the book
    book_query = df_books[(df_books['title'].str.lower() == title.lower()) & 
                          (df_books['authors'].str.lower() == author.lower()) & 
                          (df_books['genre'].str.lower() == genre.lower())]

    if not book_query.empty:
        book_name = book_query.iloc[0]['title']
        book_id = np.where(book_pivot.index == book_name)[0][0]
        distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=10)

        suggested_books = []
        for i in range(len(suggestion)):
            books = book_pivot.index[suggestion[i]]
            for book in books:
                if book != book_name:
                    author_genre = df_books.loc[df_books['title'] == book, ['authors', 'genre']].values[0]
                    suggested_books.append({'title': book, 'author': author_genre[0], 'genre': author_genre[1]})

        return suggested_books
    else:
        return []

# Example usage:
# recommendations = recommend_book("Endless Night", "Agatha Christie", "Fiction")
# for book in recommendations:
#     print(book)
