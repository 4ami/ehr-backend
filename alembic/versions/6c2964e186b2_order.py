"""order

Revision ID: 6c2964e186b2
Revises: 6c157b95aecc
Create Date: 2024-11-25 01:23:36.070306

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '6c2964e186b2'
down_revision: Union[str, None] = '6c157b95aecc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'order',
        sa.Column(name='_id', type_= sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column(name='type', type_= sa.Enum('CONSULTATION', 'LAB', 'IMAGING', 'MEDICATION')),
        sa.Column(name='status', type_= sa.Enum('PENDING', 'PROCESSED', 'REJECTED'), default='PENDING'),
        sa.Column(name='department', type_= sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['department'], ['department._id'], ondelete='SET NULL', onupdate='CASCADE')
    )


def downgrade() -> None:
    op.drop_table('order')
