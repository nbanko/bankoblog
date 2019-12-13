"""blocked

Revision ID: d06090bf07f8
Revises: 648b36470593
Create Date: 2019-12-12 19:50:36.471336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd06090bf07f8'
down_revision = '648b36470593'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blocked',
    sa.Column('blocker_id', sa.Integer(), nullable=True),
    sa.Column('blocked_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blocked_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['blocker_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blocked')
    # ### end Alembic commands ###
