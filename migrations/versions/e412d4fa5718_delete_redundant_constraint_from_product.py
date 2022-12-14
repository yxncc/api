"""delete redundant constraint from product

Revision ID: e412d4fa5718
Revises: c6bc4cf2a55d
Create Date: 2022-11-12 18:52:25.822133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e412d4fa5718'
down_revision = 'c6bc4cf2a55d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('products_provider_id_key', 'products', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('products_provider_id_key', 'products', ['provider_id'])
    # ### end Alembic commands ###
