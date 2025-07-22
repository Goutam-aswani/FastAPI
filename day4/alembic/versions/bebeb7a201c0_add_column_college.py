"""add column college

Revision ID: bebeb7a201c0
Revises: 
Create Date: 2025-07-18 18:19:38.966994

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bebeb7a201c0'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'interns',
        sa.Column(
            'college',
            sa.String(),
            nullable=True,
            comment='College of the intern'
        )
    )


def downgrade() -> None:
    op.drop_column('interns', 'college')
    
