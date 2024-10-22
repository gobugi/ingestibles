from .db import db, environment, SCHEMA, add_prefix_for_prod


class Instruction(db.Model):
    __tablename__ = 'instructions'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)


    # COMMENT THIS IN ONCE RECIPES IS CREATED
    recipeId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('recipes.id')), nullable=False)
    recipe = db.relationship('Recipe', back_populates='instructions')

    imageUrl = db.Column(db.String, nullable=True)
    stepTitle = db.Column(db.String, nullable=False)
    directions = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'imageUrl': self.imageUrl,
            'stepTitle': self.stepTitle,
            'directions': self.directions,
            'recipeId': self.recipeId
        }
