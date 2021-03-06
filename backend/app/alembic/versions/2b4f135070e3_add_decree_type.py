"""Add decree_type

Revision ID: 2b4f135070e3
Revises: e5833da0286c
Create Date: 2022-04-21 08:34:07.564660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b4f135070e3'
down_revision = 'e5833da0286c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('decree_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nameRu', sa.String(), nullable=True),
    sa.Column('nameKz', sa.String(), nullable=True),
    sa.Column('registrationIndex', sa.String(), nullable=True),
    sa.Column('registrationPrefix', sa.String(), nullable=True),
    sa.Column('isActive', sa.Integer(), nullable=True),
    sa.Column('kindId', sa.Integer(), nullable=True),
    sa.Column('counterId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['counterId'], ['counter.id'], ),
    sa.ForeignKeyConstraint(['kindId'], ['decree_kind.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_decree_type_id'), 'decree_type', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_decree_type_id'), table_name='decree_type')
    op.drop_table('decree_type')
    # ### end Alembic commands ###
