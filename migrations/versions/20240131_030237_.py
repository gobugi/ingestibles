"""empty message

Revision ID: 54a12b0b9a3c
Revises: 
Create Date: 2024-01-31 03:02:37.824620

"""
from alembic import op
import sqlalchemy as sa


import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = '54a12b0b9a3c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('biography', sa.Text(), nullable=True),
    sa.Column('profilePic', sa.String(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('recipes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('ingredientPhoto', sa.String(), nullable=False),
    sa.Column('authorId', sa.Integer(), nullable=False),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['authorId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('recipeId', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipeId', sa.Integer(), nullable=False),
    sa.Column('info', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('instructions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipeId', sa.Integer(), nullable=False),
    sa.Column('imageUrl', sa.String(), nullable=True),
    sa.Column('stepTitle', sa.String(), nullable=False),
    sa.Column('directions', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipeId', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipeId', sa.Integer(), nullable=False),
    sa.Column('mediaUrl', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('recipeId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE recipes SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE comments SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE ingredients SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE instructions SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE likes SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE media SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE tags SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    op.drop_table('media')
    op.drop_table('likes')
    op.drop_table('instructions')
    op.drop_table('ingredients')
    op.drop_table('comments')
    op.drop_table('recipes')
    op.drop_table('users')
    # ### end Alembic commands ###