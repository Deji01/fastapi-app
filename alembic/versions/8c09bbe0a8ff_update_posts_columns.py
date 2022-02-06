"""update posts columns

Revision ID: 8c09bbe0a8ff
Revises: e172210ed263
Create Date: 2022-02-06 22:26:02.969866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c09bbe0a8ff'
down_revision = 'e172210ed263'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
                  sa.Column('owner_id', sa.Integer(), nullable=False)),
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=[
                          "owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
