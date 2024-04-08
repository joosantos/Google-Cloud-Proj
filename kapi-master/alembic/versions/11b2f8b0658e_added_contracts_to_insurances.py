"""Added contracts to insurances

Revision ID: 11b2f8b0658e
Revises: 0859540fd898
Create Date: 2024-01-29 17:36:23.804019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11b2f8b0658e'
down_revision = '0859540fd898'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('insurances', sa.Column('contract_url', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('insurances', 'contract_url')
    # ### end Alembic commands ###
