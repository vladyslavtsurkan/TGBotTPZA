"""initial

Revision ID: 3e25b5b80864
Revises: 
Create Date: 2022-10-26 22:29:39.456927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e25b5b80864'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bot_disciplines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('bot_faculties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('title_short', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('bot_teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('full_name')
    )
    op.create_table('bot_departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('title_short', sa.String(length=10), nullable=False),
    sa.Column('faculty_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['faculty_id'], ['bot_faculties.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('bot_lessons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('discipline_id', sa.Integer(), nullable=True),
    sa.Column('week', sa.Integer(), nullable=False),
    sa.Column('day', sa.Integer(), nullable=False),
    sa.Column('number_lesson', sa.Integer(), nullable=False),
    sa.Column('type_and_location', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['discipline_id'], ['bot_disciplines.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bot_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=10), nullable=True),
    sa.Column('schedule_url', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['bot_departments.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('lesson_teacher',
    sa.Column('lesson_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lesson_id'], ['bot_lessons.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['bot_teachers.id'], )
    )
    op.create_table('bot_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['bot_groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lesson_group',
    sa.Column('lesson_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['bot_groups.id'], ),
    sa.ForeignKeyConstraint(['lesson_id'], ['bot_lessons.id'], )
    )
    op.create_table('bot_tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['bot_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bot_tasks')
    op.drop_table('lesson_group')
    op.drop_table('bot_users')
    op.drop_table('lesson_teacher')
    op.drop_table('bot_groups')
    op.drop_table('bot_lessons')
    op.drop_table('bot_departments')
    op.drop_table('bot_teachers')
    op.drop_table('bot_faculties')
    op.drop_table('bot_disciplines')
    # ### end Alembic commands ###
