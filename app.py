from flask import Flask, render_template, request
from content import recommend_books
from knn import recommend_book

app = Flask(__name__)

# Route for the main page with the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and display recommendations
@app.route('/recommend', methods=['POST'])
@app.route('/recommend', methods=['POST'])
def recommend():
    # Get input data from the form
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    
    # Call content-based filtering script
    content_based_results = recommend_books(title, author, genre)
    
    # Convert DataFrame to list of dictionaries
    recommended_books = content_based_results.to_dict(orient='records')

    # Call collaborative filtering script
    collaborative_results = recommend_book(title, author, genre)
    
    # Combine and format recommendations
    recommendations = {
        'content_based': recommended_books,  # Update variable name
        'collaborative': collaborative_results
    }

    # Render the template with the recommended books
    rendered_template = render_template('recommendations.html', recommendations=recommendations)

    return rendered_template

if __name__ == '__main__':
    app.run(debug=True)

