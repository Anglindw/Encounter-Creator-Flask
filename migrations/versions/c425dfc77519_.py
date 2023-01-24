"""empty message

Revision ID: c425dfc77519
Revises: f3e836d9d8b2
Create Date: 2023-01-18 19:13:04.855557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c425dfc77519'
down_revision = 'f3e836d9d8b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('monsters', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['name'])

    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.drop_constraint('team_name_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('team', schema=None) as batch_op:
        batch_op.create_unique_constraint('team_name_key', ['name'])

    with op.batch_alter_table('monsters', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
