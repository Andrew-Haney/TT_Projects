"""SQLAlchemy models for Airbnb"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class Listing(DB.Model):
    """Airbnb listings corresponding to Hosts"""
    id = DB.Column(DB.Integer, primary_key=True)
    property_type = DB.Column(DB.String, nullable=False)
    room_type = DB.Column(DB.String, nullable=False)
    accommodates = DB.Column(DB.Integer, nullable=False)
    bedrooms = DB.Column(DB.Integer, nullable=False)
    baths = DB.Column(DB.Numeric, nullable=False)
    zip = DB.Column(DB.Integer, nullable=False)

    def __repr__(self):
        rep = f"""Id: {self.id} Property Type: {self.property_type} Room Type: {self.room_type} Accommodates: {self.accommodates} Bedrooms: {self.bedrooms} Baths: {self.baths} Zip: {self.zip}"""
        return rep
