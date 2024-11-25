"""department

Revision ID: 6c157b95aecc
Revises: 22bfc8fdd1ca
Create Date: 2024-11-25 01:22:32.272805

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c157b95aecc'
down_revision: Union[str, None] = '22bfc8fdd1ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'department',
        sa.Column(name='_id', type_=sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column(name='dept_name', type_=sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('department')
