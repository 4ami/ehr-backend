"""users-table

Revision ID: 0f28ae749e3f
Revises: 
Create Date: 2024-11-23 19:37:52.813802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f28ae749e3f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('_id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('userId', sa.String(35), nullable=False, unique=True),
        sa.Column('full_name', sa.String(70), nullable=False),
        sa.Column('role', sa.Enum('RECEPTIONIST', 'PHARMACIST', 'CASHIER'), nullable=False),
        sa.Column('password', sa.String(257), nullable=False)
   )


def downgrade() -> None:
    op.drop_table('user')
