from .db import db, environment, SCHEMA, add_prefix_for_prod


class Media(db.Model):
    __tablename__ = 'media'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)

    #COMMENT THIS IN ONCE RECIPES IS CREATED
    recipeId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)
    recipe = db.relationship('Recipe', back_populates='medias')
    mediaUrl = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'mediaUrl': self.mediaUrl,
            'recipeId': self.recipeId
        }
