"""empty message

Revision ID: 6e30df07125b
Revises: 9a00ae26c6f8
Create Date: 2016-10-17 03:14:49.500598

"""

# revision identifiers, used by Alembic.
revision = '6e30df07125b'
down_revision = '9a00ae26c6f8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('title', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'title')
    ### end Alembic commands ###