"""add posts table

Revision ID: e172210ed263
Revises: b138179461e3
Create Date: 2022-02-06 21:58:56.918314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e172210ed263'
down_revision = 'b138179461e3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(),
                              nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))

    pass


def downgrade():
    op.drop_table('posts')
    pass
