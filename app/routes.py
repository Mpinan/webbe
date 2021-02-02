from flask import Flask
from flask import jsonify, request, json

from app.models.reviews_model import Review
from app import app

import os


@app.route('/')

@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/reviews', methods=['GET'])
def get_all_reviews():
    all_reviews = Review.get_all_reviews()
    return jsonify(
        reviews = [review.reviews_serializer for review in all_reviews]
        )

@app.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.get_one_review(review_id)
    return jsonify(review)

@app.route("/submit_review", methods=["POST"])
def submit_review():
    incoming = request.get_json()

    success, id = Review.save(Review (
        incoming["review_name"],
        incoming["review_text"],

        ))

    if not success:
        return jsonify(message="Error submitting review", id=None), 409

    return jsonify(success=True, id=id)