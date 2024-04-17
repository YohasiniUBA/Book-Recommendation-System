# Book-Recommendation-System

This repository contains the code for a book recommendation system that combines content-based and collaborative filtering techniques to recommend books to users. The system utilizes k-nearest neighbors algorithm, TF-IDF vectorization, and cosine similarity to generate recommendations.

The datasets used in this project include:
1. Books
2. Ratings
3. Users
These datasets are uploaded in the repository.

Models Used:
1. K Nearest Neighbors (KNN): KNN algorithm is utilized for collaborative filtering to find similar users or items.
2. TF-IDF Vectorization: TF-IDF (Term Frequency-Inverse Document Frequency) vectorization is employed for content-based filtering. It converts textual data into numerical vectors based on the importance of terms in documents.
3. Cosine Similarity: Cosine similarity metric is used to measure the similarity between TF-IDF vectors of items.


Tools:

Flask is used to seamlessly bridge the recommendation system's frontend and backend, allowing smooth communication between the user interface and the underlying functionality. By defining routes and handling requests with Flask, we ensure efficient data exchange and presentation of recommendations to the user. This integration streamlines the user experience, making it intuitive and responsive.


Demo Video:

A demo video demonstrating the front end of the book recommendation system and explaining the code is available in the repository.

https://drive.google.com/file/d/1KyAYZwwlBJcm-rcx60YXUFFPlu_Qi20e/view?usp=sharing
