"""First tables

Revision ID: 211f870b8768
Revises: 28538631bd38
Create Date: 2022-12-04 23:27:47.851639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '211f870b8768'
down_revision = '28538631bd38'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_tweet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_user')
    op.drop_table('tb_tweet')
    # ### end Alembic commands ###
