"""fix typo 'cater' to 'cate'

Revision ID: 36c66835b2c9
Revises: 4d01918c9aac
Create Date: 2015-11-10 01:38:39.181344

"""

# revision identifiers, used by Alembic.
revision = '36c66835b2c9'
down_revision = '4d01918c9aac'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction', sa.Column('category_id', sa.Integer(), nullable=True))
    op.drop_constraint(u'transaction_ibfk_1', 'transaction', type_='foreignkey')
    op.create_foreign_key(None, 'transaction', 'category', ['category_id'], ['id'])
    op.drop_column('transaction', 'catergory_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction', sa.Column('catergory_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'transaction', type_='foreignkey')
    op.create_foreign_key(u'transaction_ibfk_1', 'transaction', 'category', ['catergory_id'], ['id'])
    op.drop_column('transaction', 'category_id')
    ### end Alembic commands ###
