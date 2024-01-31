from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func
from sqlalchemy import DateTime


class Comment(db.Model):
    __tablename__ = 'comments'
        
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(DateTime(timezone=True), onupdate=func.now())


    # COMMENT THIS IN ONCE RECIPES IS CREATED
    recipeId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)
    recipe = db.relationship('Recipe', back_populates='comments')

    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    user = db.relationship('User', back_populates='comments')

    comment = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'recipeId': self.recipeId,
            'userId': self.userId,
            'comment': self.comment,
            'user': self.user.to_dict(),
            'time_created': self.time_created
        }
