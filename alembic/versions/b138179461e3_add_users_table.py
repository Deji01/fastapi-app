"""add users table

Revision ID: b138179461e3
Revises: b6c0c95f2310
Create Date: 2022-02-06 20:49:20.182794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b138179461e3'
down_revision = 'b6c0c95f2310'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
