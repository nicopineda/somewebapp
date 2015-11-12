"""rename Account to User and set User.username to unique

Revision ID: 4d01918c9aac
Revises: 5257c370c8d3
Create Date: 2015-11-09 21:30:26.258960

"""

# revision identifiers, used by Alembic.
revision = '4d01918c9aac'
down_revision = '5257c370c8d3'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=254), nullable=True),
    sa.Column('lastname', sa.String(length=254), nullable=True),
    sa.Column('username', sa.String(length=254), nullable=True),
    sa.Column('password', sa.String(length=254), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.add_column('category', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint(u'category_ibfk_1', 'category', type_='foreignkey')
    op.create_foreign_key(None, 'category', 'user', ['user_id'], ['id'])
    op.drop_column('category', 'account_id')
    op.add_column('transaction', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint(u'transaction_ibfk_1', 'transaction', type_='foreignkey')
    op.drop_constraint(u'transaction_ibfk_2', 'transaction', type_='foreignkey')
    op.create_foreign_key(None, 'transaction', 'category', ['catergory_id'], ['id'])
    op.create_foreign_key(None, 'transaction', 'user', ['user_id'], ['id'])
    op.drop_column('transaction', 'account_id')
    op.drop_table('account')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction', sa.Column('account_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'transaction', type_='foreignkey')
    op.drop_constraint(None, 'transaction', type_='foreignkey')
    op.create_foreign_key(u'transaction_ibfk_2', 'transaction', 'category', ['catergory_id'], ['id'], ondelete=u'SET NULL')
    op.create_foreign_key(u'transaction_ibfk_1', 'transaction', 'account', ['account_id'], ['id'], ondelete=u'SET NULL')
    op.drop_column('transaction', 'user_id')
    op.add_column('category', sa.Column('account_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'category', type_='foreignkey')
    op.create_foreign_key(u'category_ibfk_1', 'category', 'account', ['account_id'], ['id'], ondelete=u'SET NULL')
    op.drop_column('category', 'user_id')
    op.create_table('account',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('firstname', mysql.VARCHAR(length=254), nullable=True),
    sa.Column('lastname', mysql.VARCHAR(length=254), nullable=True),
    sa.Column('username', mysql.VARCHAR(length=254), nullable=True),
    sa.Column('password', mysql.VARCHAR(length=254), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('user')
    ### end Alembic commands ###