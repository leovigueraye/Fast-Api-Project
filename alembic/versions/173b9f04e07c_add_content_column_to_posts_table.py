"""add content column to posts table

Revision ID: 173b9f04e07c
Revises: d196fef52d30
Create Date: 2022-10-01 07:38:02.261074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '173b9f04e07c'
down_revision = 'd196fef52d30'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
