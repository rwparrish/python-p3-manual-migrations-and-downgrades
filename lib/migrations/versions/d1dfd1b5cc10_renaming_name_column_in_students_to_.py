"""Renaming name column in students to student_name

Revision ID: d1dfd1b5cc10
Revises: 791279dd0760
Create Date: 2023-06-05 13:06:14.633162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1dfd1b5cc10'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='student_name')


def downgrade() -> None:
    op.alter_column('students', 'student_name', new_column_name='name')
