"""empty message

Revision ID: 019bebe20427
Revises: 5120cca446ef
Create Date: 2023-01-18 15:11:57.824088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '019bebe20427'
down_revision = '5120cca446ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('monsters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('challenge_rating', sa.Integer(), nullable=False),
    sa.Column('hit_points', sa.Integer(), nullable=False),
    sa.Column('armor_class', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('monsters')
    # ### end Alembic commands ###
