"""Upgraded Tweet related classes

Revision ID: 3e0395cc0374
Revises: 211f870b8768
Create Date: 2022-12-05 00:40:52.885631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3e0395cc0374"
down_revision = "211f870b8768"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tb_domain",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "tb_entity",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "tb_tweet_domain",
        sa.Column("tweet_id", sa.Integer(), nullable=False),
        sa.Column("domain_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["domain_id"],
            ["tb_domain.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tweet_id"],
            ["tb_tweet.id"],
        ),
        sa.PrimaryKeyConstraint("tweet_id", "domain_id"),
    )
    op.create_table(
        "tb_tweet_entity",
        sa.Column("tweet_id", sa.Integer(), nullable=False),
        sa.Column("entity_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["entity_id"],
            ["tb_entity.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tweet_id"],
            ["tb_tweet.id"],
        ),
        sa.PrimaryKeyConstraint("tweet_id", "entity_id"),
    )
    op.add_column("tb_tweet", sa.Column("user_id", sa.Integer(), nullable=True))
    op.add_column("tb_tweet", sa.Column("created_at", sa.DateTime(), nullable=False))
    op.add_column("tb_tweet", sa.Column("lang", sa.String(), nullable=False))
    op.create_foreign_key(None, "tb_tweet", "tb_user", ["user_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "tb_tweet", type_="foreignkey")
    op.drop_column("tb_tweet", "lang")
    op.drop_column("tb_tweet", "created_at")
    op.drop_column("tb_tweet", "user_id")
    op.drop_table("tb_tweet_entity")
    op.drop_table("tb_tweet_domain")
    op.drop_table("tb_entity")
    op.drop_table("tb_domain")
    # ### end Alembic commands ###
