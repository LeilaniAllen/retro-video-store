from app import db
from datetime import datetime
from flask import current_app
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


# videos_fk = db.Table('videos_fk',
#     db.Column('video_id', db.Integer, db.ForeignKey('video.id'), primary_key=True),
#     db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'), primary_key=True)
# )

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    postal_code = db.Column(db.Integer)
    phone = db.Column(db.String)
    registered_at = db.Column(db.DateTime(), nullable=True)
    videos_checked_out_count = db.Column(db.Integer, default =0)
    # Making a relationship with the word "rentals" and customer which will now be tied together
    rentals = db.relationship("Rental", back_populates="customer")


    # helper function  display  json
    def display_json(self):
        return {
                "id": self.customer_id,
                "name": self.name,
                "registered_at": self.registered_at,
                "postal_code": str(self.postal_code),
                "phone": self.phone,
                "videos_checked_out_count": self.videos_checked_out_count
                }  




