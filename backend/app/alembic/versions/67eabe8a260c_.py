"""empty message

Revision ID: 67eabe8a260c
Revises: 8274e212158a
Create Date: 2022-04-22 06:17:37.053142

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '67eabe8a260c'
down_revision = '8274e212158a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('eds', 'signedFilesIdSequence',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               type_=sa.ARRAY(sa.Integer()),
               existing_nullable=True)
    op.add_column('signer', sa.Column('employeeId', sa.Integer(), nullable=True))
    op.add_column('signer', sa.Column('fullNameRu', sa.String(), nullable=True))
    op.add_column('signer', sa.Column('fullNameKz', sa.String(), nullable=True))
    op.add_column('signer', sa.Column('positionRu', sa.String(), nullable=True))
    op.add_column('signer', sa.Column('positionKz', sa.String(), nullable=True))
    op.add_column('signer', sa.Column('departmentRu', sa.String(), nullable=True))
    op.add_column('signer', sa.Column('departmentKz', sa.String(), nullable=True))
    op.drop_column('signer', 'nameRu')
    op.drop_column('signer', 'nameKz')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('signer', sa.Column('nameKz', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('signer', sa.Column('nameRu', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('signer', 'departmentKz')
    op.drop_column('signer', 'departmentRu')
    op.drop_column('signer', 'positionKz')
    op.drop_column('signer', 'positionRu')
    op.drop_column('signer', 'fullNameKz')
    op.drop_column('signer', 'fullNameRu')
    op.drop_column('signer', 'employeeId')
    op.alter_column('eds', 'signedFilesIdSequence',
               existing_type=sa.ARRAY(sa.Integer()),
               type_=postgresql.ARRAY(sa.VARCHAR()),
               existing_nullable=True)
    # ### end Alembic commands ###
