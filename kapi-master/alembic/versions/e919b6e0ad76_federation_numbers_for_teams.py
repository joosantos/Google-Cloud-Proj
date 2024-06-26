"""Federation numbers for teams

Revision ID: e919b6e0ad76
Revises: 52e4f79a5241
Create Date: 2024-01-31 14:57:52.417335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e919b6e0ad76'
down_revision = '52e4f79a5241'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teams', sa.Column('federation_number', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('teams', 'federation_number')
    # ### end Alembic commands ###
