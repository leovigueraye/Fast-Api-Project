"""add last few columns to posts table

Revision ID: 270391cb4682
Revises: 2d893ac7f21c
Create Date: 2022-10-01 08:15:44.932799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '270391cb4682'
down_revision = '2d893ac7f21c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
