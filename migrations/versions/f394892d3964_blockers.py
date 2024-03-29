"""blockers

Revision ID: f394892d3964
Revises: d06090bf07f8
Create Date: 2019-12-12 20:24:04.422176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f394892d3964'
down_revision = 'd06090bf07f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blockers',
    sa.Column('blocker_id', sa.Integer(), nullable=True),
    sa.Column('blocked_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blocked_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['blocker_id'], ['user.id'], )
    )
    op.drop_table('blocked')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blocked',
    sa.Column('blocker_id', sa.INTEGER(), nullable=True),
    sa.Column('blocked_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['blocked_id'], [u'user.id'], ),
    sa.ForeignKeyConstraint(['blocker_id'], [u'user.id'], )
    )
    op.drop_table('blockers')
    # ### end Alembic commands ###
