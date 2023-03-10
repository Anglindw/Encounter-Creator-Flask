"""empty message

Revision ID: 164bef95106a
Revises: 322e4a46ef70
Create Date: 2023-01-25 21:53:54.925182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '164bef95106a'
down_revision = '322e4a46ef70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.add_column(sa.Column('challenge_score', sa.Float(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.drop_column('challenge_score')

    # ### end Alembic commands ###
