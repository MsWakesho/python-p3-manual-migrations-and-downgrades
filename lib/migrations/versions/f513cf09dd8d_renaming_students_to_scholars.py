"""Renaming students to scholars

Revision ID: f513cf09dd8d
Revises: 791279dd0760
Create Date: 2024-03-25 12:24:48.232493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f513cf09dd8d'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
     op.rename_table('scholars', 'students')
