from .db import db, environment, SCHEMA, add_prefix_for_prod


class Like(db.Model):
    __tablename__ = 'likes'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)

    #COMMENT THIS IN ONCE RECIPES IS CREATED
    recipeId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)
    recipe = db.relationship('Recipe', back_populates='likes')

    userId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    user = db.relationship('User', back_populates='likes')

    def to_dict(self):
        return {
            'id': self.id,
            'recipeId': self.recipeId,
            'userId': self.userId,
        }
