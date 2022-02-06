"""add last few columns to post table

Revision ID: f8fb374a5fd0
Revises: 8c09bbe0a8ff
Create Date: 2022-02-06 22:44:54.100146

"""
from http import server
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8fb374a5fd0'
down_revision = '8c09bbe0a8ff'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
