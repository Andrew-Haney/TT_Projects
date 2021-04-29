"""Main file for Airbnb Price Predicter."""

import json
import os
from os import getenv
from tempfile import mkdtemp
import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request
from joblib import load

from .models import DB, Listing


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv(
        "DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)

    features = load_features()

    # airbnb_model = load("Unit_4_PLACEHOLDER")

    listing = {}

    @app.route('/')
    def root():
        return render_template('predict-one.html', forms=features, title="Home")

    @app.route('/add_listing', methods=["GET", "POST"])
    def add_listing():
        """Add a new listing to the database"""
        if request.method == "POST":
            listing = get_input_data()
        return render_template('listing.html', title="Add a Listing", forms=features, message=f"{listing}")

    @app.route('/predict', methods=["POST"])
    def predict():
        return render_template('predict.html', title='Home', message="Coming Soon")

    @app.route('/reset')
    def test_db():
        listing = {}
        DB.drop_all()
        DB.create_all()
        return "DB created"

    @app.route('/return-all')
    def return_db_entries():
        temp_db_query = Listing.query.all()
        list_of_listings = []
        for id in temp_db_query:
            list_of_listings.append(id)
        print("A" + str(list_of_listings))
        return render_template('return-all.html', title="List of Listings", listings=list_of_listings)

    return app


def load_features():
    feature_order = get_feature_orders()
    with open('features.json') as file:
        all_possible = json.load(file)
        features = {feature: all_possible[feature]
                    for feature in feature_order}
        return features


def get_feature_orders():
    feature_order = [
        "property_type",
        "room_type",
        "accommodates",
        "bedrooms",
        "baths",
        "zip",
    ]
    return feature_order


# def get_input_data():
#     listing = {}
#     features = load_features()
