"""empty message

Revision ID: 2281f27dfc35
Revises: 1f0e077436a1
Create Date: 2021-05-18 21:37:00.252422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2281f27dfc35'
down_revision = '1f0e077436a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('video', 'release_date',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('video', 'release_date',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
