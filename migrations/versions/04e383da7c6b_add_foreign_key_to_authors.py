"""add foreign key to authors

Revision ID: 04e383da7c6b
Revises: 4741e6224ff0
Create Date: 2025-05-15 15:52:53.362869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04e383da7c6b'
down_revision: Union[str, None] = '4741e6224ff0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_books_author_id_authors', 'authors', ['author_id'], ['id'])

def downgrade():
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_constraint('fk_books_author_id_authors', type_='foreignkey')
        batch_op.drop_column('author_id')
