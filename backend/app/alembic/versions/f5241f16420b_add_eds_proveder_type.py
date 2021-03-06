"""add eds_proveder_type

Revision ID: f5241f16420b
Revises: d4867f3a4c0a
Create Date: 2022-04-21 07:03:22.432598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5241f16420b'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eds_provider_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nameRu', sa.String(), nullable=True),
    sa.Column('nameKz', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_eds_provider_type_id'), 'eds_provider_type', ['id'], unique=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_index(op.f('ix_eds_provider_type_id'), table_name='eds_provider_type')
    op.drop_table('eds_provider_type')
    # ### end Alembic commands ###
