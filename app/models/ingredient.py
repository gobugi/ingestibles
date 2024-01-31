from .db import db, environment, SCHEMA, add_prefix_for_prod


class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)


    # COMMENT THIS IN ONCE RECIPES IS CREATED
    recipeId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)
    recipe = db.relationship('Recipe', back_populates='ingredients')

    info = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'recipeId': self.recipeId,
            'info': self.info
        }
