"""New node_class column in comp_tasks

Revision ID: f3555bb4bc34
Revises: 43b26b6e762b
Create Date: 2020-02-28 14:12:14.444624+00:00

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f3555bb4bc34'
down_revision = '43b26b6e762b'
branch_labels = None
depends_on = None


# NOTE: Autogenerate does not properly handle postgres ENUM
# https://github.com/sqlalchemy/alembic/issues/278
#

def upgrade():
    nodeclass = postgresql.ENUM('COMPUTATIONAL', 'INTERACTIVE', 'FRONTEND', name='nodeclass')
    nodeclass.create(op.get_bind())

    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comp_tasks', sa.Column('node_class', sa.Enum('COMPUTATIONAL', 'INTERACTIVE', 'FRONTEND', name='nodeclass'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comp_tasks', 'node_class')
    # ### end Alembic commands ###

    nodeclass = postgresql.ENUM('COMPUTATIONAL', 'INTERACTIVE', 'FRONTEND', name='nodeclass')
    nodeclass.drop(op.get_bind())
