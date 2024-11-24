"""create patient table

Revision ID: 22bfc8fdd1ca
Revises: 0f28ae749e3f
Create Date: 2024-11-23 20:45:22.494742

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22bfc8fdd1ca'
down_revision: Union[str, None] = '0f28ae749e3f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'patient',
        sa.Column('_id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('patient_name', sa.String(35), nullable=False),
        sa.Column('MRN', sa.Integer(), nullable=True, autoincrement=True),
        sa.Column('phone_number', sa.String(10), nullable=False),
        sa.Column('address', sa.String(70), nullable=False),
        sa.Column('visit', sa.Date(), nullable=False),
        sa.Column('gender', sa.String(1), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('patient')