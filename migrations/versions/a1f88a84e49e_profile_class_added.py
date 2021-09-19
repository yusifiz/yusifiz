"""Profile class added

Revision ID: a1f88a84e49e
Revises: f1f2c2264a9f
Create Date: 2021-09-10 00:30:31.700327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1f88a84e49e'
down_revision = 'f1f2c2264a9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prof_name', sa.String(length=50), nullable=True),
    sa.Column('prof_age', sa.String(length=10), nullable=True),
    sa.Column('prof_email', sa.String(length=100), nullable=True),
    sa.Column('prof_phone', sa.String(length=50), nullable=True),
    sa.Column('prof_adress', sa.String(length=50), nullable=True),
    sa.Column('prof_img', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    # ### end Alembic commands ###
