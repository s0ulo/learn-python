"""Add email to User model

Revision ID: 426e8ba1aa63
Revises: 17f63308693c
Create Date: 2020-10-19 00:25:03.311818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '426e8ba1aa63'
down_revision = '17f63308693c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###