"""empty message

Revision ID: 079ad0f968d7
Revises: b4cf6a71c525
Create Date: 2022-04-21 15:34:39.484816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '079ad0f968d7'
down_revision = 'b4cf6a71c525'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('signDate', sa.DateTime(), nullable=True),
    sa.Column('certStartDate', sa.DateTime(), nullable=True),
    sa.Column('certEndtDate', sa.DateTime(), nullable=True),
    sa.Column('certOwner', sa.String(), nullable=True),
    sa.Column('PUID', sa.String(), nullable=True),
    sa.Column('cert', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('signedFieldsSequence', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('signedFilesIdSequence', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('providerTypeId', sa.Integer(), nullable=True),
    sa.Column('signatureId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['providerTypeId'], ['eds_provider_type.id'], ),
    sa.ForeignKeyConstraint(['signatureId'], ['signature.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_eds_id'), 'eds', ['id'], unique=False)
    op.add_column('signature', sa.Column('edsId', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'signature', 'eds', ['edsId'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'signature', type_='foreignkey')
    op.drop_column('signature', 'edsId')
    op.drop_index(op.f('ix_eds_id'), table_name='eds')
    op.drop_table('eds')
    # ### end Alembic commands ###
