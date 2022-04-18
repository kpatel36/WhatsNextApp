"""empty message

Revision ID: 6bc386d9d8f2
Revises: e49459a5346c
Create Date: 2022-04-14 22:35:46.425245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bc386d9d8f2'
down_revision = 'e49459a5346c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie_faves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_title', sa.String(length=150), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie_watchlist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_title', sa.String(length=150), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_watchlist')
    op.drop_table('movie_faves')
    # ### end Alembic commands ###
