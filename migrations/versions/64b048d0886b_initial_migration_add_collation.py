"""Initial migration, add collation

Revision ID: 64b048d0886b
Revises: 
Create Date: 2024-11-07 14:02:06.737849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64b048d0886b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE COLLATION IF NOT EXISTS numeric (provider = icu, locale = "en-u-kn-true");')
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sat_version',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jenkins_job', sa.String(length=200), nullable=False),
    sa.Column('sat_version', sa.String(length=32, collation='numeric'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('container',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('image', sa.String(length=200), nullable=False),
    sa.Column('sat_version_id', sa.Integer(), nullable=False),
    sa.Column('first_seen', sa.DateTime(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['sat_version_id'], ['sat_version.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('instance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('flavor', sa.String(length=200), nullable=False),
    sa.Column('image', sa.String(length=200), nullable=False),
    sa.Column('sat_version_id', sa.Integer(), nullable=False),
    sa.Column('first_seen', sa.DateTime(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['sat_version_id'], ['sat_version.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('instance')
    op.drop_table('container')
    op.drop_table('sat_version')
    # ### end Alembic commands ###
    op.execute('DROP COLLATION IF EXISTS numeric;')
