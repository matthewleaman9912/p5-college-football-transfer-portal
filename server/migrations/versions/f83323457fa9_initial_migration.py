"""initial migration

Revision ID: f83323457fa9
Revises: 0aeab8eb5343
Create Date: 2025-01-26 14:17:01.761566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f83323457fa9'
down_revision = '0aeab8eb5343'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coaches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('playing_style', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('_password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('mascot', sa.String(), nullable=True),
    sa.Column('wins', sa.Integer(), nullable=True),
    sa.Column('theme', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('city'),
    sa.UniqueConstraint('mascot')
    )
    op.create_table('rosters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roster_size', sa.Integer(), nullable=True),
    sa.Column('level', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('coach_id', sa.Integer(), nullable=True),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['coach_id'], ['coaches.id'], name=op.f('fk_rosters_coach_id_coaches')),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], name=op.f('fk_rosters_team_id_teams')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('position', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('roster_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['roster_id'], ['rosters.id'], name=op.f('fk_players_roster_id_rosters')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('players')
    op.drop_table('rosters')
    op.drop_table('teams')
    op.drop_table('coaches')
    # ### end Alembic commands ###
